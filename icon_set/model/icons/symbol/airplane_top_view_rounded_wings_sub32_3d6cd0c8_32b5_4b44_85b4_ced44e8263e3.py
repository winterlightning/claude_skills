"""Independent 32px profile of airplane-top-view-rounded-wings.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '3d6cd0c8-32b5-4b44-85b4-ced44e8263e3'
SOURCE_PATH = 'pictographic-primitives/travel/plane_3d6cd0c8-32b5-4b44-85b4-ced44e8263e3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3d6cd0c8-32b5-4b44-85b4-ced44e8263e3', 'pictographic-primitives/travel/plane_3d6cd0c8-32b5-4b44-85b4-ced44e8263e3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/airplane-top-view-rounded-wings',)
SOLO_SOURCE_ICON_IDS = ('airplane-top-view-rounded-wings',)
REFERENCE_EXPORT_SHA256 = 'fb4447582230d026b2568ca5211b41e60f1eebd3e3151a344cbe3a61af0633b2'

class Drawing(Sub32):
    icon_id = 'airplane-top-view-rounded-wings-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'travel'
    categories = ('travel', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (20, 6), (20, 7))
        self.add_line('p1-r1-2', (20, 7), (27, 9))
        self.add_arc('p1-r1-3', (27, 9), (27, 17), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (27, 17), (20, 14))
        self.add_line('p1-r1-5', (20, 14), (20, 21))
        self.add_line('p1-r1-6', (20, 21), (24, 22))
        self.add_arc('p1-r1-7', (24, 22), (24, 30), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (24, 30), (16, 27))
        self.add_line('p1-r1-9', (16, 27), (8, 30))
        self.add_arc('p1-r1-10', (8, 30), (8, 22), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-11', (8, 22), (12, 21))
        self.add_line('p1-r1-12', (12, 21), (12, 14))
        self.add_line('p1-r1-13', (12, 14), (5, 17))
        self.add_arc('p1-r1-14', (5, 17), (5, 9), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-15', (5, 9), (12, 7))
        self.add_line('p1-r1-16', (12, 7), (12, 6))
        self.add_arc('p1-r1-17', (12, 6), (20, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', closed=False)
