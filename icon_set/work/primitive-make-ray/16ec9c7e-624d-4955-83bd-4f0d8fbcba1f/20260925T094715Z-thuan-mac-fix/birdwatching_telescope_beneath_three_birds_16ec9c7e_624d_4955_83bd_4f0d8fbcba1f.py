"""Birdwatching: a telescope on a tripod, tilted up to the right, beneath
three small birds in flight.

Symbol plan: the tube is a rectangle on the integer axis (2,-1) with the
perpendicular (-1,-2)*4 (width 8.9); the eyepiece continues the axis from
the midpoint of the tube's rear end; the tripod apex is a point on the tube's
lower edge, with three legs to the ground spaced 8 apart. The three birds
repeat one 8-wide "v" definition; the middle bird flies highest.
Keyshape SQUARE: eyepiece x=6, right bird x=42, birds y=6, legs y=42.
Lucide construction: telescope (tilted tube + tripod legs) and bird "v" marks.
Revision of the rejected drawing ("Bad stroke drawn"): the old drawing used
heart shapes for birds and a segmented tube; here the birds are chevrons and
the tube is one clean rectangle.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "16ec9c7e-624d-4955-83bd-4f0d8fbcba1f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__birdwatching-telescope-beneath-three-birds/20260925T092544Z-thuan-mac/reference/bird watching 2_16ec9c7e-624d-4955-83bd-4f0d8fbcba1f.svg"
AUTHOR = "claude-opus-5-5"

AXIS = (2, -1)          # tube direction, up to the right
NORMAL = (-4, -8)       # tube width vector (perpendicular to AXIS)
REAR_LOW = (14, 34)     # rear lower corner of the tube
LENGTH = 8              # tube length in AXIS steps
APEX_STEP = 5           # tripod apex position along the lower edge
GROUND = 42
BIRDS = ((10, 12), (24, 6), (38, 12))   # (centre x, wing-tip y); middle bird flies highest
BIRD_HALF, BIRD_DIP = 4, 3


def add(p, v, k=1):
    return (p[0] + k * v[0], p[1] + k * v[1])


class BirdwatchingTelescopeBeneathThreeBirds(Solo48):
    icon_id = "birdwatching-telescope-beneath-three-birds"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("bird-watching", "birdwatching")
    keywords = ("bird", "watching", "telescope", "tripod", "birds", "nature", "observe")

    def build(self) -> None:
        low_rear = REAR_LOW
        low_front = add(low_rear, AXIS, LENGTH)
        up_front = add(low_front, NORMAL)
        up_rear = add(low_rear, NORMAL)
        self.add_polyline("tube", low_rear, low_front, up_front, up_rear, closed=True)

        rear_mid = add(low_rear, (NORMAL[0] // 2, NORMAL[1] // 2))
        self.add_line("eyepiece", rear_mid, add(rear_mid, AXIS, -3))
        self.relate("connect", "tube", "eyepiece")

        apex = add(low_rear, AXIS, APEX_STEP)
        for name, dx in (("left", -4), ("middle", 4), ("right", 12)):
            self.add_line(f"leg-{name}", apex, (apex[0] + dx, GROUND))
            self.relate("connect", "tube", f"leg-{name}")
        self.relate("connect", "leg-left", "leg-middle", "leg-right")

        for index, (x, y) in enumerate(BIRDS, 1):
            self.add_polyline(f"bird-{index}", (x - BIRD_HALF, y), (x, y + BIRD_DIP), (x + BIRD_HALF, y))
