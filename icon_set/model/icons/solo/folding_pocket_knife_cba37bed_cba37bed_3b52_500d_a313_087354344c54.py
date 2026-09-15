"""Folding pocket knife (tools), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cba37bed-3b52-500d-a313-087354344c54'
SOURCE_PATH = 'pictographic-primitives/tools/folding pocket knife_cba37bed-3b52-500d-a313-087354344c54.svg'
AUTHOR = 'gpt-6'

class FoldingPocketKnifeCba37bed(Solo48):
    icon_id = 'folding-pocket-knife-cba37bed'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tools'
    aliases = ()
    keywords = ('folding', 'pocket', 'knife', 'tools')

    def build(self):
        self.add_line('e0', (31, 42), (11, 42))
        self.add_line('e1', (10, 31), (27, 31))
        self.add_line('e2', (31, 30), (33, 29))
        self.add_line('e3', (17, 20), (27, 31))
        self.add_line('e4-1', (38, 27), (41, 30))
        self.add_line('e4-2', (41, 30), (42, 34))
        self.add_line('e4-3', (42, 34), (40, 39))
        self.add_arc('e4-4', (40, 39), (31, 42), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_arc('e5-1', (11, 42), (6, 37), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e5-2', (6, 37), (7, 34), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e5-3', (7, 34), (10, 31), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('e6', (27, 31), (31, 30))
        self.add_arc('e7', (33, 29), (38, 27), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('e8-1', (38, 27), (21, 12))
        self.add_arc('e8-2', (21, 12), (11, 6), radius_x=71, radius_y=71, large_arc=False, sweep=False)
        self.add_arc('e8-3', (11, 6), (17, 20), radius_x=19, radius_y=19, large_arc=False, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e1', 'e6', 'e2', 'e7', closed=True)
        self.add_contour('c1', 'e8-1', 'e8-2', 'e8-3', 'e3', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
