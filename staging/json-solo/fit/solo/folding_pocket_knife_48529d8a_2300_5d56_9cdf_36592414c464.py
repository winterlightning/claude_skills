"""Folding pocket knife (tools), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48529d8a-2300-5d56-9cdf-36592414c464'
SOURCE_PATH = 'icons-json/tools/folding pocket knife_48529d8a-2300-5d56-9cdf-36592414c464.json'
AUTHOR = 'json_to_solo'

class FoldingPocketKnife48529d8a(Solo48):
    icon_id = 'folding-pocket-knife-48529d8a'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tools'
    aliases = ()
    keywords = ('folding', 'pocket', 'knife', 'tools')

    def build(self):
        self.add_line('e0', (35, 24), (23, 12))
        self.add_line('e1', (20, 20), (29, 27))
        self.add_line('e2', (22, 31), (29, 27))
        self.add_arc('e3-1', (23, 12), (11, 4), radius_x=54, sweep=False)
        self.add_arc('e3-2', (11, 4), (20, 20), radius_x=20, sweep=False)
        self.add_arc('e4-1', (29, 27), (40, 29), radius_x=6)
        self.add_arc('e4-2', (40, 29), (32, 37), radius_x=11)
        self.add_arc('e4-3', (32, 37), (13, 44), radius_x=42)
        self.add_arc('e4-4', (13, 44), (8, 39), radius_x=5)
        self.add_arc('e4-5', (8, 39), (10, 36), radius_x=4)
        self.add_arc('e4-6', (10, 36), (22, 31), radius_x=39, sweep=False)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e1')
        self.add_contour('c1', 'e2', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
