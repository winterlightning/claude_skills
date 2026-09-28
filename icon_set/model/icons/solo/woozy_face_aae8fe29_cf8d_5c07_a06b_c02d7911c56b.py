"""Woozy Face; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aae8fe29-cf8d-5c07-a06b-c02d7911c56b'
SOURCE_PATH = 'pictographic-primitives/smileys/woozy face_aae8fe29-cf8d-5c07-a06b-c02d7911c56b.svg'
AUTHOR = 'gpt-6'


class WoozyFace(Solo48):
    icon_id = 'woozy-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('woozy', 'dizzy', 'ill', 'unwell', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: visible radius22; shared center (24,24), centerline radius20.
        axis,radius=24,20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        self.add_arc("eye-left",(15,17),(19,18),radius_x=4,sweep=False)
        self.add_arc("eye-right",(29,17),(33,18),radius_x=4,sweep=False)
        self.add_arc("mouth-top",(19,30),(29,30),radius_x=5,radius_y=4)
        for i,(a,b) in enumerate(zip(((29,30),(28,34),(24,33),(20,34)),((28,34),(24,33),(20,34),(19,30))),1):self.add_line(f"mouth-bottom-{i}",a,b)
        self.add_contour("mouth","mouth-top","mouth-bottom-1","mouth-bottom-2","mouth-bottom-3","mouth-bottom-4",closed=True)
