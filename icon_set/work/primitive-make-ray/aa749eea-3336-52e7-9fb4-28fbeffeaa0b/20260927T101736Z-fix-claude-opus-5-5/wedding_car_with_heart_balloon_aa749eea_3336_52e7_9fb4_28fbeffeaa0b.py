"""Wedding car with a heart balloon: a right-facing rounded sedan with a heart-shaped
balloon tied to its rear deck by a wavy string.

Plan: SQUARE centerline box (6,6)-(42,42). Balloon: Lucide `heart` construction, 12 wide
(6..18), mirrored about x=12, notch (12,8), tip (12,17), in the upper-left corner. Its string
waves down to the rear deck corner. Car: stands on its wheel-centre line y=38 like Lucide
`car` - body ends and the sill meet the r4 wheel rings at their side points; rear deck and
hood at y=26 (8 above the wheel tops), arched cabin with a rounded roof at y=16.
Omitted: the reference's heart decal on the cabin (no band inside the cabin clears a heart
by 8 from the roof, pillars and wheels) and the speed lines under the car.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "aa749eea-3336-52e7-9fb4-28fbeffeaa0b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__wedding-car-with-heart-balloon/20260927T101553Z-thuan-mac-1/reference/wedding car heart balloon_aa749eea-3336-52e7-9fb4-28fbeffeaa0b.svg"
AUTHOR = "claude-opus-5-5"


class WeddingCarWithHeartBalloon(Solo48):
    icon_id = "wedding-car-with-heart-balloon"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "romance"
    categories = ("primitives", "romance")
    aliases = ()
    keywords = ("car", "wedding", "balloon", "heart", "vehicle", "celebration", "just-married")

    def build(self) -> None:
        # Heart balloon, mirrored about x = ax.
        ax, tip = 12, (12, 17)

        def m(p):
            return (2 * ax - p[0], p[1])

        right = [(ax, 8), ((13, 7), (14, 6), (15, 6)), ((17, 6), (18, 7), (18, 9)),
                 ((18, 11), (17, 12), (16, 13))]
        self.add_bezier("balloon-right-top", right[0], *right[1:])
        self.add_line("balloon-right-edge", (16, 13), tip)
        self.add_line("balloon-left-edge", tip, m((16, 13)))
        left = [m((16, 13)), (m((17, 12)), m((18, 11)), m((18, 9))),
                (m((18, 7)), m((17, 6)), m((15, 6))), (m((14, 6)), m((13, 7)), (ax, 8))]
        self.add_bezier("balloon-left-top", left[0], *left[1:])
        self.add_contour("balloon", "balloon-right-top", "balloon-right-edge",
                         "balloon-left-edge", "balloon-left-top", closed=True)

        deck_y = 26
        deck = (11, deck_y)
        self.add_bezier("string", tip, ((14, 20), (10, 21), (11, 23)), ((12, 24), (11, 25), deck))

        # Car body: rear wheel side -> rear -> deck -> cabin -> hood -> nose -> front wheel side.
        wheel_y, r = 38, 4
        rear_x, front_x = 13, 35
        self.add_bezier("body-rear", (rear_x - r, wheel_y), ((7, wheel_y), (6, 37), (6, 35)),
                        ((6, 33), (6, 32), (6, 31)), ((6, 28), (8, deck_y), deck))
        self.add_bezier("body-top", deck, ((14, deck_y), (20, deck_y), (20, deck_y)),
                        ((21, 20), (23, 16), (27, 16)), ((29, 16), (30, 16), (30, 16)),
                        ((33, 16), (35, 20), (36, deck_y)), ((38, deck_y), (38, deck_y), (38, deck_y)),
                        ((40, deck_y), (42, 28), (42, 31)),
                        ((42, 34), (42, 37), (front_x + r, wheel_y)))
        self.add_contour("body", "body-rear", "body-top")
        self.add_line("sill", (rear_x + r, wheel_y), (front_x - r, wheel_y))

        def ring(name, cx, cy):
            self.add_arc(f"{name}-upper", (cx - r, cy), (cx + r, cy), radius_x=r)
            self.add_arc(f"{name}-lower", (cx + r, cy), (cx - r, cy), radius_x=r)
            self.add_contour(name, f"{name}-upper", f"{name}-lower", closed=True)

        ring("rear-wheel", rear_x, wheel_y)
        ring("front-wheel", front_x, wheel_y)

        self.relate("connect", "string", "balloon-right-edge")
        self.relate("connect", "string", "balloon-left-edge")
        self.relate("connect", "string", "body-rear")
        self.relate("connect", "string", "body-top")
        for part in ("body-rear", "sill"):
            self.relate("connect", part, "rear-wheel-upper")
            self.relate("connect", part, "rear-wheel-lower")
        for part in ("body-top", "sill"):
            self.relate("connect", part, "front-wheel-upper")
            self.relate("connect", part, "front-wheel-lower")
