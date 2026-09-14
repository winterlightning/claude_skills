"""Smiling Face with Tongue Out; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5547be6c-0538-593b-ae62-248e923cebef'
SOURCE_PATH = 'pictographic-primitives/smileys/tongue_5547be6c-0538-593b-ae62-248e923cebef.svg'
AUTHOR = 'gpt-6'


class WideTongueSmilingFace(Solo48):
    icon_id = 'wide-tongue-smiling-face'
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
        self.add_arc("smile-left",(14,25),(19,26),radius_x=10,sweep=False)
        self.add_line("tongue-left",(19,26),(19,29))
        self.add_arc("tongue-tip",(19,29),(29,29),radius_x=5,sweep=False)
        self.add_line("tongue-right",(29,29),(29,26))
        self.add_arc("smile-right",(29,26),(34,25),radius_x=10,sweep=False)
        self.add_contour("mouth","smile-left","tongue-left","tongue-tip","tongue-right","smile-right")
