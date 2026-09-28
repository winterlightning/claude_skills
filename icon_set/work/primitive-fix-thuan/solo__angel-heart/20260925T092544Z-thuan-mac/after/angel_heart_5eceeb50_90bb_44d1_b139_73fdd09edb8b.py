"""Angel heart ("love it angel"): a heart as the angel's body, a halo ellipse
above it and two arms hanging from its sides.

Symbol plan: heart mirrored about x=24 (lobe tops, dip, widest points, tip);
each arm leaves the heart's widest point at a right angle (T-junction on a
heart knot, declared connection) and drops to the base; the halo is a closed
ellipse centred on the axis with an 8-unit gap above the lobes.
Keyshape SQUARE: arms x=6/42, halo top y=6, heart tip and arm ends y=42.
Lucide construction: heart (two lobes flowing into a pointed tip) and a
flattened circle for the halo.
Revision of the rejected drawing ("Bad stroke drawn"): the old drawing hung
two pill loops against the heart; here the arms grow from the heart cleanly.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5eceeb50-90bb-44d1-b139-73fdd09edb8b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__angel-heart/20260925T092544Z-thuan-mac/reference/love it angel_5eceeb50-90bb-44d1-b139-73fdd09edb8b.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
HALO = (24, 10)
HALO_RX, HALO_RY = 8, 4


def m(point):
    return (2 * AXIS - point[0], point[1])


class AngelHeart(Solo48):
    icon_id = "angel-heart"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("love-it-angel", "heart-angel")
    keywords = ("angel", "heart", "love", "halo", "like", "favorite")

    def path(self, name, start, steps, closed=False):
        members = []
        for index, (c1, c2, end) in enumerate(steps):
            tag = f"{name}-{index + 1}"
            self.add_bezier(tag, start, (c1, c2, end))
            start = end
            members.append(tag)
        self.add_contour(name, *members, closed=closed)

    def build(self) -> None:
        left = [
            ((22, 23.5), (21, 23), (19, 23)),     # dip to left lobe top
            ((16, 23), (14, 25), (14, 28)),       # lobe to widest point
            ((14, 33), (19, 37), (AXIS, 42)),     # side into the tip
        ]
        # right side runs tip -> widest -> lobe top -> dip, mirrored from the left
        right = [
            (m((19, 37)), m((14, 33)), m((14, 28))),
            (m((14, 25)), m((16, 23)), m((19, 23))),
            (m((21, 23)), m((22, 23.5)), (AXIS, 26)),
        ]
        self.path("heart", (AXIS, 26), left + right, closed=True)

        for name, f in (("left", lambda p: p), ("right", m)):
            self.add_bezier(f"arm-{name}-shoulder", f((14, 28)), (f((10, 28)), f((6, 30)), f((6, 34))))
            self.add_line(f"arm-{name}-hang", f((6, 34)), f((6, 42)))
            self.add_contour(f"arm-{name}", f"arm-{name}-shoulder", f"arm-{name}-hang")
            self.relate("connect", "heart", f"arm-{name}")

        hx, hy = HALO
        self.add_arc("halo-top", (hx - HALO_RX, hy), (hx + HALO_RX, hy), radius_x=HALO_RX, radius_y=HALO_RY)
        self.add_arc("halo-bottom", (hx + HALO_RX, hy), (hx - HALO_RX, hy), radius_x=HALO_RX, radius_y=HALO_RY)
        self.add_contour("halo", "halo-top", "halo-bottom", closed=True)
