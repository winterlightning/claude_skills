"""A phone's dual rear camera: two round lenses side by side in a pill-shaped module.

Symbol plan: symmetric about x = 24 and y = 24. The module is a closed stadium, x 4..44,
y 10..38: straight top and bottom joined by r14 semicircular ends about (18, 24) and
(30, 24). The lenses are r3 rings (approved 6-diameter circles) at (16, 24) and (32, 24):
10 apart and 9 inside the module ends.
Lucide construction: 'rectangle-horizontal' rounded to a stadium with Lucide 'circle'
lenses, as in Lucide's camera modules.
Keyshape HRECT_M: centerline x 4..44, y 10..38.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7a9a0bfb-6240-535a-9ba2-c050f5e35304"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__dual-camera-module/20260926T055140Z-thuan-mac/reference/phone double camera_7a9a0bfb-6240-535a-9ba2-c050f5e35304.svg"
AUTHOR = "claude-opus-5-5"


class DualCameraModule(Solo48):
    icon_id = "dual-camera-module"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("phone double camera", "dual camera", "rear camera")
    keywords = ("camera", "phone", "dual", "lens", "smartphone", "module", "photo", "rear camera")

    def ring(self, name, cx, cy, r):
        pts = [(cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)]
        names = tuple(f"{name}-{q}" for q in ("nw", "ne", "se", "sw"))
        for i, n in enumerate(names):
            self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=r)
        self.add_contour(name, *names, closed=True)

    def build(self) -> None:
        t, b, lc, rc, r = 10, 38, 18, 30, 14
        self.add_line("module-top", (lc, t), (rc, t))
        self.add_arc("module-right", (rc, t), (rc, b), radius_x=r)
        self.add_line("module-bottom", (rc, b), (lc, b))
        self.add_arc("module-left", (lc, b), (lc, t), radius_x=r)
        self.add_contour("module", "module-top", "module-right", "module-bottom", "module-left", closed=True)
        self.ring("lens-left", 16, 24, 3)
        self.ring("lens-right", 32, 24, 3)
