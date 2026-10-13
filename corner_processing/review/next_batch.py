#!/usr/bin/env python3
"""review/next_batch.py — take the next icons to review (20 by default), mark them `reviewing` and draw a sheet each.

Picks `todo` icons from review/status.json in its order (most-flagged first; icons an earlier review left for a
human, `needs-user` or a `report` proposal, come first: the AI decides those too), or the ones named with --icons, or
only those with a --flag. A `reviewing` icon is skipped unless its claim is older than CLAIM_HOURS (a reviewer
that stopped), so parallel reviewers never get the same icon.

Per icon it draws one review sheet, review/batches/<batch>/<icon>.png:
  row 1   input · all round · all sharp, 256 px, light 4 u grid, keyshape dashed (orange)
  row 2   the same three at 48 px (the real size)
  row 3   only when the input is mirror-symmetric: each drawing over its mirror; red / blue ink = not symmetric
and writes review/batches/<batch>/batch.json: per icon its flags, note, checks, the corner logs (only what
changed), the input / round / sharp path d's, and symmetry scores. Prints a short list to read.

  python3 review/next_batch.py                    # next 20 todo icons
  python3 review/next_batch.py --count 10 --flag check-fail
  python3 review/next_batch.py --count 10 --offset 20         # skip the first 20 free icons
  python3 review/next_batch.py --icons north-east.svg book-open-1.svg
  python3 review/next_batch.py --release batch-003      # give back the unreviewed icons of a batch
"""

import argparse
import datetime
import json
import os
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
STATUS = os.path.join(HERE, "status.json")
BATCHES = os.path.join(HERE, "batches")
CLAIM_HOURS = 6
BIG, SMALL = 256, 48
SYMMETRIC = 0.9      # input ink IoU with its mirror at or above this: mostly symmetric, the mirror row is drawn
NEW_ASYM = 0.01       # share of an output's ink that is lopsided where the input is symmetric: lost symmetry
ASYM_GROW = 7         # px (odd) — the input's own lopsided ink is widened this much (a hand-drawn flame tilts)
SHAPES = ("path", "line", "rect", "circle", "ellipse", "polyline", "polygon")


def now():
    return datetime.datetime.now(datetime.timezone.utc)


def stamp(t):
    return t.strftime("%Y-%m-%d %H:%M UTC")


class status_lock:
    """Hold an exclusive lock on status.json for a read-modify-write, so parallel reviewers (record.py, next_batch.py,
    build_status.py) never overwrite each other's changes."""

    def __enter__(self):
        import fcntl
        self.f = open(STATUS + ".lock", "w")
        fcntl.flock(self.f, fcntl.LOCK_EX)
        return self

    def __exit__(self, *exc):
        import fcntl
        fcntl.flock(self.f, fcntl.LOCK_UN)
        self.f.close()


def load_status():
    with open(STATUS, encoding="utf-8") as f:
        return json.load(f)


def save_status(s):
    fd, tmp = tempfile.mkstemp(dir=HERE, suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(s, f, indent=1, ensure_ascii=False)
        f.write("\n")
    os.replace(tmp, STATUS)


def render(svg_path, size):
    out = subprocess.run(["rsvg-convert", "-w", str(size), "-h", str(size), "-b", "white", svg_path],
                         capture_output=True, check=True).stdout
    from io import BytesIO
    return Image.open(BytesIO(out)).convert("RGB")


def guides(size, ks):
    """Transparent overlay: 4 u grid and the keyshape (dashed)."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    u = size / 48
    for k in range(0, 49, 4):
        d.line([(k * u, 0), (k * u, size)], fill=(120, 140, 170, 40))
        d.line([(0, k * u), (size, k * u)], fill=(120, 140, 170, 40))
    if ks and ks.get("bounds"):
        l, t, r, b = (v * u for v in ks["bounds"])
        if ks.get("r"):
            cx, cy, rr = (l + r) / 2, (t + b) / 2, ks["r"] * u
            d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=(232, 118, 12, 200), width=1)
        else:
            for x0, y0, x1, y1 in ((l, t, r, t), (r, t, r, b), (r, b, l, b), (l, b, l, t)):
                n = 24
                for k in range(0, n, 2):
                    d.line([(x0 + (x1 - x0) * k / n, y0 + (y1 - y0) * k / n),
                            (x0 + (x1 - x0) * (k + 1) / n, y0 + (y1 - y0) * (k + 1) / n)],
                           fill=(232, 118, 12, 200), width=1)
    return im


def ink(im):
    return im.convert("L").point(lambda v: 255 if v < 128 else 0)


def sym_score(im):
    """Ink IoU of a render with its left-right mirror."""
    a = ink(im)
    b = ImageOps.mirror(a)
    inter = ImageChops.multiply(a, b).histogram()[255]
    union = ImageChops.lighter(a, b).histogram()[255]
    return round(inter / union, 4) if union else 1.0


def new_asymmetry(inp, out):
    """Share of the output's ink that is lopsided where the input is not: the input's own lopsided ink
    (widened by ASYM_GROW) is allowed, anything beyond it was made by the processing."""
    def asym(im):
        a = ink(im)
        return ImageChops.difference(a, ImageOps.mirror(a))
    allowed = asym(inp).filter(ImageFilter.MaxFilter(ASYM_GROW))
    new = ImageChops.subtract(asym(out), allowed)
    total = ink(out).histogram()[255]
    return round(new.histogram()[255] / total, 4) if total else 0.0


def mirror_overlay(im):
    a, b = ink(im), ink(ImageOps.mirror(im))
    out = Image.new("RGB", im.size, "white")
    px, pa, pb = out.load(), a.load(), b.load()
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            ia, ib = pa[x, y], pb[x, y]
            if ia and ib:
                px[x, y] = (0, 0, 0)
            elif ia:
                px[x, y] = (220, 40, 40)
            elif ib:
                px[x, y] = (40, 90, 220)
    return out


def path_ds(svg_path):
    """{id or tag#n: d / geometry} of the drawing's shapes."""
    out = {}
    try:
        root = ET.parse(svg_path).getroot()
    except (ET.ParseError, FileNotFoundError):
        return out
    n = 0
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag not in SHAPES or (el.get("d") or "").startswith("M-16"):
            continue                                  # the sharp output's keyshape clip
        n += 1
        key = el.get("id") or f"{tag}#{n}"
        out[key] = el.get("d") or " ".join(f"{a}={el.get(a)}" for a in
                                            ("x", "y", "width", "height", "cx", "cy", "r", "rx", "ry",
                                             "x1", "y1", "x2", "y2", "points") if el.get(a) is not None)
    return out


def sheet(name, files, ks, path):
    big = {k: render(p, BIG) for k, p in files.items()}
    small = {k: render(p, SMALL) for k, p in files.items()}
    syms = {k: sym_score(im) for k, im in big.items()}
    symmetric = syms["input"] >= SYMMETRIC
    new = {k: new_asymmetry(big["input"], big[k]) for k in big if k != "input"} if symmetric else {}
    pad, head = 12, 22
    cols = list(files)
    rows = 3 if symmetric else 2
    W = pad + len(cols) * (BIG + pad)
    H = head + (BIG + head) + (SMALL + head) + ((BIG + head) if symmetric else 0) + pad
    im = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(im)
    d.text((pad, 4), name, fill=(0, 0, 0))
    g = guides(BIG, ks)
    y = head
    for i, k in enumerate(cols):
        x = pad + i * (BIG + pad)
        d.text((x, y), k, fill=(80, 80, 80))
        tile = big[k].convert("RGBA")
        tile.alpha_composite(g)
        im.paste(tile.convert("RGB"), (x, y + 14))
        d.rectangle([x - 1, y + 13, x + BIG, y + 14 + BIG], outline=(200, 200, 200))
    y += BIG + head
    for i, k in enumerate(cols):
        x = pad + i * (BIG + pad) + (BIG - SMALL) // 2
        d.text((pad + i * (BIG + pad), y), f"{k} · 48 px", fill=(80, 80, 80))
        im.paste(small[k], (x, y + 14))
    y += SMALL + head
    if symmetric:
        for i, k in enumerate(cols):
            x = pad + i * (BIG + pad)
            d.text((x, y), f"{k} vs mirror · {syms[k]:.3f}" + (f" · new {new[k]:.1%}" if k in new else ""),
                   fill=(200, 40, 40) if new.get(k, 0) > NEW_ASYM else (80, 80, 80))
            im.paste(mirror_overlay(big[k]), (x, y + 14))
    im.save(path)
    lost = [k for k, v in new.items() if v > NEW_ASYM]
    return {"input_symmetric": symmetric, "scores": syms, "new_asymmetry": new, "lost_in": lost}


def changed(log):
    """The corner log entries that say something (not the untouched sharp corners)."""
    keep = ("p", "angle", "r", "status", "why", "band", "was_round", "reduced", "by")
    return [{k: e[k] for k in keep if e.get(k) is not None} for e in log if e.get("status") != "kept sharp"]


def release(batch):
    with status_lock():
        s = load_status()
        n = 0
        for e in s["icons"]:
            if e["status"] == "reviewing" and (e.get("claim") or {}).get("batch") == batch:
                e["status"] = "todo"
                e.pop("claim", None)
                n += 1
        save_status(s)
    print(f"released {n} icons of {batch} back to todo")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Take the next icons to review and draw their review sheets.")
    ap.add_argument("--count", type=int, default=20)
    ap.add_argument("--offset", type=int, default=0, help="skip this many free icons first (in list order)")
    ap.add_argument("--flag", help="only icons with this flag (see status.json 'flags')")
    ap.add_argument("--icons", nargs="*", help="these icons (any status)")
    ap.add_argument("--reviewer", default=os.environ.get("CORNER_REVIEWER", "ai"), help="who claims the batch")
    ap.add_argument("--out-dir", default=os.path.join(ROOT, "outputs", "solo48"))
    ap.add_argument("--input", default=os.path.join(ROOT, "input", "solo48", "svg"))
    ap.add_argument("--release", metavar="BATCH", help="put a batch's unreviewed icons back to todo")
    cfg = ap.parse_args(argv)
    if cfg.release:
        return release(cfg.release)

    lock = status_lock().__enter__()                  # held until the claim is saved
    s = load_status()
    t = now()
    def left_for_human(e):
        return e["status"] == "needs-user" or (e["status"] == "proposed"
                                                and (e.get("decision") or {}).get("decision") == "report")

    def free(e):
        if e["status"] == "todo" or left_for_human(e):
            return True
        if e["status"] == "reviewing":
            at = (e.get("claim") or {}).get("at", "")
            try:
                when = datetime.datetime.strptime(at, "%Y-%m-%d %H:%M UTC").replace(tzinfo=datetime.timezone.utc)
            except ValueError:
                return True
            return (t - when).total_seconds() > CLAIM_HOURS * 3600
        return False
    if cfg.icons:
        want = set(cfg.icons) | {n + ".svg" for n in cfg.icons}
        picked = [e for e in s["icons"] if e["icon"] in want]
    else:
        pool = [e for e in s["icons"] if free(e) and (not cfg.flag or cfg.flag in e["flags"])]
        pool.sort(key=lambda e: not left_for_human(e))     # stable: earlier left-for-human icons first
        picked = pool[cfg.offset:cfg.offset + cfg.count]
    if not picked:
        lock.__exit__()
        print("nothing to review" + (f" with flag {cfg.flag}" if cfg.flag else ""))
        return 0

    os.makedirs(BATCHES, exist_ok=True)
    nums = [int(m.group(1)) for m in (re.match(r"batch-(\d+)$", n) for n in os.listdir(BATCHES)) if m]
    batch = f"batch-{max(nums, default=0) + 1:03d}"
    folder = os.path.join(BATCHES, batch)
    os.makedirs(folder)
    for e in picked:                                # claim first: a parallel reviewer skips them
        if e["status"] in ("todo", "reviewing") or left_for_human(e):
            e["status"] = "reviewing"
            e["claim"] = {"batch": batch, "by": cfg.reviewer, "at": stamp(t)}
    save_status(s)
    lock.__exit__()

    tog = json.load(open(os.path.join(cfg.out_dir, "toggle.json"), encoding="utf-8"))["icons"]
    kp = os.path.join(cfg.out_dir, "keyshapes.json")
    kss = json.load(open(kp, encoding="utf-8")) if os.path.exists(kp) else {}
    items = []
    for e in picked:
        name = e["icon"]
        files = {"input": os.path.join(cfg.input, name),
                 "round": os.path.join(cfg.out_dir, "round", name),
                 "sharp": os.path.join(cfg.out_dir, "sharp", name)}
        files = {k: p for k, p in files.items() if os.path.exists(p)}
        png = os.path.join(folder, name[:-4] + ".png")
        sym = sheet(name, files, kss.get(name), png) if "input" in files else None
        v = tog.get(name, {})
        items.append({
            "icon": name, "status": e["status"], "flags": e["flags"] + (["lost-symmetry"] if sym and sym["lost_in"] else []),
            "note": e.get("note", ""), "sheet": os.path.relpath(png, ROOT),
            "check": {m: (v.get(m, {}).get("check") or {}).get("status") for m in ("round", "sharp")},
            "round_log": changed(v.get("round", {}).get("log", [])),
            "sharp_log": changed(v.get("sharp", {}).get("log", [])),
            "shared_keep": v.get("shared_keep", []),
            "keyshape": {k: (kss.get(name) or {}).get(k) for k in ("keyshape", "bounds", "over")},
            "symmetry": sym,
            "paths": {k: path_ds(p) for k, p in files.items()},
        })
    with open(os.path.join(folder, "batch.json"), "w", encoding="utf-8") as f:
        json.dump({"batch": batch, "claimed_by": cfg.reviewer, "at": stamp(t), "icons": items}, f, indent=1,
                  ensure_ascii=False)
    left = sum(x["status"] == "todo" or left_for_human(x) for x in s["icons"])
    print(f"{batch}: {len(items)} icons -> {os.path.relpath(folder, ROOT)}/ ({left} todo left)")
    for it in items:
        print(f"  {it['icon']:<50} {' '.join(it['flags']) or '-'}")
    print(f"record each: python3 review/record.py {batch} ICON --status ok|proposed --note '...'")
    return 0


if __name__ == "__main__":
    sys.exit(main())
