#!/usr/bin/env python3
"""core/fetch.py — the approved icons of one family (solo 48 or icon-72), fetched again from the review Worker.

Pages through /api/icons (family solo or icon-72, status approve), downloads each icon's current SVG
(the built drawing, or the edited / uploaded artwork the reviewers picked) and copies its Python
model from the local claude_skills checkout when it is there (solo only: icon-72 icons are uploads). The set is downloaded into a temp
folder first and only then replaces svg/ and model/, so a failed fetch leaves the old set alone.

  python3 -m core.fetch                       # -> input/solo48/{svg,model,icons.csv,...}
  python3 -m core.fetch --family icon-72      # -> input/icon72/
  python3 -m core.fetch --api https://pictographic-review.pictographic.workers.dev

icons.csv columns: key, icon_id, approved_by, file, model, svg_matches_model, keyshape,
artwork_source (svg_matches_model = the SVG is the model's build, not edited / uploaded artwork).
"""

import argparse
import csv
import json
import os

import numpy as np
import shutil
import sys
import tempfile
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import xml.etree.ElementTree as ET

from svgpathtools import Arc, Path
from svgpathtools.parser import parse_transform
from svgpathtools.path import transform as transform_path

from .svg_io import DEFAULT_INPUT, element_to_path, localname

API = "https://pictographic-review-next.pictographic.workers.dev"
from .paths import FIXES_DIR, INPUT_DIR, SETS, SKILLS
PAGE = 192             # the Worker's largest page size


def get(url, tries=4):
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "corner48-fetch/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:   # Cloudflare 403s urllib's own UA
                return r.read()
        except Exception:                            # noqa: BLE001 — retry, then give up
            if k == tries - 1:
                raise


def approved(api, family="solo"):
    """Every approved icon of the family, once. Reviews change while the list is paged (an icon approved or
    disapproved meanwhile shifts the pages: one page repeats an icon, the next skips one), so the list is read
    again until it holds as many icons as the Worker says there are (at most three passes)."""
    found, total = {}, None
    for _ in range(3):
        items, total = _approved_pass(api, family)
        found.update((item["key"], item) for item in items)
        if len(found) >= total:
            break
    return list(found.values())


def _approved_pass(api, family):
    items, offset = [], 0
    while True:
        q = urllib.parse.urlencode({"family": family, "status": "approve", "limit": PAGE,
                                    "offset": offset, "sort": "name"})
        d = json.loads(get(f"{api}/api/icons?{q}"))
        items += d["items"]
        offset += PAGE
        print(f"  listed {len(items)}/{d['total']}", end="\r", flush=True)
        if offset >= d["total"] or not d["items"]:
            print()
            return items, d["total"]


def svg_url(api, item):
    # preview_url is relative to the gallery page (/gallery/...): "../solo48/x.svg" -> /solo48/x.svg
    return urllib.parse.urljoin(f"{api}/gallery/", item["preview_url"])


FIXES = os.path.join(FIXES_DIR, "applied_in_source.json")
SVG_NS = "http://www.w3.org/2000/svg"
SHAPES = ("path", "rect", "line", "polyline", "polygon", "circle", "ellipse")
GEOM = ("d", "x", "y", "width", "height", "rx", "ry", "cx", "cy", "r", "x1", "y1", "x2", "y2",
        "points", "transform")


def _shape_path(el):
    """Any shape element as an svgpathtools Path (circles / ellipses as two half arcs)."""
    if localname(el.tag) in ("circle", "ellipse"):
        r0 = float(el.get("r") or 0)
        cx, cy = float(el.get("cx", 0)), float(el.get("cy", 0))
        rx, ry = float(el.get("rx") or r0), float(el.get("ry") or r0)
        a, b = complex(cx + rx, cy), complex(cx - rx, cy)
        return Path(Arc(a, complex(rx, ry), 0, False, True, b), Arc(b, complex(rx, ry), 0, False, True, a))
    return element_to_path(el)


def bake_transforms(svg_dir):
    """Apply every transform= to the geometry it moves (the corner tools read coordinates
    as drawn: a rect drawn with rotate(45) would come out unrotated, off the canvas). Each
    transformed shape becomes a plain <path>; ids and stroke attributes are kept. -> files done"""
    ET.register_namespace("", SVG_NS)
    done = 0
    for name in sorted(os.listdir(svg_dir)):
        path = os.path.join(svg_dir, name)
        if not name.endswith(".svg"):
            continue
        with open(path, encoding="utf-8") as f:
            if "transform=" not in f.read():
                continue
        tree = ET.parse(path)
        root = tree.getroot()

        def walk(el, m):
            if el.get("transform"):
                m = m @ parse_transform(el.get("transform"))
                del el.attrib["transform"]
            for k, ch in enumerate(list(el)):
                if localname(ch.tag) in SHAPES and (ch.get("transform") or not (m == np.eye(3)).all()):
                    mm = m @ parse_transform(ch.get("transform")) if ch.get("transform") else m
                    p = _shape_path(ch)
                    if p is None:
                        continue
                    new = ET.Element(f"{{{SVG_NS}}}path", {a: v for a, v in ch.attrib.items() if a not in GEOM})
                    new.set("d", transform_path(p, mm).d())
                    new.tail = ch.tail
                    el.remove(ch)
                    el.insert(k, new)
                else:
                    walk(ch, m)

        walk(root, np.eye(3))
        tree.write(path, encoding="unicode")
        done += 1
        print(f"  transform baked: {name}")
    return done


def reapply_source_fixes(svg_dir, fixes=FIXES):
    """Redraws applied by hand to the local source SVGs (input_fixes/applied_in_source.json) that
    the Worker does not have yet: put back every path still drawn the old way. -> count applied"""
    if not os.path.exists(fixes):
        return 0
    with open(fixes, encoding="utf-8") as f:
        table = json.load(f)
    n = 0
    for v in table.values():
        path = os.path.join(svg_dir, v["file"])
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as f:
            s = f.read()
        done = []
        for pid, c in v["changed_paths"].items():
            old, new = f'id="{pid}" d="{c["old"]}"', f'id="{pid}" d="{c["new"]}"'
            if old in s:
                s = s.replace(old, new)
                done.append(pid)
        if done:
            with open(path, "w", encoding="utf-8") as f:
                f.write(s)
            n += 1
            print(f"  source fix put back: {v['file']} ({', '.join(done)})")
    return n


def main(argv=None):
    ap = argparse.ArgumentParser(description="Fetch the approved icons of one family from the review Worker.")
    ap.add_argument("--api", default=API)
    ap.add_argument("--family", choices=sorted(SETS), default="solo")
    ap.add_argument("--dest", help="set folder holding svg/ and model/ (default: input/solo48 or input/icon72)")
    ap.add_argument("--skills", default=SKILLS)
    ap.add_argument("--jobs", type=int, default=16)
    cfg = ap.parse_args(argv)
    cfg.dest = cfg.dest or os.path.join(INPUT_DIR, SETS[cfg.family])
    os.makedirs(cfg.dest, exist_ok=True)

    items = approved(cfg.api, cfg.family)
    tmp = tempfile.mkdtemp(prefix="approved-", dir=cfg.dest)
    os.makedirs(os.path.join(tmp, "svg")), os.makedirs(os.path.join(tmp, "model"))

    def one(item):
        name = item["key"].split("/", 1)[1]
        try:
            data = get(svg_url(cfg.api, item))
            if not data.lstrip().startswith(b"<svg"):
                raise ValueError("not an SVG")
            with open(os.path.join(tmp, "svg", name + ".svg"), "wb") as f:
                f.write(data)
        except Exception as e:                       # noqa: BLE001
            return item, name, None, f"{type(e).__name__}: {e}"[:200]
        model = None
        src = (item.get("python_source") or {}).get("path")
        if cfg.family == "solo" and src and os.path.exists(os.path.join(cfg.skills, src)):
            model = "model/" + os.path.basename(src)
            shutil.copyfile(os.path.join(cfg.skills, src), os.path.join(tmp, model))
        return item, name, model, None

    rows, failed, no_model = [], [], []
    with ThreadPoolExecutor(cfg.jobs) as ex:
        for k, (item, name, model, err) in enumerate(ex.map(one, items), 1):
            print(f"  fetched {k}/{len(items)}", end="\r", flush=True)
            if err:
                failed.append(f"{item['key']}\t{err}")
                continue
            if not model:
                src = (item.get("python_source") or {}).get("path")
                no_model.append(f"{item['key']}\t" + ("model not in local claude_skills: " + src if src
                                                      else "uploaded SVG, no Python model"))
            rows.append({"key": item["key"], "icon_id": item["icon_id"], "svg_sha256": item.get("svg_sha256") or "",
                         "approved_by": (item.get("review") or {}).get("by") or "",
                         "file": f"svg/{name}.svg", "model": model or "",
                         "svg_matches_model": "yes" if model and not item.get("artwork_source") else "no",
                         "keyshape": item.get("keyshape") or "",
                         "artwork_source": item.get("artwork_source") or "build"})
    print()
    with open(os.path.join(tmp, "icons.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: r["key"]))
    for fname, lines in (("failed.txt", failed), ("no-model.txt", no_model)):
        with open(os.path.join(tmp, fname), "w", encoding="utf-8") as f:
            f.write("".join(line + "\n" for line in sorted(lines)))

    reapply_source_fixes(os.path.join(tmp, "svg"))
    bake_transforms(os.path.join(tmp, "svg"))
    for part in ("svg", "model", "icons.csv", "failed.txt", "no-model.txt"):
        dst = os.path.join(cfg.dest, part)
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        elif os.path.exists(dst):
            os.remove(dst)
        os.rename(os.path.join(tmp, part), dst)
    shutil.rmtree(tmp, ignore_errors=True)       # only Finder litter (.DS_Store) is left
    print(f"{len(rows)} approved icons -> {cfg.dest}/svg | {len(rows) - len(no_model)} with a model, "
          f"{len(no_model)} without | {len(failed)} failed")
    for line in failed[:10]:
        print("  FAILED", line)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
