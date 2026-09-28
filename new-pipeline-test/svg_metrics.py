#!/usr/bin/env python3
"""Measure a traced *_raw.svg against the SOLO48 rules -> <slug>_metrics.json.

Pipeline position: image model PNG -> vectorize (png2svg) -> *_raw.svg ->
THIS SCRIPT -> /icon-solo agent reads the metrics and redraws the icon as a
Solo48 model, repairing every listed issue it can.

What it writes next to the raw SVG (or into --out-dir):
  <slug>_metrics.json   geometry, keyshape fit, junctions, clearances, holes, issues
  <slug>_fitted.svg     the trace uniformly scaled into the suggested keyshape,
                        stroke 4 -- what the icon looks like before any repair
  <slug>_fitted-48.png  native-size render of the fitted SVG

All coordinates in the JSON are 48-grid units. "source48" is the plain
1024 -> 48 scale; "fitted" is after the keyshape fit. Clearances are measured
on centerlines of the fitted geometry against the SOLO48 targets (8 between
separate parts, 6 inscribed for holes, exactly 8 for a detached human head).

Usage:
  /opt/homebrew/bin/python3 new-pipeline-test/svg_metrics.py <run>/<slug>_raw.svg
  ... --keyshape VRECT_L        # force a keyshape instead of the suggestion
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage
from scipy.spatial import cKDTree
from svgpathtools import Arc, CubicBezier, Line, Path as SvgPath, QuadraticBezier, parse_path

REPO = Path(__file__).resolve().parent.parent
SCHEMA = "pipeline-svg-metrics.v1"
CANVAS = 48
STROKE = 4
MIN_GAP = 8            # centerline gap between separate parts
MIN_HOLE = 6           # inscribed diameter of an enclosed hole
HEAD_GAP = 8           # detached human head outline -> body centerline, exact
MIN_JOIN_ANGLE = 35    # below this two joined strokes merge into a wedge blob
MAX_STROKES = 6        # prompt.md budget
SAMPLE_STEP = 0.2
JOIN_TOL = 1.5         # endpoint within this distance of another part = joined
RASTER = 10            # px per unit for hole measurement
HUMAN_RE = re.compile(
    r"\b(person|people|man|woman|men|women|child|kid|boy|girl|hiker|athlete|player|"
    r"swimm\w*|runner|walker|human|figure|user|worker|skier|climber|rider|dancer)\b", re.I)

FALLBACK_INK = {  # SOLO48 visible-ink bounds, used only if the model cannot be imported
    "CIRCLE": (2, 2, 46, 46), "SQUARE": (4, 4, 44, 44),
    "HRECT_L": (2, 6, 46, 42), "HRECT_M": (2, 8, 46, 40),
    "VRECT_L": (6, 2, 42, 46), "VRECT_M": (8, 2, 40, 46),
}
SHAPE_HINT = {"tall": ("VRECT_M", "VRECT_L"), "wide": ("HRECT_M", "HRECT_L"),
              "square": ("SQUARE",), "round": ("CIRCLE",)}


def keyshape_ink_bounds() -> dict[str, tuple[int, int, int, int]]:
    try:
        sys.path.insert(0, str(REPO))
        from icon_set.model.keyshapes import Keyshape
        from icon_set.model.profiles import Profile
        return {k: tuple(Keyshape[k].bounds_for(Profile.SOLO48)) for k in FALLBACK_INK}
    except Exception:
        return dict(FALLBACK_INK)


def r2(v: float) -> float:
    return round(float(v), 2)


def pt(z: complex) -> list[float]:
    return [r2(z.real), r2(z.imag)]


# ---------------------------------------------------------------- parsing

def load_elements(svg_path: Path) -> tuple[list[dict], float]:
    root = ET.parse(svg_path).getroot()
    vb = [float(v) for v in root.get("viewBox", "0 0 1024 1024").replace(",", " ").split()]
    size = max(vb[2], vb[3])
    elements = []
    for node in root.iter():
        tag = node.tag.split("}")[-1]
        if tag == "circle":
            cx, cy, r = (float(node.get(k)) for k in ("cx", "cy", "r"))
            path = SvgPath(Arc(complex(cx - r, cy), complex(r, r), 0, False, True, complex(cx + r, cy)),
                           Arc(complex(cx + r, cy), complex(r, r), 0, False, True, complex(cx - r, cy)))
            kind = "circle"
        elif tag == "path" and node.get("d"):
            path, kind = parse_path(node.get("d")), "path"
        else:
            continue
        if not len(path):
            continue
        elements.append({"id": f"e{len(elements)}", "kind": kind, "path": path,
                         "stroke_width": float(node.get("stroke-width", 0) or 0),
                         "closed": kind == "circle" or path.isclosed()})
    return elements, size


def transform(path: SvgPath, scale: float, offset: complex) -> SvgPath:
    return path.scaled(scale).translated(offset)


def describe_segments(path: SvgPath, grid: bool = False) -> list[dict]:
    snap = (lambda z: [round(z.real), round(z.imag)]) if grid else pt
    out = []
    for seg in path:
        if isinstance(seg, Line):
            out.append({"type": "line", "from": snap(seg.start), "to": snap(seg.end)})
        elif isinstance(seg, Arc):
            out.append({"type": "arc", "from": snap(seg.start), "to": snap(seg.end),
                        "center": pt(seg.center), "radius": [r2(seg.radius.real), r2(seg.radius.imag)],
                        "rotation": r2(seg.rotation), "large_arc": bool(seg.large_arc),
                        "sweep": bool(seg.sweep)})
        elif isinstance(seg, CubicBezier):
            out.append({"type": "cubic", "from": snap(seg.start), "c1": pt(seg.control1),
                        "c2": pt(seg.control2), "to": snap(seg.end)})
        elif isinstance(seg, QuadraticBezier):
            out.append({"type": "quad", "from": snap(seg.start), "c": pt(seg.control), "to": snap(seg.end)})
    return out


def corners(path: SvgPath, min_turn: float = 20.0) -> list[dict]:
    """Vertices inside one element where the direction turns by more than min_turn degrees."""
    out = []
    for a, b in zip(path, path[1:]):
        try:
            ta, tb = a.unit_tangent(1), b.unit_tangent(0)
        except Exception:
            continue
        turn = math.degrees(abs(np.angle(tb / ta)))
        if turn > min_turn:
            out.append({"at": pt(a.end), "turn_deg": r2(turn)})
    return out


def sample(path: SvgPath) -> np.ndarray:
    pts = []
    for seg in path:
        n = max(8, int(math.ceil(seg.length() / SAMPLE_STEP)))
        pts.extend(seg.point(t) for t in np.linspace(0, 1, n + 1))
    return np.array([[z.real, z.imag] for z in pts])


def bbox(paths) -> tuple[float, float, float, float]:
    boxes = [p.bbox() for p in paths]
    return (min(b[0] for b in boxes), min(b[2] for b in boxes),
            max(b[1] for b in boxes), max(b[3] for b in boxes))


# ---------------------------------------------------------------- keyshape fit

def keyshape_candidates(paths48: list[SvgPath], ink: dict, hint: str | None) -> list[dict]:
    x0, y0, x1, y1 = bbox(paths48)
    w, h = x1 - x0, y1 - y0
    center = complex((x0 + x1) / 2, (y0 + y1) / 2)
    pts = np.vstack([sample(p) for p in paths48])
    radial = float(np.max(np.hypot(pts[:, 0] - center.real, pts[:, 1] - center.imag)))
    hinted = SHAPE_HINT.get((hint or "").lower(), ())
    out = []
    for token, (ix0, iy0, ix1, iy1) in ink.items():
        cx0, cy0, cx1, cy1 = ix0 + 2, iy0 + 2, ix1 - 2, iy1 - 2   # centerline box
        bw, bh = cx1 - cx0, cy1 - cy0
        if token == "CIRCLE":
            s = (bw / 2) / radial
            fill_x = fill_y = min(w, h) * s / bw
            stretch = None
        else:
            s = min(bw / w, bh / h)
            fill_x, fill_y = w * s / bw, h * s / bh
            stretch = {"x": r2(bw / (w * s)), "y": r2(bh / (h * s))}
        out.append({"token": token, "ink_bounds": list(ink[token]),
                    "centerline_box": [cx0, cy0, cx1, cy1], "scale": round(s, 4),
                    "fill": {"x": r2(fill_x), "y": r2(fill_y)},
                    "stretch_for_exact_fit": stretch,
                    "matches_shape_hint": token in hinted,
                    "score": r2(min(fill_x, fill_y) + (0.25 if token in hinted else 0))})
    out.sort(key=lambda c: -c["score"])
    return out


# ---------------------------------------------------------------- relations

def endpoints(el: dict) -> list[complex]:
    return [] if el["closed"] else [el["fitted"].start, el["fitted"].end]


def directions_at(el: dict, at: np.ndarray, reach: float = 4.0) -> list[complex]:
    """Unit directions leaving point `at` along element el (one for an end, two mid-path)."""
    s = el["samples"]
    d = np.hypot(*(s - at).T)
    i = int(np.argmin(d))
    arc_len = np.concatenate([[0], np.cumsum(np.hypot(*np.diff(s, axis=0).T))])
    dirs = []
    for sign in (-1, 1):
        target = arc_len[i] + sign * reach
        if not (arc_len[0] <= target <= arc_len[-1]) and abs(arc_len[i] - (arc_len[0] if sign < 0 else arc_len[-1])) < 0.5:
            continue
        j = int(np.argmin(np.abs(arc_len - target)))
        v = complex(*(s[j] - s[i]))
        if abs(v) > 0.5:
            dirs.append(v / abs(v))
    return dirs


def find_junctions(els: list[dict]) -> list[dict]:
    junctions = []
    for a in els:
        for end in endpoints(a):
            p = np.array([end.real, end.imag])
            for b in els:
                if b is a:
                    continue
                d, _ = b["tree"].query(p)
                if d > JOIN_TOL:
                    continue
                at_end = any(abs(end - e) <= JOIN_TOL for e in endpoints(b))
                key = frozenset((a["id"], b["id"]))
                if any(j["_key"] == key and np.hypot(*(np.array(j["at"]) - p)) < 2 for j in junctions):
                    continue
                dirs = [("a", v) for v in directions_at(a, p)] + [("b", v) for v in directions_at(b, p)]
                angles = [math.degrees(abs(np.angle(v2 / v1)))
                          for i, (o1, v1) in enumerate(dirs) for o2, v2 in dirs[i + 1:] if o1 != o2]
                junctions.append({"_key": key, "elements": [a["id"], b["id"]], "at": pt(end),
                                  "kind": "shared-endpoint" if at_end else "t-junction",
                                  "gap": r2(d), "min_angle_deg": r2(min(angles)) if angles else None})
    return junctions


def pair_clearances(els: list[dict], junctions: list[dict]) -> list[dict]:
    out = []
    for i, a in enumerate(els):
        for b in els[i + 1:]:
            joins = [np.array(j["at"]) for j in junctions if j["_key"] == frozenset((a["id"], b["id"]))]
            sa, sb = a["samples"], b["samples"]
            if joins:   # ignore the stroke overlap around the shared joint itself
                keep = lambda s: np.all([np.hypot(*(s - j).T) > MIN_GAP for j in joins], axis=0)
                sa, sb = sa[keep(sa)], sb[keep(sb)]
                if not len(sa) or not len(sb):
                    continue
            d, idx = cKDTree(sb).query(sa)
            k = int(np.argmin(d))
            out.append({"elements": [a["id"], b["id"]], "connected": bool(joins),
                        "min_centerline_distance": r2(d[k]),
                        "min_ink_gap": r2(d[k] - STROKE),
                        "between": [pt(complex(*sa[k])), pt(complex(*sb[idx[k]]))],
                        "measured": "beyond 8 units of the shared joint" if joins else "whole parts",
                        "ok": bool(d[k] >= MIN_GAP - 1e-6)})
    return out


def head_check(els: list[dict]) -> list[dict]:
    out = []
    for head in (e for e in els if e["kind"] == "circle"):
        c = head["fitted"][0].center
        r = abs(head["fitted"][0].radius.real)
        best = None
        for other in els:
            if other is head:
                continue
            d = np.hypot(other["samples"][:, 0] - c.real, other["samples"][:, 1] - c.imag)
            k = int(np.argmin(d))
            if best is None or d[k] < best[0]:
                best = (float(d[k]), other["id"], other["samples"][k])
        if best:
            gap = best[0] - r
            out.append({"head": head["id"], "center": pt(c), "radius": r2(r),
                        "nearest_body_element": best[1], "nearest_body_point": pt(complex(*best[2])),
                        "outline_to_body_centerline": r2(gap), "target": HEAD_GAP,
                        "ink_gap": r2(gap - STROKE), "ok": abs(gap - HEAD_GAP) < 0.05})
    return out


# ---------------------------------------------------------------- raster checks

def fitted_svg(els: list[dict]) -> str:
    paths = "\n".join(f'  <path id="{e["id"]}" d="{e["fitted"].d()}"/>' for e in els)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS}" height="{CANVAS}" '
            f'viewBox="0 0 {CANVAS} {CANVAS}" fill="none" stroke="currentColor" '
            f'stroke-width="{STROKE}" stroke-linecap="round" stroke-linejoin="round">\n{paths}\n</svg>\n')


def render(svg_text: str, px: int, out: Path) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".svg", delete=False) as fh:
        fh.write(svg_text.replace("currentColor", "#000"))
    subprocess.run(["rsvg-convert", "-w", str(px), "-h", str(px), "-b", "white", fh.name, "-o", str(out)],
                   check=True)
    Path(fh.name).unlink()


def raster_metrics(svg_text: str) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        png = Path(tmp) / "r.png"
        render(svg_text, CANVAS * RASTER, png)
        ink = np.array(Image.open(png).convert("L")) < 128
    ys, xs = np.nonzero(ink)
    labels, n = ndimage.label(~ink)
    border = set(np.unique(np.concatenate([labels[0], labels[-1], labels[:, 0], labels[:, -1]])))
    holes = []
    for lab in range(1, n + 1):
        if lab in border:
            continue
        region = labels == lab
        area = region.sum() / RASTER ** 2
        if area < 0.5:
            continue
        edt = ndimage.distance_transform_edt(region)
        cy, cx = np.unravel_index(np.argmax(edt), edt.shape)
        diameter = 2 * edt.max() / RASTER
        holes.append({"inscribed_diameter": r2(diameter), "area": r2(area),
                      "center": [r2(cx / RASTER), r2(cy / RASTER)], "ok": bool(diameter >= MIN_HOLE - 0.2)})
    ink_labels, ink_parts = ndimage.label(ink)
    return {"ink_bounds": [r2(xs.min() / RASTER), r2(ys.min() / RASTER),
                           r2((xs.max() + 1) / RASTER), r2((ys.max() + 1) / RASTER)],
            "connected_ink_parts": int(ink_parts), "holes": holes}


# ---------------------------------------------------------------- main

def build(raw: Path, out_dir: Path, force_keyshape: str | None) -> tuple[dict, str]:
    slug = re.sub(r"(_final)?_raw$", "", raw.stem)
    choice_file = raw.parent / "choice.json"
    choice = json.loads(choice_file.read_text()) if choice_file.exists() else {}
    els, size = load_elements(raw)
    if not els:
        raise SystemExit(f"no <path> or <circle> in {raw}")
    s0 = CANVAS / size
    for e in els:
        e["p48"] = e["path"].scaled(s0)

    ink = keyshape_ink_bounds()
    cands = keyshape_candidates([e["p48"] for e in els], ink, choice.get("shape"))
    chosen = next(c for c in cands if c["token"] == force_keyshape) if force_keyshape else cands[0]
    x0, y0, x1, y1 = bbox([e["p48"] for e in els])
    s = chosen["scale"]
    bx0, by0, bx1, by1 = chosen["centerline_box"]
    offset = complex((bx0 + bx1) / 2 - s * (x0 + x1) / 2, (by0 + by1) / 2 - s * (y0 + y1) / 2)
    for e in els:
        e["fitted"] = transform(e["p48"], s, offset)
        e["samples"] = sample(e["fitted"])
        e["tree"] = cKDTree(e["samples"])

    junctions = find_junctions(els)
    clearances = pair_clearances(els, junctions)
    subject = choice.get("subject", slug.replace("-", " "))
    is_human = bool(HUMAN_RE.search(subject + " " + choice.get("parts", "")))
    heads = head_check(els) if is_human else []
    svg_text = fitted_svg(els)
    raster = raster_metrics(svg_text)
    fx0, fy0, fx1, fy1 = bbox([e["fitted"] for e in els])

    issues = []
    def issue(sev, code, msg, **kw):
        issues.append({"severity": sev, "code": code, "message": msg, **kw})

    src_sw = max((e["stroke_width"] for e in els), default=0) * s0
    if src_sw and abs(src_sw * s - STROKE) > 0.5:
        issue("info", "stroke-width", f"trace stroke is {r2(src_sw * s)} after fitting, target {STROKE}: "
              "every gap shrinks when redrawn at stroke 4", source_stroke_on_48=r2(src_sw), fitted=r2(src_sw * s))
    if len(els) > MAX_STROKES:
        issue("warn", "stroke-count", f"{len(els)} strokes, prompt budget {MAX_STROKES}")
    if chosen["stretch_for_exact_fit"]:
        for axis, k in chosen["stretch_for_exact_fit"].items():
            if k > 1.001:
                issue("warn", "keyshape-short-axis",
                      f"{chosen['token']} needs every extreme on its box (tolerance 0); the {axis} axis only "
                      f"fills {chosen['fill'][axis]:.0%}: widen parts or stretch by {k} on {axis}",
                      axis=axis, stretch=k)
    for c in clearances:
        if not c["ok"]:
            issue("error", "clearance", f"{c['elements'][0]} and {c['elements'][1]} are "
                  f"{c['min_centerline_distance']} apart on centerlines (need {MIN_GAP})",
                  elements=c["elements"], at=c["between"])
    for j in junctions:
        if j["min_angle_deg"] is not None and j["min_angle_deg"] < MIN_JOIN_ANGLE:
            issue("warn", "narrow-join", f"{j['elements'][0]} meets {j['elements'][1]} at "
                  f"{j['min_angle_deg']} deg: the strokes fuse into a wedge", elements=j["elements"], at=j["at"])
        if j["gap"] > 0.3:
            issue("info", "loose-join", f"{j['elements'][0]} ends {j['gap']} short of {j['elements'][1]}: "
                  "share the exact endpoint and relate('connect')", elements=j["elements"], at=j["at"])
    for h in raster["holes"]:
        if not h["ok"]:
            issue("error", "hole", f"enclosed hole at {h['center']} is {h['inscribed_diameter']} wide "
                  f"(need {MIN_HOLE} inscribed)", at=h["center"])
    for hd in heads:
        if not hd["ok"]:
            issue("error", "head-gap", f"head {hd['head']} outline is {hd['outline_to_body_centerline']} from "
                  f"{hd['nearest_body_element']} (need exactly {HEAD_GAP}: 4-unit ink gap, head centred on "
                  "the upper torso axis)", elements=[hd["head"], hd["nearest_body_element"]],
                  at=hd["nearest_body_point"])
    if is_human and not heads:
        issue("warn", "no-head", "human subject but no circle traced as the head")

    return {
        "schema": SCHEMA,
        "created_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "slug": slug,
        "subject": subject,
        "choice": choice or None,
        "files": {"raw_svg": raw.name, "fitted_svg": f"{slug}_fitted.svg",
                  "fitted_png_48": f"{slug}_fitted-48.png",
                  "reference_png": next((p.name for p in (raw.parent / f"{slug}.png",) if p.exists()), None)},
        "target": {"family": "solo", "profile": "SOLO48", "canvas": CANVAS, "stroke_width": STROKE,
                   "min_centerline_gap": MIN_GAP, "min_hole_inscribed": MIN_HOLE,
                   "human_head_gap_centerline": HEAD_GAP, "max_strokes": MAX_STROKES},
        "source": {"viewbox_size": size, "scale_to_48": s0, "element_count": len(els),
                   "stroke_width_on_48": r2(src_sw),
                   "centerline_bounds_48": [r2(x0), r2(y0), r2(x1), r2(y1)],
                   "size_48": [r2(x1 - x0), r2(y1 - y0)], "aspect_w_over_h": r2((x1 - x0) / (y1 - y0))},
        "keyshape": {"suggested": chosen["token"], "forced": bool(force_keyshape),
                     "shape_hint": choice.get("shape"), "candidates": cands},
        "fit": {"keyshape": chosen["token"], "scale_from_48": s, "offset": pt(offset),
                "source_to_fitted": {"scale": round(s0 * s, 6), "dx": r2(offset.real), "dy": r2(offset.imag)},
                "centerline_bounds": [r2(fx0), r2(fy0), r2(fx1), r2(fy1)],
                "raster": raster},
        "elements": [{
            "id": e["id"], "kind": e["kind"], "closed": e["closed"],
            "length": r2(e["fitted"].length()),
            "bounds": [r2(v) for v in (lambda b: (b[0], b[2], b[1], b[3]))(e["fitted"].bbox())],
            "segments": describe_segments(e["fitted"]),
            "grid_endpoints": describe_segments(e["fitted"], grid=True),
            "corners": corners(e["fitted"]),
            "source48_segments": describe_segments(e["p48"]),
        } for e in els],
        "junctions": [{k: v for k, v in j.items() if k != "_key"} for j in junctions],
        "clearances": clearances,
        "human": {"detected": is_human, "heads": heads},
        "issues": issues,
        "summary": {"errors": sum(i["severity"] == "error" for i in issues),
                    "warnings": sum(i["severity"] == "warn" for i in issues),
                    "infos": sum(i["severity"] == "info" for i in issues)},
    }, svg_text


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("raw_svg", type=Path)
    ap.add_argument("--out-dir", type=Path)
    ap.add_argument("--keyshape", choices=sorted(FALLBACK_INK))
    args = ap.parse_args()
    raw = args.raw_svg.resolve()
    out_dir = (args.out_dir or raw.parent).resolve()
    metrics, svg_text = build(raw, out_dir, args.keyshape)
    slug = metrics["slug"]
    (out_dir / f"{slug}_fitted.svg").write_text(svg_text)
    render(svg_text, CANVAS, out_dir / f"{slug}_fitted-48.png")
    out = out_dir / f"{slug}_metrics.json"
    out.write_text(json.dumps(metrics, indent=2, default=lambda o: o.item() if hasattr(o, "item") else str(o)) + "\n")
    s = metrics["summary"]
    print(f"{out}  keyshape={metrics['keyshape']['suggested']}  "
          f"errors={s['errors']} warnings={s['warnings']} infos={s['infos']}")
    for i in metrics["issues"]:
        print(f"  [{i['severity']}] {i['code']}: {i['message']}")


if __name__ == "__main__":
    main()
