"""Protection sand bag (protection), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13b7d462-ded5-5fff-978a-c0240f20bf63'
SOURCE_PATH = 'icons-json/protection/protection sand bag_13b7d462-ded5-5fff-978a-c0240f20bf63.json'
AUTHOR = 'json_to_solo'

class ProtectionSandBag(Solo48):
    icon_id = 'protection-sand-bag'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('protection', 'sand', 'bag')

    def build(self):
        self.add_line('e0', (28, 13), (21, 13))
        self.add_line('e1', (13, 41), (36, 41))
        self.add_line('e2', (28, 13), (31, 6))
        self.add_line('e3', (31, 6), (17, 6))
        self.add_line('e4', (17, 6), (20, 13))
        self.add_arc('e5-1', (21, 13), (12, 18), radius_x=11, sweep=False)
        self.add_arc('e5-2', (12, 18), (8, 35), radius_x=37, sweep=False)
        self.add_line('e5-3', (8, 35), (6, 39))
        self.add_arc('e5-4', (6, 39), (9, 42), radius_x=3, sweep=False)
        self.add_line('e5-5', (9, 42), (13, 41))
        self.add_line('e6-1', (36, 41), (40, 42))
        self.add_line('e6-2', (40, 42), (42, 40))
        self.add_line('e6-3', (42, 40), (40, 35))
        self.add_arc('e6-4', (40, 35), (38, 22), radius_x=49, sweep=False)
        self.add_arc('e6-5', (38, 22), (28, 13), radius_x=13, sweep=False)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e1', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e2', 'e3', 'e4')
