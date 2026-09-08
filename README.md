# Roblox Crosshair Library

A static site listing Roblox crosshair decal IDs, with a live cursor preview
over in-game screenshots. No build step, no dependencies.

To view it locally, serve the folder rather than double-clicking the file:

```sh
python3 -m http.server 8000    # then open http://localhost:8000
```

Opening `index.html` straight from disk still works, but browsers block
reading image pixels over `file://`, so the card auto-zoom and the downscaled
cursor for large decals quietly turn themselves off.

---

## Adding a crosshair

Two steps. You only ever edit **one** file.

**1. Save the image** into `images/`, named after its Roblox ID:

```
images/123456789.png
```

**2. Add one line** to the `CROSSHAIRS` list in [`crosshairs.js`](crosshairs.js):

```js
{ id: "123456789", name: "My Crosshair", color: "red" },
```

Save, refresh the page. Done.

### Fields

| Field   | Required | What it does |
|---------|----------|--------------|
| `id`    | yes      | Roblox decal ID. **Must match the image filename.** |
| `name`  | no       | Card label. Falls back to the ID. |
| `color` | no       | Powers the colour filter buttons. Leave it out and the crosshair still shows under **All**. |
| `tags`  | no       | Extra search words, e.g. `tags: "sniper thin outline"` |

Valid `color` values: `white` `black` `red` `orange` `yellow` `green` `cyan`
`blue` `purple` `pink`. The filter bar builds itself from whatever colours the
list actually uses, so a new colour appears on its own.

### Adding several at once

Just add several lines. The list renders top to bottom, so put new or popular
crosshairs near the top if you want them seen first. The `// ---- Green ----`
comments are only there for your convenience — nothing depends on them.

---

## Adding a preview background

**1.** Drop a screenshot into `backgrounds/`.

**2.** Shrink it (a raw 1080p PNG screenshot is ~1 MB; this gets it to ~100 KB
and builds the picker thumbnail):

```sh
pip install pillow
python3 tools/make_thumbs.py
```

**3.** Add one line to the `BACKGROUNDS` list in `crosshairs.js`:

```js
{ file: "myshot.jpg", name: "My Game" },
```

---

## Checking your work

```sh
python3 tools/check_library.py
```

It flags crosshairs listed with no image, images you uploaded but forgot to
list, duplicate IDs, identical files, and backgrounds missing a thumbnail.
Exits non-zero if something is actually broken.

---

## Layout

```
index.html          page + styles + behaviour
crosshairs.js       the library data — the only file you edit to add content
images/<id>.png     one image per crosshair, named by Roblox ID
backgrounds/*.jpg   full-size preview backgrounds
backgrounds/thumbs/ small versions used by the picker
tools/              helper scripts (optional, not needed to run the site)
```

## Notes

* Cards load lazily and off-screen cards skip layout entirely, so the page
  stays fast as the list grows.
* Card previews auto-zoom to each decal's artwork (most decals are a few
  pixels floating in a big transparent canvas). Measured once per image and
  cached in `localStorage`, so uploading a crosshair needs no extra config.
* The picker loads thumbnails (~60 KB total); a full background is only
  fetched once you click it.
* Roblox decals larger than 128px can't be used as a CSS cursor directly, so
  the preview downscales them once and caches the result.
* Everything is client-side. Uploading = committing files to this repo.
