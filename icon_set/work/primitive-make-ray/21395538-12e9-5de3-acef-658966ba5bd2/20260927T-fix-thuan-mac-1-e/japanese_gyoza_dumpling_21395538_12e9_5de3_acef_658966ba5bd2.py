"""Japanese gyoza dumpling with a fan of pleats.

Symbol plan: a wide, low front dome (base 10..38 at y=35, shallow belly
to y=38, dome-top nodes (10,28) (18,19) (30,19) (38,28) joined by r20
arcs) with five pleat lobes fanned around it: left, upper-left, top,
upper-right and right. Each lobe is one cubic from notch to notch whose
two controls sit at equal offsets along the outward normal, so its apex
lands exactly on the keyshape edge (x=4, y=10, x=44). Each pleat reads
as its own crimped fold between the dome and the lobe.
Mirror-symmetric about x=24.
Revision: the rejected drawing was a flat oval with a dome and three
spokes (read as a bun); the reference is a low crescent with rounded
pleats fanned behind the front dome.
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "21395538-12e9-5de3-acef-658966ba5bd2"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__japanese-gyoza-dumpling/20260927T153253Z-thuan-mac-1/reference/gyoza grill deep fried dumpling_21395538-12e9-5de3-acef-658966ba5bd2.svg"
AUTHOR = "claude-opus-5-5"

NODES = ((10, 35), (10, 28), (18, 19), (30, 19), (38, 28), (38, 35))
# (outward bulge at the lobe middle, tangential spread of the controls)
LOBES = ((6, 1.5), (8.5, 2.5), (9, 2.5), (8.5, 2.5), (6, 1.5))


def _lobe(p, q, bulge, spread):
    dx, dy = q[0] - p[0], q[1] - p[1]
    length = math.hypot(dx, dy)
    tx, ty = dx / length, dy / length
    nx, ny = ty, -tx  # outward (left of travel, clockwise outline)
    k = bulge / 0.75
    c1 = (p[0] + nx * k - tx * spread, p[1] + ny * k - ty * spread)
    c2 = (q[0] + nx * k + tx * spread, q[1] + ny * k + ty * spread)
    return tuple(round(v, 4) for v in c1), tuple(round(v, 4) for v in c2)


class JapaneseGyozaDumpling(Solo48):
    icon_id = "japanese-gyoza-dumpling"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ("gyoza", "potsticker", "dumpling")
    keywords = ("gyoza", "dumpling", "potsticker", "japanese", "fried", "food")

    def build(self) -> None:
        lobes = []
        for i, (bulge, spread) in enumerate(LOBES):
            c1, c2 = _lobe(NODES[i], NODES[i + 1], bulge, spread)
            self.add_bezier(f"pleat-{i}", NODES[i], (c1, c2, NODES[i + 1]))
            lobes.append(f"pleat-{i}")
        belly_c = 35 + 3 / 0.75
        self.add_bezier("belly", NODES[5], ((32, belly_c), (16, belly_c), NODES[0]))
        self.add_contour("outline", *lobes, "belly", closed=True)

        self.add_line("dome-left", NODES[0], NODES[1])
        for i, radius in ((1, 20), (2, 20), (3, 20)):
            self.add_arc(f"dome-{i}", NODES[i], NODES[i + 1], radius_x=radius, sweep=True)
        self.add_line("dome-right", NODES[4], NODES[5])
        self.add_contour("dome", "dome-left", "dome-1", "dome-2", "dome-3", "dome-right")
        self.relate("connect", "outline", "dome")
