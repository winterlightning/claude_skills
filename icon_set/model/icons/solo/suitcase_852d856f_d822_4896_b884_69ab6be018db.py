"""Suitcase (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '852d856f-d822-4896-b884-69ab6be018db'
SOURCE_PATH = 'pictographic-primitives/symbol/suitcase_852d856f-d822-4896-b884-69ab6be018db.svg'
AUTHOR = 'gpt-6'

class Suitcase(Solo48):
    icon_id = 'suitcase'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('suitcase', 'symbol')

    def build(self):
        self.add_line('sym-e0', (35, 40), (35, 16))
        self.add_line('sym-e1', (35, 16), (39, 16))
        self.add_arc('sym-e2', (39, 16), (44, 20), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e3', (44, 20), (44, 37))
        self.add_arc('sym-e4', (44, 37), (41, 40), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e5-1', (41, 40), (40, 40))
        self.add_arc('sym-e5-2', (40, 40), (39, 40), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_line('sym-e6', (39, 40), (13, 40))
        self.add_line('sym-e10', (13, 40), (13, 16))
        self.add_line('sym-e11', (13, 16), (9, 16))
        self.add_arc('sym-e12', (9, 16), (4, 20), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e13', (4, 20), (4, 37))
        self.add_arc('sym-e14', (4, 37), (7, 40), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e15-1', (7, 40), (8, 40))
        self.add_arc('sym-e15-2', (8, 40), (9, 40), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_line('sym-e16', (9, 40), (13, 40))
        self.add_line('sym-e18', (24, 8), (30, 8))
        self.add_arc('sym-e20', (30, 8), (33, 11), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e21', (33, 11), (33, 16))
        self.add_line('sym-e22', (33, 16), (35, 16))
        self.add_line('sym-e23', (33, 16), (15, 16))
        self.add_line('sym-e25', (15, 16), (15, 11))
        self.add_arc('sym-e26', (15, 11), (18, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e27', (18, 8), (24, 8))
        self.add_line('sym-e29', (13, 16), (15, 16))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5-1', 'sym-e5-2', 'sym-e6', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15-1', 'sym-e15-2', 'sym-e16', closed=False)
        self.add_contour('sym-c1', 'sym-e18', 'sym-e20', 'sym-e21', 'sym-e22', closed=False)
        self.add_contour('sym-c2', 'sym-e23', 'sym-e25', 'sym-e26', 'sym-e27', closed=False)
        self.add_contour('sym-c3', 'sym-e29', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')

SOURCE_REFERENCES = (('e5b10ed9-04b3-459c-88b3-1713b82f6977', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/luggage_e5b10ed9-04b3-459c-88b3-1713b82f6977.svg'),)
