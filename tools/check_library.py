#!/usr/bin/env python3
"""Sanity-check the crosshair library.

    python3 tools/check_library.py

Reports:
  * crosshairs listed in crosshairs.js with no image in images/
  * images in images/ that nothing lists (upload it, forget the line)
  * duplicate IDs, duplicate names and byte-identical image files
  * backgrounds listed with no file, and backgrounds with no thumbnail

Exits non-zero if anything is broken, so it can be wired into CI later.
"""

import hashlib
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "crosshairs.js")
IMAGES = os.path.join(ROOT, "images")
BACKGROUNDS = os.path.join(ROOT, "backgrounds")
THUMBS = os.path.join(BACKGROUNDS, "thumbs")

ENTRY_RE = re.compile(r'\bid\s*:\s*["\']([^"\']+)["\']')
NAME_RE = re.compile(r'\bname\s*:\s*["\']([^"\']*)["\']')
BG_RE = re.compile(r'\bfile\s*:\s*["\']([^"\']+)["\']')


def strip_comments(text):
    """Drop /* */ and // comments so the examples in them aren't parsed."""
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    return re.sub(r"^\s*//.*$", "", text, flags=re.M)


def read_data():
    with open(DATA, encoding="utf-8") as fh:
        text = strip_comments(fh.read())
    # Split into the two list literals so background `name:` fields don't get
    # mixed in with crosshair names.
    cross_block, _, bg_block = text.partition("const BACKGROUNDS")
    entries = []
    for line in cross_block.splitlines():
        m = ENTRY_RE.search(line)
        if m:
            n = NAME_RE.search(line)
            entries.append((m.group(1), n.group(1) if n else m.group(1)))
    return entries, BG_RE.findall(bg_block)


def main():
    entries, backgrounds = read_data()
    ids = [i for i, _ in entries]
    problems, notes = [], []

    # --- duplicate IDs / names -------------------------------------
    seen = defaultdict(int)
    for i in ids:
        seen[i] += 1
    for i, n in seen.items():
        if n > 1:
            problems.append(f"duplicate id in crosshairs.js: {i} (listed {n}x)")

    names = defaultdict(list)
    for i, name in entries:
        names[name.lower()].append(i)
    for name, group in names.items():
        if len(group) > 1:
            notes.append(f"duplicate name {name!r} used by: {', '.join(group)}")

    # --- listed but missing ----------------------------------------
    on_disk = {
        os.path.splitext(f)[0]: f
        for f in os.listdir(IMAGES)
        if f.lower().endswith(".png")
    }
    for i in ids:
        if i not in on_disk:
            problems.append(f"listed but no image: images/{i}.png")

    # --- on disk but unlisted --------------------------------------
    for stem, fname in sorted(on_disk.items()):
        if stem not in seen:
            notes.append(f"image not listed in crosshairs.js: images/{fname}")

    # --- identical files -------------------------------------------
    by_hash = defaultdict(list)
    for fname in on_disk.values():
        with open(os.path.join(IMAGES, fname), "rb") as fh:
            by_hash[hashlib.md5(fh.read()).hexdigest()].append(fname)
    for group in by_hash.values():
        if len(group) > 1:
            notes.append("identical image files: " + ", ".join(sorted(group)))

    # --- backgrounds ------------------------------------------------
    for f in backgrounds:
        if not os.path.exists(os.path.join(BACKGROUNDS, f)):
            problems.append(f"background listed but missing: backgrounds/{f}")
        elif not os.path.exists(os.path.join(THUMBS, f)):
            notes.append(
                f"no thumbnail for backgrounds/{f} "
                "— run: python3 tools/make_thumbs.py"
            )

    print(f"{len(ids)} crosshairs, {len(backgrounds)} backgrounds")
    for n in notes:
        print(f"  note:  {n}")
    for p in problems:
        print(f"  ERROR: {p}")
    if problems:
        print(f"\n{len(problems)} problem(s) found.")
        return 1
    print("\nLibrary OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
