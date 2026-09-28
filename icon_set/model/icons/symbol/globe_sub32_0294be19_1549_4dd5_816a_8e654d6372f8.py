"""Independent 32px profile of globe.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '0294be19-1549-4dd5-816a-8e654d6372f8'
SOURCE_PATH = 'pictographic-primitives/symbol/globe_0294be19-1549-4dd5-816a-8e654d6372f8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0294be19-1549-4dd5-816a-8e654d6372f8', 'pictographic-primitives/symbol/globe_0294be19-1549-4dd5-816a-8e654d6372f8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/globe',)
SOLO_SOURCE_ICON_IDS = ('globe',)
REFERENCE_EXPORT_SHA256 = '820fdfb9a58dc6d7c86b3e2c58da6a32a2315711a0efcfae3becfd093bb1844f'

class Drawing(Sub32):
    icon_id = 'globe-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 2), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (16, 30), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (16, 30), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (2, 16), (16, 2), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_arc('p2-r1-1', (16, 2), (9, 16), radius_x=7, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('p2-r1-2', (9, 16), (16, 30), radius_x=7, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('p2-r1-3', (16, 30), (23, 16), radius_x=7, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('p2-r1-4', (23, 16), (16, 2), radius_x=7, radius_y=14, large_arc=False, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 16), (9, 16))
        self.add_line('p3-r1-2', (9, 16), (23, 16))
        self.add_line('p3-r1-3', (23, 16), (30, 16))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-4')
        self.relate('connect', 'p1-r1-1', 'p3-r1-3')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
        self.relate('connect', 'p1-r1-2', 'p3-r1-3')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-3')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-4')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
        self.relate('connect', 'p2-r1-3', 'p3-r1-2')
        self.relate('connect', 'p2-r1-3', 'p3-r1-3')
        self.relate('connect', 'p2-r1-4', 'p3-r1-2')
        self.relate('connect', 'p2-r1-4', 'p3-r1-3')
