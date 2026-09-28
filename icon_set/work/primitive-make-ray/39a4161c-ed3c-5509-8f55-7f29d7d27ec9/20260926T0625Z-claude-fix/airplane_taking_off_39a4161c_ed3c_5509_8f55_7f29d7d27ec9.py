"""Airplane taking off: an airliner in side view climbing to the upper right above a
ground line, with a triangular far wing on top, a near wing sweeping down and back
under the body, and a tail that curves smoothly underneath.

Symbol plan: one closed airframe outline plus the ground. The body top and belly
are parallel straight runs of direction (12,-5), 10 apart vertically (9.2
perpendicular), with lattice nodes at x = 12, 24, 36. The nose is two cubics: the
top one has equal end heights and equal control heights, so its highest point is
exactly y=6; it turns down the right edge and back into the belly tangentially.
The far wing is a triangle on the body top (roots (24,12) and (12,17), tip
(6,9), swept back). The near wing hangs from the belly between (24,22) and (12,27), its tip
edge 11 above the ground. The tail tip sits at the left edge and the underside
returns to the belly in one tangent cubic.
Deliberate asymmetry: a directional side view.
Revision (reviewer: triangular upper wing, lower wing sweeping downward, tail
curving smoothly underneath): the rejected drawing had a line wing and a zigzag
tail.
Lucide construction: 'plane-takeoff' - climbing airliner over a ground line.
Keyshape SQUARE: centerline x 6 (tail tip) .. 42 (nose), y 6 (nose) .. 42 (ground).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "39a4161c-ed3c-5509-8f55-7f29d7d27ec9"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__airplane-taking-off/20260926T061914Z-thuan-mac/reference/plane take off_39a4161c-ed3c-5509-8f55-7f29d7d27ec9.svg"
AUTHOR = "claude-opus-5-5"


class AirplaneTakingOff(Solo48):
    icon_id = "airplane-taking-off"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/air"
    aliases = ("plane-take-off", "departure")
    keywords = ("airplane", "takeoff", "departure", "flight", "airport", "travel", "plane")

    def segments(self, name: str, *points: tuple[int, int]) -> list[str]:
        names = []
        for i, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(f"{name}-{i}", a, b)
            names.append(f"{name}-{i}")
        return names

    def build(self) -> None:
        s = 4 / 15  # control step along (12,-5): equal control heights 7-5s put the extreme at 6
        self.add_bezier("nose-top", (36, 7), ((36 + 12 * s, 7 - 5 * s), (42, 7 - 5 * s), (42, 7)))
        self.add_bezier("nose-chin", (42, 7), ((42, 12), (39, 15.75), (36, 17)))
        belly = self.segments("belly", (36, 17), (24, 22))
        near_wing = self.segments("near-wing", (24, 22), (19, 31), (13, 31), (12, 27))
        self.add_bezier("tail-under", (12, 27), ((9, 28.25), (6, 23), (6, 20)))
        top = self.segments("top", (6, 20), (12, 17), (6, 9), (24, 12), (36, 7))
        self.add_contour("airframe", "nose-top", "nose-chin", *belly, *near_wing, "tail-under",
                         *top, closed=True)
        self.add_line("ground", (8, 42), (36, 42))
