#!/usr/bin/env python3
"""Prepare preview backgrounds for the web.

    pip install pillow
    python3 tools/make_thumbs.py

For every image in backgrounds/ this:
  * writes a web-sized progressive JPEG (max 1600px wide) in place, and
  * writes a small picker thumbnail to backgrounds/thumbs/.

Full-size PNG screenshots are ~1 MB each; this takes the whole set from
several megabytes to a few dozen kilobytes on first paint. Drop a raw
screenshot in backgrounds/, run this, then add one line to crosshairs.js.

Source PNGs are replaced by their JPEG version (pass --keep to keep them).
"""

import os
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow is required:  pip install pillow")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKGROUNDS = os.path.join(ROOT, "backgrounds")
THUMBS = os.path.join(BACKGROUNDS, "thumbs")

MAX_WIDTH = 1600
THUMB_BOX = (360, 202)
SOURCE_EXT = (".png", ".jpg", ".jpeg", ".webp", ".bmp")


def main():
    keep = "--keep" in sys.argv
    os.makedirs(THUMBS, exist_ok=True)

    sources = sorted(
        f for f in os.listdir(BACKGROUNDS)
        if f.lower().endswith(SOURCE_EXT) and os.path.isfile(os.path.join(BACKGROUNDS, f))
    )
    if not sources:
        print("No images found in backgrounds/")
        return

    for fname in sources:
        path = os.path.join(BACKGROUNDS, fname)
        stem = os.path.splitext(fname)[0]
        target = os.path.join(BACKGROUNDS, stem + ".jpg")
        before = os.path.getsize(path)

        with Image.open(path) as src:
            img = src.convert("RGB")

        full = img.copy()
        if full.width > MAX_WIDTH:
            full = full.resize(
                (MAX_WIDTH, round(full.height * MAX_WIDTH / full.width)), Image.LANCZOS
            )
        full.save(target, "JPEG", quality=82, optimize=True, progressive=True)

        thumb = img.copy()
        thumb.thumbnail(THUMB_BOX, Image.LANCZOS)
        thumb.save(os.path.join(THUMBS, stem + ".jpg"), "JPEG", quality=78, optimize=True)

        if path != target and not keep:
            os.remove(path)

        after = os.path.getsize(target)
        print(f"{fname}: {before // 1024} KB -> {after // 1024} KB (+ thumbnail)")

    print("\nDone. Now list the .jpg names in the BACKGROUNDS list in crosshairs.js.")


if __name__ == "__main__":
    main()
