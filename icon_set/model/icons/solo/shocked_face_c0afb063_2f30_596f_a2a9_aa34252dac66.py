"""Shocked Face; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c0afb063-2f30-596f-a2a9-aa34252dac66'
SOURCE_PATH = 'pictographic-primitives/smileys/shock_c0afb063-2f30-596f-a2a9-aa34252dac66.svg'
AUTHOR = 'gpt-6'


class ShockedFace(Solo48):
    icon_id = 'shocked-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('shocked', 'surprised', 'astonished', 'gasp', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: visible radius22; shared center (24,24), centerline radius20.
        axis,radius=24,20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        for side,x in (("left",16),("right",32)):
            self.add_arc(f"eye-{side}-top",(x-3,20),(x+3,20),radius_x=3)
            self.add_arc(f"eye-{side}-bottom",(x+3,20),(x-3,20),radius_x=3)
            self.add_contour(f"eye-{side}",f"eye-{side}-top",f"eye-{side}-bottom",closed=True)
        self.add_arc("mouth-top",(21,32),(27,32),radius_x=3)
        self.add_arc("mouth-bottom",(27,32),(21,32),radius_x=3)
        self.add_contour("mouth","mouth-top","mouth-bottom",closed=True)
