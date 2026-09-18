"""Independent 32px profile of circle-medical-cross.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c8cdc83b-0683-4b47-8454-a4e5b0461a29'
SOURCE_PATH = 'pictographic-primitives/state/circle medical cross_c8cdc83b-0683-4b47-8454-a4e5b0461a29.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c8cdc83b-0683-4b47-8454-a4e5b0461a29', 'pictographic-primitives/state/circle medical cross_c8cdc83b-0683-4b47-8454-a4e5b0461a29.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circle-medical-cross',)
SOLO_SOURCE_ICON_IDS = ('circle-medical-cross',)
REFERENCE_EXPORT_SHA256 = '6b5897c0715475331a4c23c3c0144e510287deaea8f4892d5fbce5c4d560d5a8'

class Drawing(Sub32):
    icon_id = 'circle-medical-cross-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 9), (16, 23))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (10, 16), (22, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
