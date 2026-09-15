"""Petrified Face; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f46d10c-0c4a-5930-a1a2-1a6d1851bf6f'
SOURCE_PATH = 'pictographic-primitives/smileys/petrified_7f46d10c-0c4a-5930-a1a2-1a6d1851bf6f.svg'
AUTHOR = 'gpt-6'


class PetrifiedFace(Solo48):
    icon_id = 'petrified-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('petrified', 'fear', 'shock', 'surprised', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: center (24,24), centerline radius20, visible radius22.
        axis,radius=24,20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        for side,x in (("left",16),("right",32)):
            self.add_line(f"eye-{side}",(x,16),(x,20))
        self.add_arc("mouth-top",(20,30),(28,30),radius_x=4,radius_y=5)
        self.add_arc("mouth-bottom",(28,30),(20,30),radius_x=4,radius_y=5)
        self.add_contour("mouth","mouth-top","mouth-bottom",closed=True)
