"""Crestfallen Face. Rebuilt from the supplied visual reference on SOLO48.
Lucide construction: face-angry / face-slightly-frowning circular face and sparse expression;
glasses uses paired circular lenses. Shared axis and paired geometry preserve expression.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '080cff4d-c989-5eb7-8be2-3824af3b4722'
SOURCE_PATH = 'pictographic-primitives/smileys/crying_080cff4d-c989-5eb7-8be2-3824af3b4722.svg'
AUTHOR = 'gpt-6'


class CrestfallenFace(Solo48):
    icon_id = 'crestfallen-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('crestfallen', 'sad', 'crying', 'disappointed', 'face', 'emoji')

    def build(self) -> None:

        # Circle envelope: center (24,24), radius 20; extremes 4 and 44.
        axis, radius = 24, 20
        self.add_arc("head-top", (axis-radius,24), (axis+radius,24), radius_x=radius)
        self.add_arc("head-bottom", (axis+radius,24), (axis-radius,24), radius_x=radius)
        self.add_contour("head", "head-top", "head-bottom", closed=True)

        for side, sign in (("left",1),("right",-1)):
            self.add_line(f"brow-{side}", (24+sign*(18-24),15), (24+sign*(20-24),14))

        for side, sign in (("left",1),("right",-1)):
            self.add_arc(f"eye-{side}", (24+sign*(15-24),24),(24+sign*(19-24),24),radius_x=4,sweep=sign<0)

        self.add_arc("mouth", (18,34), (30,34), radius_x=11)
