"""Independent 32px profile of horn.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '82d50937-0e36-4f84-b67b-aafe2b74a0ce'
SOURCE_PATH = 'pictographic-primitives/transportation/horn_82d50937-0e36-4f84-b67b-aafe2b74a0ce.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('82d50937-0e36-4f84-b67b-aafe2b74a0ce', 'pictographic-primitives/transportation/horn_82d50937-0e36-4f84-b67b-aafe2b74a0ce.svg'),)
PROFILE_SOURCE_KEYS = ('solo/horn',)
SOLO_SOURCE_ICON_IDS = ('horn',)
REFERENCE_EXPORT_SHA256 = '78f31830a9201ccb3190ed0578582ef53e345604c5515f7c375688fc55df65d7'

class Drawing(Sub32):
    icon_id = 'horn-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (9, 12))
        self.add_line('p1-r1-2', (9, 12), (23, 12))
        self.add_line('p1-r1-3', (23, 12), (30, 5))
        self.add_line('p1-r1-4', (30, 5), (30, 22))
        self.add_line('p1-r1-5', (30, 22), (23, 17))
        self.add_line('p1-r1-6', (23, 17), (9, 17))
        self.add_line('p1-r1-7', (9, 17), (2, 22))
        self.add_line('p1-r1-8', (2, 22), (2, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (9, 17), (9, 24))
        self.add_arc('p2-r1-2', (9, 24), (12, 27), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p2-r1-3', (12, 27), (20, 27))
        self.add_arc('p2-r1-4', (20, 27), (23, 24), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p2-r1-5', (23, 24), (23, 17))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.relate('connect', 'p1-r1-5', 'p2-r1-5')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-5')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
