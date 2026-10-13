"""Independent 32px profile of rounded-milk-bottle-with-flared-mouth.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '5612c8eb-6383-491c-93b7-71057a5f1e8f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/milk_5612c8eb-6383-491c-93b7-71057a5f1e8f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5612c8eb-6383-491c-93b7-71057a5f1e8f', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/milk_5612c8eb-6383-491c-93b7-71057a5f1e8f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rounded-milk-bottle-with-flared-mouth',)
SOLO_SOURCE_ICON_IDS = ('rounded-milk-bottle-with-flared-mouth',)
REFERENCE_EXPORT_SHA256 = '420aff0df18cf2546160d699eff001fff6bd1b4c3caede141920ed546d769fd0'

class Drawing(Sub32):
    icon_id = 'rounded-milk-bottle-with-flared-mouth-sub32'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'drinks'
    categories = ('drinks', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (10, 8), (10, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (10, 2), (22, 2))
        self.add_arc('p1-r1-3', (22, 2), (22, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (22, 8), (10, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (10, 8), (10, 10))
        self.add_arc('p2-r1-2', (10, 10), (8, 15), radius_x=2, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (8, 15), (6, 19), radius_x=2, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p2-r1-4', (6, 19), (6, 26))
        self.add_arc('p2-r1-5', (6, 26), (10, 30), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p2-r1-6', (10, 30), (22, 30))
        self.add_arc('p2-r1-7', (22, 30), (26, 26), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p2-r1-8', (26, 26), (26, 19))
        self.add_arc('p2-r1-9', (26, 19), (24, 15), radius_x=2, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('p2-r1-10', (24, 15), (22, 10), radius_x=2, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-11', (22, 10), (22, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', 'p2-r1-11', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-11')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-11')
