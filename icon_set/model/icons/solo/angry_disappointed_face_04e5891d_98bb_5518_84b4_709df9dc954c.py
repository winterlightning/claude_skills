"""Angry Face. Rebuilt from the supplied visual reference on SOLO48.
Lucide construction: face-angry / face-slightly-frowning circular face and sparse expression;
glasses uses paired circular lenses. Shared axis and paired geometry preserve expression.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04e5891d-98bb-5518-84b4-709df9dc954c'
SOURCE_PATH = 'pictographic-primitives/smileys/disapointed mad_04e5891d-98bb-5518-84b4-709df9dc954c.svg'
AUTHOR = 'gpt-6'


class AngryDisappointedFace(Solo48):
    icon_id = 'angry-disappointed-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('angry', 'scowl', 'frown', 'disappointed', 'face', 'emoji')

    def build(self) -> None:

        # Circle envelope: center (24,24), radius 20; extremes 4 and 44.
        axis, radius = 24, 20
        self.add_arc("head-top", (axis-radius,24), (axis+radius,24), radius_x=radius)
        self.add_arc("head-bottom", (axis+radius,24), (axis-radius,24), radius_x=radius)
        self.add_contour("head", "head-top", "head-bottom", closed=True)

        for side, sign in (("left",1),("right",-1)):
            self.add_line(f"brow-{side}", (24+sign*(17-24),16), (24+sign*(20-24),17))

        for side, x in (("left",16),("right",32)):
            self.add_dot(f"eye-{side}", (x,25))

        self.add_arc("mouth", (18,34), (30,34), radius_x=13)
