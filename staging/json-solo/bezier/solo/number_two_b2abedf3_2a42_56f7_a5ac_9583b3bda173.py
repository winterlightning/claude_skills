"""Number two (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b2abedf3-2a42-56f7-a5ac-9583b3bda173'
SOURCE_PATH = 'icons-json/interface-essential/number two_b2abedf3-2a42-56f7-a5ac-9583b3bda173.json'
AUTHOR = 'json_to_solo'

class NumberTwoInterfaceEssential(Solo48):
    icon_id = 'number-two-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('number', 'two', 'interface-essential')

    def build(self):
        self.add_line('e0', (34, 24), (8, 44))
        self.add_line('e1', (8, 44), (40, 44))
        self.add_bezier('e2', (9, 11), ((12.348, 7.491), (17.834, 4.018), (24.062, 4.018)), ((24.283, 4.018), (24.505, 4), (24.726, 4)), ((24.73, 4), (24.733, 4), (24.737, 4)), ((24.967, 4), (25.185, 4.009), (25.403, 4.009)), ((26.978, 4.009), (28.615, 4.309), (30.092, 4.7)), ((39.225, 7.118), (40, 14.209), (37.12, 20.191)), ((36.283, 21.518), (35.391, 22.927), (34, 24)))
        self.add_contour('c0', 'e2', 'e0', 'e1')
