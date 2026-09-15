"""Smiling Face with Side Tongue; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd331b73b-057f-59d7-923b-6ed15186434b'
SOURCE_PATH = 'pictographic-primitives/smileys/tongue_d331b73b-057f-59d7-923b-6ed15186434b.svg'
AUTHOR = 'gpt-6'


class SmilingFaceWithSideTongue(Solo48):
    icon_id = 'smiling-face-with-side-tongue'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('tongue', 'smiling', 'playful', 'silly', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: visible radius22; shared center (24,24), centerline radius20.
        axis,radius=24,20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        for side,x in (("left",17),("right",31)):
            self.add_arc(f"eye-{side}",(x-2,17),(x+2,17),radius_x=2)
        self.add_arc("smile-left",(14,26),(23,28),radius_x=10,sweep=False)
        self.add_line("tongue-left",(23,28),(23,30))
        self.add_arc("tongue-tip",(23,30),(31,30),radius_x=4,sweep=False)
        self.add_line("tongue-right",(31,30),(31,26))
        self.add_contour("mouth","smile-left","tongue-left","tongue-tip","tongue-right")
