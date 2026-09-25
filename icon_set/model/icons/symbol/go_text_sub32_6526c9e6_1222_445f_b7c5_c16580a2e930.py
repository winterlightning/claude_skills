"""Independent 32px profile of go-text.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '6526c9e6-1222-445f-b7c5-c16580a2e930'
SOURCE_PATH = 'pictographic-primitives/symbol/GO_6526c9e6-1222-445f-b7c5-c16580a2e930.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6526c9e6-1222-445f-b7c5-c16580a2e930', 'pictographic-primitives/symbol/GO_6526c9e6-1222-445f-b7c5-c16580a2e930.svg'),)
PROFILE_SOURCE_KEYS = ('solo/go-text',)
SOLO_SOURCE_ICON_IDS = ('go-text',)
REFERENCE_EXPORT_SHA256 = '425f4aa0b5fac6db2bd8a75e28e74fde34c22ee567fe8bbb24e998511389b6a5'

class Drawing(Sub32):
    icon_id = 'go-text-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (13, 10), (2, 10), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p1-r1-2', (2, 10), (2, 22))
        self.add_arc('p1-r1-3', (2, 22), (13, 22), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (13, 22), (13, 17))
        self.add_line('p2-r1-2', (13, 17), (8, 17))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (19, 10), (30, 10), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p3-r1-2', (30, 10), (30, 22))
        self.add_arc('p3-r1-3', (30, 22), (19, 22), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p3-r1-4', (19, 22), (19, 10))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
