"""What the review pages share: the output folder they read by default, and an icon's filled shapes.

Whole-set runs write to outputs/solo48/ (README), partial runs to outputs/: a page built without
--dir reads whichever of the two was run last.
"""

import os
import re

from core.paths import OUT_DIR
from core.svg_io import localname
from core.toggle import filled_shapes

WHITE = re.compile(r"^(#fff(fff)?|white)$", re.I)


def default_dir():
    runs = [d for d in (os.path.join(OUT_DIR, "solo48"), OUT_DIR)
            if os.path.exists(os.path.join(d, "toggle.json"))]
    return max(runs, key=lambda d: os.path.getmtime(os.path.join(d, "toggle.json"))) if runs else OUT_DIR


def filled_markup(root, centerlines, geom_attrs, skip=()):
    """The drawing's filled shapes (a window dot, an arrowhead, a white backdrop) as SVG strings,
    painted with the page's ink or panel colour so they follow the theme. core/toggle.py copies
    them into both outputs (a sharp output's dots become squares); iter_skeleton_shapes leaves them out."""
    out = []
    for el in filled_shapes(root, centerlines):
        if el in skip:
            continue
        m = re.search(r"fill\s*:\s*([^;]+)", el.get("style") or "")
        fill = (m.group(1) if m else el.get("fill") or "").strip()
        paint = "var(--panel)" if WHITE.match(fill) else "var(--ink)"
        attrs = " ".join(f'{a}="{el.get(a)}"' for a in geom_attrs if el.get(a) is not None)
        out.append(f'<{localname(el.tag)} {attrs} style="fill:{paint};stroke:none"/>')
    return out
