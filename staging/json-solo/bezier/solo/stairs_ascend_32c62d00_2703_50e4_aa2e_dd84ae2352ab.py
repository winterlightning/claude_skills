"""Stairs ascend (wayfinding), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '32c62d00-2703-50e4-aa2e-dd84ae2352ab'
SOURCE_PATH = 'icons-json/wayfinding/stairs ascend_32c62d00-2703-50e4-aa2e-dd84ae2352ab.json'
AUTHOR = 'json_to_solo'

class StairsAscendWayfinding(Solo48):
    icon_id = 'stairs-ascend-wayfinding'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('stairs', 'ascend', 'wayfinding')

    def build(self):
        self.add_line('e0', (15, 8), (24, 8))
        self.add_line('e1', (4, 26), (24, 8))
        self.add_line('e2', (24, 8), (24, 16))
        self.add_line('e3', (44, 17), (32, 17))
        self.add_line('e4', (32, 17), (32, 25))
        self.add_line('e5', (32, 25), (23, 25))
        self.add_line('e6', (23, 25), (23, 32))
        self.add_line('e7', (23, 32), (14, 32))
        self.add_line('e8', (14, 32), (14, 40))
        self.add_line('e9', (4, 40), (44, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8')
        self.add_contour('c3', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c3')
