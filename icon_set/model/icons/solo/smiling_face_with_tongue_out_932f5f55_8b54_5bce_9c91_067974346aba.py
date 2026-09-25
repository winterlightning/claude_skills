"""Smiling Face with Tongue Out; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '932f5f55-8b54-5bce-9c91-067974346aba'
SOURCE_PATH = 'pictographic-primitives/smileys/tongue sticking_932f5f55-8b54-5bce-9c91-067974346aba.svg'
AUTHOR = 'gpt-6'


class SmilingFaceWithTongueOut(Solo48):
    icon_id = 'smiling-face-with-tongue-out'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
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
        self.add_arc("smile-left",(14,25),(20,26),radius_x=10,sweep=False)
        self.add_line("tongue-left",(20,26),(20,31))
        self.add_arc("tongue-tip",(20,31),(28,31),radius_x=4,sweep=False)
        self.add_line("tongue-right",(28,31),(28,26))
        self.add_arc("smile-right",(28,26),(34,25),radius_x=10,sweep=False)
        self.add_contour("mouth","smile-left","tongue-left","tongue-tip","tongue-right","smile-right")
