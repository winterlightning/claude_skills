"""Batch-04/astrology libra (culture), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf03c01d-0ec1-5a48-b85f-a420423f6055'
SOURCE_PATH = 'icons-json/culture/batch-04/astrology libra_cf03c01d-0ec1-5a48-b85f-a420423f6055.json'
AUTHOR = 'json_to_solo'

class Batch04AstrologyLibra(Solo48):
    icon_id = 'batch-04-astrology-libra'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('batch', 'astrology', 'libra', 'culture')

    def build(self):
        self.add_line('e0', (4, 30), (15, 30))
        self.add_line('e1', (36, 24), (34, 30))
        self.add_line('e2', (34, 30), (44, 30))
        self.add_line('e3', (4, 40), (44, 40))
        self.add_bezier('e4', (15, 30), ((13.5, 27.38), (12.009, 24.76), (11.9, 21.58)), ((11.655, 14.82), (17.009, 8.02), (23.336, 8.02)), ((23.542, 8.02), (23.757, 8), (23.963, 8)), ((23.966, 8), (23.969, 8), (23.973, 8)), ((24.182, 8), (24.391, 8.02), (24.609, 8.02)), ((30.955, 8.02), (36.336, 14.83), (36, 21.63)), ((35.955, 22.35), (36.209, 23.31), (36, 24)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e2')
        self.add_contour('c1', 'e3')
