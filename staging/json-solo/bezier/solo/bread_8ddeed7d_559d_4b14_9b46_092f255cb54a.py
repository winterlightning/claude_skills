"""Bread (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ddeed7d-559d-4b14-9b46-092f255cb54a'
SOURCE_PATH = 'icons-json/symbol/bread_8ddeed7d-559d-4b14-9b46-092f255cb54a.json'
AUTHOR = 'json_to_solo'

class BreadSymbol(Solo48):
    icon_id = 'bread-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bread', 'symbol')

    def build(self):
        self.add_line('e0', (39, 18), (41, 17))
        self.add_line('e1', (33, 6), (18, 6))
        self.add_line('e2', (8, 17), (9, 18))
        self.add_line('e3', (9, 18), (9, 42))
        self.add_line('e4', (9, 42), (11, 42))
        self.add_line('e5', (11, 42), (34, 42))
        self.add_line('e6', (34, 42), (39, 42))
        self.add_line('e7', (39, 42), (39, 18))
        self.add_bezier('e8', (41, 17), ((41.532, 16.067), (41.992, 14.935), (41.992, 13.838)), ((41.992, 13.717), (42, 13.589), (42, 13.46)), ((42, 13.458), (42, 13.456), (42, 13.454)), ((42, 13.396), (41.992, 13.339), (41.992, 13.274)), ((41.992, 9.535), (38.662, 7.399), (35.455, 6.45)), ((35.078, 6.335), (34.645, 6), (34.252, 6)), ((33.835, 6), (33.417, 6), (33, 6)))
        self.add_bezier('e9', (18, 6), ((17.247, 6), (16.767, 6.008), (16.015, 6.008)), ((12.586, 6.008), (9.068, 7.219), (7.047, 10.091)), ((6.475, 10.901), (6.016, 11.973), (6.016, 12.995)), ((6.008, 13.052), (6, 13.1), (6, 13.156)), ((6, 13.157), (6, 13.158), (6, 13.159)), ((6, 14.509), (7.174, 16.043), (8, 17)))
        self.add_contour('c0', 'e0', 'e8', 'e1', 'e9', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', closed=True)
