"""Independent 32px profile of peace-travel.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2e44a4da-4f72-452e-869b-7b4b265330f4'
SOURCE_PATH = 'pictographic-primitives/travel/peace_2e44a4da-4f72-452e-869b-7b4b265330f4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2e44a4da-4f72-452e-869b-7b4b265330f4', 'pictographic-primitives/travel/peace_2e44a4da-4f72-452e-869b-7b4b265330f4.svg'),)
PROFILE_SOURCE_KEYS = ('solo/peace-travel',)
SOLO_SOURCE_ICON_IDS = ('peace-travel',)
REFERENCE_EXPORT_SHA256 = '727286c8478a7f95b8003dc97ebc10ab3900ebf01f0f559f3debb6dbc7ab07b2'

class Drawing(Sub32):
    icon_id = 'peace-travel-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'travel'
    categories = ('travel', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 30), (16, 15))
        self.add_line('p1-r1-2', (16, 15), (8, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (24, 27), (16, 15))
        self.add_line('p2-r1-2', (16, 15), (16, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (30, 16), (24, 27), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (24, 27), (8, 27), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (8, 27), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p3-r1-3')
        self.relate('connect', 'p1-r1-2', 'p3-r1-4')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-1', 'p3-r1-3')
