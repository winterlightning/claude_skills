from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c5fb655-5227-5b55-b446-6c49a2774cc8'
SOURCE_PATH = 'pictographic-primitives/shipping/crack_8c5fb655-5227-5b55-b446-6c49a2774cc8.svg'
AUTHOR = 'gpt-6-astra'


class CrackedParcel(Solo48):
    icon_id = 'cracked-parcel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shipping"
    categories = ("primitives", "shipping")
    aliases = ()
    keywords = ('parcel', 'box', 'crack', 'damage', 'shipping', 'broken')

    def build(self) -> None:
        # Square centerline extremes (6,6)-(42,42); matching corner radii 4.
        self.add_polyline("top", (10,6), (24, 6), (38,6))
        self.add_arc("tr", (38,6), (42,10), radius_x=4)
        self.add_line("right", (42,10), (42,38))
        self.add_arc("br", (42,38), (38,42), radius_x=4)
        self.add_line("bottom", (38,42), (10,42))
        self.add_arc("bl", (10,42), (6,38), radius_x=4)
        self.add_line("left", (6,38), (6,10))
        self.add_arc("tl", (6,10), (10,6), radius_x=4)
        
        self.add_contour("sides", "tr", "right", "br", "bottom", "bl", "left", "tl")
        self.relate("connect", "top", "sides")
        self.add_polyline("fracture", (24,6), (24,11), (17,19), (27,25), (22,32))
        self.relate("connect", "top", "fracture")
