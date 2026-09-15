"""Unimpressed Face. Rebuilt from the supplied visual reference on SOLO48.
Lucide construction: face-angry / face-slightly-frowning circular face and sparse expression;
glasses uses paired circular lenses. Shared axis and paired geometry preserve expression.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e923b8b8-9be0-59a8-a652-99ec014352c3'
SOURCE_PATH = 'pictographic-primitives/smileys/disapointed_e923b8b8-9be0-59a8-a652-99ec014352c3.svg'
AUTHOR = 'gpt-6'


class UnimpressedFace(Solo48):
    icon_id = 'unimpressed-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('unimpressed', 'disappointed', 'frown', 'stern', 'face', 'emoji')

    def build(self) -> None:

        # Circle envelope: center (24,24), radius 20; extremes 4 and 44.
        axis, radius = 24, 20
        self.add_arc("head-top", (axis-radius,24), (axis+radius,24), radius_x=radius)
        self.add_arc("head-bottom", (axis+radius,24), (axis-radius,24), radius_x=radius)
        self.add_contour("head", "head-top", "head-bottom", closed=True)

        for side, sign in (("left",1),("right",-1)):
            self.add_line(f"brow-{side}", (24+sign*(17-24),15), (24+sign*(20-24),15))

        for side, x in (("left",16),("right",32)):
            self.add_dot(f"eye-{side}", (x,23))

        self.add_arc("mouth", (18,34), (30,34), radius_x=13)
