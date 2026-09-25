"""Angry Face. Rebuilt from the supplied visual reference on SOLO48.
Lucide construction: face-angry / face-slightly-frowning circular face and sparse expression;
glasses uses paired circular lenses. Shared axis and paired geometry preserve expression.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95bc8a10-0aff-51c3-93b1-993f1c2d28f9'
SOURCE_PATH = 'pictographic-primitives/smileys/angry_95bc8a10-0aff-51c3-93b1-993f1c2d28f9.svg'
AUTHOR = 'gpt-6'


class AngryFace(Solo48):
    icon_id = 'angry-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('angry', 'scowl', 'frown', 'rage', 'face', 'emoji')

    def build(self) -> None:

        # Circle envelope: center (24,24), radius 20; extremes 4 and 44.
        axis, radius = 24, 20
        self.add_arc("head-top", (axis-radius,24), (axis+radius,24), radius_x=radius)
        self.add_arc("head-bottom", (axis+radius,24), (axis-radius,24), radius_x=radius)
        self.add_contour("head", "head-top", "head-bottom", closed=True)

        for side, sign in (("left",1),("right",-1)):
            self.add_line(f"brow-{side}", (24+sign*(17-24),15), (24+sign*(20-24),17))

        for side, x in (("left",16),("right",32)):
            self.add_dot(f"eye-{side}", (x,25))

        self.add_arc("mouth", (18,34), (30,34), radius_x=11)
