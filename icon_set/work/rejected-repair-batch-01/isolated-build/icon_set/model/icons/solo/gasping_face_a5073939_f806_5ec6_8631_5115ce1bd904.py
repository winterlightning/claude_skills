"""Shocked Face; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a5073939-f806-5ec6-8631-5115ce1bd904'
SOURCE_PATH = 'pictographic-primitives/smileys/shocked_a5073939-f806-5ec6-8631-5115ce1bd904.svg'
AUTHOR = 'gpt-6'


class GaspingFace(Solo48):
    icon_id = 'gasping-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('shocked', 'surprised', 'astonished', 'gasp', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: visible radius22; shared center (24,24), centerline radius20.
        axis,radius=24,20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        for side,x in (("left",17),("right",31)):
            self.add_arc(f"eye-{side}-top",(x-2,18),(x+2,18),radius_x=2)
            self.add_arc(f"eye-{side}-bottom",(x+2,18),(x-2,18),radius_x=2)
            self.add_contour(f"eye-{side}",f"eye-{side}-top",f"eye-{side}-bottom",closed=True)
        self.add_arc("mouth-top",(20,31),(28,31),radius_x=4,radius_y=4)
        self.add_arc("mouth-bottom",(28,31),(20,31),radius_x=4,radius_y=4)
        self.add_contour("mouth","mouth-top","mouth-bottom",closed=True)
