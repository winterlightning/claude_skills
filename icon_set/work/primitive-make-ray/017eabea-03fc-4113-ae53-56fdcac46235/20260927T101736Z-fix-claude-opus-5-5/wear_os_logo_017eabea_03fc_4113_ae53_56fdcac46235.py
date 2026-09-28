"""Wear OS logo: two parallel slanted bars followed by a large ring over a smaller ring.

Plan: HRECT_L centerline box (4,8)-(44,40). Both bars share one vector (10,32) and a
horizontal pitch of 10 (9.5 perpendicular). The capsule outlines of the reference are
reduced to single strokes (an outlined capsule needs a 10-wide band per bar, which the
width budget cannot hold). Rings: upper r6 at (38,14) reaches the right extreme; lower r5
sits below and slightly left, 8 clear of the upper ring and of the second bar. r5 is the
smallest ring that keeps a 6-unit hole, which repairs the pinhole of the rejected drawing.
No useful Lucide match; circle construction as Lucide `circle`.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "017eabea-03fc-4113-ae53-56fdcac46235"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__wear-os-logo/20260927T101553Z-thuan-mac-1/reference/wear os logo_017eabea-03fc-4113-ae53-56fdcac46235.svg"
AUTHOR = "claude-opus-5-5"


class WearOsLogo(Solo48):
    icon_id = "wear-os-logo"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ("wear-os", "google", "smartwatch", "wearable", "logo", "brand", "android")

    def build(self) -> None:
        dx, dy, pitch = 10, 32, 10
        for i in range(2):
            x = 4 + i * pitch
            self.add_line(f"bar-{i}", (x, 8), (x + dx, 8 + dy))

        def ring(name, cx, cy, r):
            self.add_arc(f"{name}-upper", (cx - r, cy), (cx + r, cy), radius_x=r)
            self.add_arc(f"{name}-lower", (cx + r, cy), (cx - r, cy), radius_x=r)
            self.add_contour(name, f"{name}-upper", f"{name}-lower", closed=True)

        ring("ring-large", 38, 14, 6)
        ring("ring-small", 36, 33, 5)
