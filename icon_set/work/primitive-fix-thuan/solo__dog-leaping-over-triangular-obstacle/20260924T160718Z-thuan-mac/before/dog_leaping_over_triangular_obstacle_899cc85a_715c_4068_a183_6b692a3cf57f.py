"""A right-facing dog stretches over a triangular agility obstacle.
HRECT_L (4,8)-(44,40). Source supplies airborne stance and triangle.
Lucide dog supplied continuous head outline; anatomy reduced to an open spine
and single-stroke legs because doubled limbs would close at 48. Tail is curved.
Shared spine nodes own legs and neck; no face details or duplicate far legs.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID="899cc85a-715c-4068-a183-6b692a3cf57f"
SOURCE_PATH="pictographic-primitives/_uncategorized_15/dog race compettion 2_899cc85a-715c-4068-a183-6b692a3cf57f.svg"
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id="dog-leaping-over-triangular-obstacle"
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="Uncategorized"
    aliases=("Dog Jumping Over Obstacle",)
    keywords=("dog","jumping","obstacle","agility","animal","leap","training")
    def build(self):
        self.add_bezier("tail",(4,8),((4,14),(8,16),(14,16)))
        self.add_line("back",(14,16),(30,16))
        self.add_polyline("head",(30,16),(32,8),(38,8),(44,12),(44,16))
        self.add_polyline("front-leg",(30,16),(34,24),(44,26))
        self.add_polyline("hind-leg",(14,16),(10,24),(4,26))
        for a,b in (("tail","back"),("tail","hind-leg"),("back","hind-leg"),("back","head"),("back","front-leg"),("head","front-leg")):
            self.relate("connect",a,b)
        self.add_polyline("obstacle",(16,40),(24,30),(32,40),closed=True)
