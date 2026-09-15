"""Confused Face. Rebuilt from the supplied visual reference on SOLO48.
Lucide construction: face-angry / face-slightly-frowning circular face and sparse expression;
glasses uses paired circular lenses. Shared axis and paired geometry preserve expression.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23110766-a392-579a-844c-0825b0fac7bc'
SOURCE_PATH = 'pictographic-primitives/smileys/confuse_23110766-a392-579a-844c-0825b0fac7bc.svg'
AUTHOR = 'gpt-6'


class ConfusedFace(Solo48):
    icon_id = 'confused-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('confused', 'puzzled', 'frown', 'uncertain', 'face', 'emoji')

    def build(self) -> None:

        # Circle envelope: center (24,24), radius 20; extremes 4 and 44.
        axis, radius = 24, 20
        self.add_arc("head-top", (axis-radius,24), (axis+radius,24), radius_x=radius)
        self.add_arc("head-bottom", (axis+radius,24), (axis-radius,24), radius_x=radius)
        self.add_contour("head", "head-top", "head-bottom", closed=True)

        self.add_line("brow-left", (17,16),(20,14))
        self.add_line("brow-right", (28,15),(32,16))

        for side, x in (("left",16),("right",32)):
            self.add_dot(f"eye-{side}", (x,24))

        self.add_arc("mouth", (20,34), (28,34), radius_x=6)
