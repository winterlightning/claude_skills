"""A rectangular banknote with a central ring. HRECT_L extremes (4,8)-(44,40). Lucide banknote informs the centered ring and landscape border. Retain the source plain outline without adding corner marks."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fbf0403-23f4-42d8-a096-400dbd664512'
SOURCE_PATH = 'pictographic-primitives/symbol/money bill_0fbf0403-23f4-42d8-a096-400dbd664512.svg'
AUTHOR = 'gpt-6'


class BanknoteSimple(Solo48):
    icon_id = 'banknote-simple'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('banknote', 'bill', 'cash', 'money', 'currency', 'payment', 'note', 'finance')

    def build(self) -> None:
        self.add_polyline('note',(4,8),(44,8),(44,40),(4,40),(4,8),closed=True)
        cx, cy, radius = 24, 24, 7
        self.add_arc('ring-top', (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc('ring-bottom', (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour('ring', 'ring-top', 'ring-bottom', closed=True)
