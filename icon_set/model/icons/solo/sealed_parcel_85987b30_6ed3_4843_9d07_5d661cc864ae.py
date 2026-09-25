from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85987b30-6ed3-4843-9d07-5d661cc864ae'
SOURCE_PATH = 'pictographic-primitives/shipping/box_85987b30-6ed3-4843-9d07-5d661cc864ae.svg'
AUTHOR = 'gpt-6-astra'


class SealedParcel(Solo48):
    icon_id = 'sealed-parcel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shipping"
    aliases = ()
    keywords = ('parcel', 'box', 'package', 'shipping', 'tape', 'delivery')

    def build(self) -> None:
        # Square centerline extremes (6,6)-(42,42); matching corner radii 4.
        self.add_polyline("top", (10,6), (16, 6), (32, 6), (38,6))
        self.add_arc("tr", (38,6), (42,10), radius_x=4)
        self.add_line("right", (42,10), (42,38))
        self.add_arc("br", (42,38), (38,42), radius_x=4)
        self.add_line("bottom", (38,42), (10,42))
        self.add_arc("bl", (10,42), (6,38), radius_x=4)
        self.add_line("left", (6,38), (6,10))
        self.add_arc("tl", (6,10), (10,6), radius_x=4)
        
        self.add_contour("sides", "tr", "right", "br", "bottom", "bl", "left", "tl")
        self.relate("connect", "top", "sides")
        self.add_polyline("tape", (16,6), (16,23), (24,17), (32,23), (32,6))
        self.relate("connect", "top", "tape")
        self.add_line("label", (28,33), (33,33))
