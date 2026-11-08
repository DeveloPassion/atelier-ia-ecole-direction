#!/usr/bin/env python3
"""Build the demo zips from the sources in src/demo/.

Usage, from the repository root:
    python3 tools/build_demo.py                      # public zips only
    python3 tools/build_demo.py --private-dir DIR    # also update the private copy in DIR

Public output (committed):
- fichiers-de-demo/Système Direction Saint-Exemple - notes seules (démo).zip  <- src/demo/Direction Saint-Exemple - notes seules/
- fichiers-de-demo/Système Direction Saint-Exemple en vrac (démo).zip         <- src/demo/Direction Saint-Exemple en vrac/
- documents/fichiers-de-demo.zip: the whole fichiers-de-demo/ folder, under "Fichiers de démo/"

Private output (never committed): the full demo system is the same notes inside an install of
AI Kit for Obsidian, a paid product that must not be published. With --private-dir, the script
rewrites the notes inside "DIR/Système Direction Saint-Exemple (démo).zip" (the kit files stay as
they are) and copies the "en vrac" zip to DIR. The full zip keeps its own LISEZ-MOI.txt.

Empty folders are part of the structure: git keeps them with a .gitkeep file, which the zips leave out.
"""
import argparse
import os
import shutil
import sys
import tempfile
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src", "demo")
OUT = os.path.join(ROOT, "fichiers-de-demo")
STAMP = (2026, 11, 5, 12, 0, 0)  # fixed date: the same sources give the same zips

NOTES = "Direction Saint-Exemple - notes seules"
VRAC = "Direction Saint-Exemple en vrac"
ZIPS = {
    NOTES: "Système Direction Saint-Exemple - notes seules (démo).zip",
    VRAC: "Système Direction Saint-Exemple en vrac (démo).zip",
}
FULL_ZIP = "Système Direction Saint-Exemple (démo).zip"
FULL_ROOT = "Direction Saint-Exemple"
SKIP = {".gitkeep", ".DS_Store", "Thumbs.db"}


def entries(folder):
    """Yield (relative path, absolute path or None for a folder), sorted, folders first in each level."""
    for cur, dirs, files in os.walk(folder):
        dirs.sort()
        rel = os.path.relpath(cur, folder)
        if rel != ".":
            yield rel.replace(os.sep, "/") + "/", None
        for f in sorted(files):
            if f not in SKIP:
                yield (os.path.join(rel, f) if rel != "." else f).replace(os.sep, "/"), os.path.join(cur, f)


def write_zip(path, folder, top):
    tmp = path + ".tmp"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(zipfile.ZipInfo(top + "/", STAMP), b"")
        for rel, absolute in entries(folder):
            info = zipfile.ZipInfo(f"{top}/{rel}", STAMP)
            if absolute is None:
                info.external_attr = 0o40755 << 16
                z.writestr(info, b"")
            else:
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                with open(absolute, "rb") as fh:
                    z.writestr(info, fh.read())
    os.replace(tmp, path)
    print("wrote", os.path.relpath(path, ROOT))


def update_full(full_path):
    """Replace the notes inside the private full zip; keep every other file of the zip."""
    notes = {rel: absolute for rel, absolute in entries(os.path.join(SRC, NOTES)) if absolute and rel != "LISEZ-MOI.txt"}
    tmp = tempfile.NamedTemporaryFile(delete=False, dir=os.path.dirname(full_path), suffix=".zip").name
    replaced = 0
    with zipfile.ZipFile(full_path) as old, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as new:
        seen = set()
        for info in old.infolist():
            rel = info.filename[len(FULL_ROOT) + 1:] if info.filename.startswith(FULL_ROOT + "/") else None
            if rel in notes:
                with open(notes[rel], "rb") as fh:
                    new.writestr(info, fh.read())
                seen.add(rel)
                replaced += 1
            else:
                new.writestr(info, old.read(info.filename))
        for rel in sorted(set(notes) - seen):  # notes added since the last build
            info = zipfile.ZipInfo(f"{FULL_ROOT}/{rel}", STAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            with open(notes[rel], "rb") as fh:
                new.writestr(info, fh.read())
            print("  added", rel)
    os.replace(tmp, full_path)
    print(f"updated {full_path} ({replaced} notes replaced)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--private-dir", help="folder with the private full zip (outside the repository)")
    args = ap.parse_args()

    for folder, name in ZIPS.items():
        write_zip(os.path.join(OUT, name), os.path.join(SRC, folder), folder)
    write_zip(os.path.join(ROOT, "documents", "fichiers-de-demo.zip"), OUT, "Fichiers de démo")

    if args.private_dir:
        d = os.path.abspath(args.private_dir)
        if d.startswith(ROOT + os.sep):
            sys.exit("--private-dir must be outside the repository: the full zip contains a paid product")
        full = os.path.join(d, FULL_ZIP)
        if os.path.exists(full):
            update_full(full)
        else:
            print("no full zip in", d, "(skipped)")
        shutil.copy2(os.path.join(OUT, ZIPS[VRAC]), os.path.join(d, ZIPS[VRAC]))
        print("copied", ZIPS[VRAC], "to", d)


if __name__ == "__main__":
    main()
