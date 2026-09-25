"""Devastated Face. Rebuilt from the supplied visual reference on SOLO48.
Lucide construction: face-angry / face-slightly-frowning circular face and sparse expression;
glasses uses paired circular lenses. Shared axis and paired geometry preserve expression.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f67b2ad-3544-5f9c-bf54-d05ccd9ed99b'
SOURCE_PATH = 'pictographic-primitives/smileys/devastated_8f67b2ad-3544-5f9c-bf54-d05ccd9ed99b.svg'
AUTHOR = 'gpt-6'


class DevastatedFace(Solo48):
    icon_id = 'devastated-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    aliases = ()
    keywords = ('devastated', 'distressed', 'wailing', 'sad', 'face', 'emoji')

    def build(self) -> None:

        # Circle envelope: center (24,24), radius 20; extremes 4 and 44.
        axis, radius = 24, 20
        self.add_arc("head-top", (axis-radius,24), (axis+radius,24), radius_x=radius)
        self.add_arc("head-bottom", (axis+radius,24), (axis-radius,24), radius_x=radius)
        self.add_contour("head", "head-top", "head-bottom", closed=True)

        for side, sign in (("left",1),("right",-1)):
            self.add_line(f"brow-{side}", (24+sign*(17-24),16), (24+sign*(20-24),14))

        # Raised brows carry the worried expression; omit tiny vertical pupils to open the wail.
        self.add_arc("mouth-top",(17,32),(31,32),radius_x=7,radius_y=7)
        self.add_arc("mouth-bottom",(31,32),(17,32),radius_x=7,radius_y=2)
        self.add_contour("mouth","mouth-top","mouth-bottom",closed=True)
