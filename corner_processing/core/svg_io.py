"""core/svg_io.py — read the stroked geometry of a 48x48 icon SVG.

The corner tools only look at STROKED elements (the centerlines of the icon):
  <path> <line> <polyline> <polygon> <rect> (incl. rx/ry)  -> svgpathtools Path
  <circle> <ellipse>                                        -> yielded, but never have corners
Fill-only elements (a white background <rect>, arrowheads drawn as filled outlines) are
skipped. A stroke can be set by attribute, inline style or a <style> .class rule, and is
inherited from parent groups / the root <svg>. A <g id="skeleton-shapes"> container is used
when present, and a <g id="background-grid"> is always ignored.
"""

import os
import re

from svgpathtools import Arc, Line, Path, parse_path

from .paths import DEFAULT_INPUT   # noqa: E402,F401  (re-exported)


def localname(tag):
    return tag.split("}")[-1] if "}" in tag else tag


_TOKEN = re.compile(r"[MmLlHhVvCcSsQqTtAaZz]|[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?")
_ARGS = {"M": 2, "L": 2, "H": 1, "V": 1, "C": 6, "S": 4, "Q": 4, "T": 2, "A": 7, "Z": 0}


def drop_null_arcs(d):
    """Path data without arcs whose end point is their start point. The SVG spec says such an
    arc is omitted; svgpathtools refuses the whole path (an icon drawn ...L44 40A1 1 0 0 1 44 40
    would be left out of every corner step). Other commands are kept as written."""
    toks = _TOKEN.findall(d)
    out, i, cmd = [], 0, None
    cur = start = 0j
    while i < len(toks):
        if toks[i].isalpha():
            cmd = toks[i]
            i += 1
            if cmd in "Zz":
                out.append(cmd)
                cur = start
                continue
        if cmd is None:
            return d
        n = _ARGS[cmd.upper()]
        args = toks[i:i + n]
        if len(args) < n:
            return d
        i += n
        v = [float(a) for a in args]
        rel = cmd.islower()
        up = cmd.upper()
        if up == "H":
            end = complex(v[0] + (cur.real if rel else 0), cur.imag)
        elif up == "V":
            end = complex(cur.real, v[0] + (cur.imag if rel else 0))
        else:
            end = complex(v[-2], v[-1]) + (cur if rel else 0)
        if up == "A" and abs(end - cur) < 1e-9:
            continue                                  # null arc: drawn as nothing
        out.append(cmd + " " + " ".join(args))
        if up == "M":
            start = end
            cmd = "l" if rel else "L"                 # implicit lineto after a moveto
        cur = end
    return " ".join(out)


def element_to_path(elem):
    """Convert a skeleton shape element to an svgpathtools Path, or None if it has no corners."""
    name = localname(elem.tag)
    if name == "path":
        d = elem.get("d")
        if not d:
            return None
        try:
            return parse_path(d)
        except Exception:
            try:
                return parse_path(drop_null_arcs(d))
            except Exception:
                return None
    if name in ("line",):
        try:
            x1, y1 = float(elem.get("x1")), float(elem.get("y1"))
            x2, y2 = float(elem.get("x2")), float(elem.get("y2"))
        except (TypeError, ValueError):
            return None
        return Path(Line(complex(x1, y1), complex(x2, y2)))
    if name in ("polyline", "polygon"):
        raw = (elem.get("points") or "").replace(",", " ").split()
        try:
            nums = [float(x) for x in raw]
        except ValueError:
            return None
        pts = [complex(nums[i], nums[i + 1]) for i in range(0, len(nums) - 1, 2)]
        if len(pts) < 2:
            return None
        segs = [Line(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
        if name == "polygon":
            segs.append(Line(pts[-1], pts[0]))
        return Path(*segs)
    if name == "rect":
        # the 48 set draws some frames as <rect x y width height rx ry>
        try:
            x, y = float(elem.get("x") or 0), float(elem.get("y") or 0)
            w, h = float(elem.get("width")), float(elem.get("height"))
        except (TypeError, ValueError):
            return None
        if w <= 0 or h <= 0:
            return None
        rx, ry = elem.get("rx"), elem.get("ry")
        rx = float(rx) if rx not in (None, "auto") else None
        ry = float(ry) if ry not in (None, "auto") else None
        rx = ry if rx is None else rx
        ry = rx if ry is None else ry
        rx, ry = min(rx or 0.0, w / 2), min(ry or 0.0, h / 2)
        if rx <= 0 or ry <= 0:
            c = [complex(x, y), complex(x + w, y), complex(x + w, y + h), complex(x, y + h)]
            return Path(*[Line(c[i], c[(i + 1) % 4]) for i in range(4)])
        r = complex(rx, ry)
        p = [complex(x + rx, y), complex(x + w - rx, y), complex(x + w, y + ry),
             complex(x + w, y + h - ry), complex(x + w - rx, y + h), complex(x + rx, y + h),
             complex(x, y + h - ry), complex(x, y + ry)]
        segs = []
        for i in range(0, 8, 2):
            if abs(p[i + 1] - p[i]) > 1e-9:
                segs.append(Line(p[i], p[i + 1]))
            segs.append(Arc(p[i + 1], r, 0.0, False, True, p[(i + 2) % 8]))
        return Path(*segs)
    # circle / ellipse -> closed smooth loop -> no corners
    return None


def iter_skeleton_shapes(root):
    """Yield shape elements to analyse, always skipping the background-grid group."""
    shape_tags = ("path", "line", "circle", "ellipse", "polyline", "polygon", "rect")
    skeleton = grid = None
    for el in root.iter():
        if el.get("id") == "skeleton-shapes":
            skeleton = el
        elif el.get("id") == "background-grid":
            grid = el
    excluded = set()
    if grid is not None:
        for el in grid.iter():
            excluded.add(id(el))
    container = skeleton if skeleton is not None else root

    # Only STROKED elements are centerlines. The 48 set mixes in fill-only outlines
    # (arrowheads drawn as filled shapes, a white <rect> background) that would otherwise
    # read as strokes. Effective stroke follows SVG inheritance: element attr / inline
    # style / .class rule, else the parent's (the root usually sets stroke="currentColor").
    css = {}
    for el in root.iter():
        if localname(el.tag) == "style" and el.text:
            for cls, body in _CSS_RULE.findall(el.text):
                for kv in body.split(";"):
                    k, _, v = kv.partition(":")
                    if k.strip() == "stroke":
                        css[cls] = v.strip()

    def own_stroke(el):
        m = _STYLE_STROKE.search(el.get("style") or "")
        if m:
            return m.group(1).strip()
        if el.get("stroke") is not None:
            return el.get("stroke").strip()
        for cls in (el.get("class") or "").split():
            if cls in css:
                return css[cls]
        return None

    inherited = None
    for anc in _path_to(root, container):
        inherited = own_stroke(anc) or inherited

    def walk(el, stroke):
        for ch in el:
            if id(ch) in excluded or localname(ch.tag) in _NON_RENDERED:
                continue
            s = own_stroke(ch) or stroke
            if localname(ch.tag) in shape_tags:
                if s is not None and s != "none":
                    yield ch
            else:
                yield from walk(ch, s)

    yield from walk(container, inherited)


_CSS_RULE = re.compile(r"\.([\w-]+)\s*\{([^}]*)\}")
_STYLE_STROKE = re.compile(r"(?:^|;)\s*stroke\s*:\s*([^;]+)")
_NON_RENDERED = ("defs", "symbol", "clipPath", "mask", "marker", "pattern", "style", "title")


def _path_to(root, target):
    """Elements from root down to target (inclusive), or [root] if target is not found."""
    def dfs(el, trail):
        if el is target:
            return trail + [el]
        for ch in el:
            r = dfs(ch, trail + [el])
            if r:
                return r
        return None
    return dfs(root, []) or [root]
