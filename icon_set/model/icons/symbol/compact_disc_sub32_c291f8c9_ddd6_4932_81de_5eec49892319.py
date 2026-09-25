"""Independent 32px profile of compact-disc.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'c291f8c9-ddd6-4932-81de-5eec49892319'
SOURCE_PATH = 'pictographic-primitives/computers/batch-03/cd_c291f8c9-ddd6-4932-81de-5eec49892319.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c291f8c9-ddd6-4932-81de-5eec49892319', 'pictographic-primitives/computers/batch-03/cd_c291f8c9-ddd6-4932-81de-5eec49892319.svg'),)
PROFILE_SOURCE_KEYS = ('solo/compact-disc',)
SOLO_SOURCE_ICON_IDS = ('compact-disc',)
REFERENCE_EXPORT_SHA256 = '0cd8854895ed2a36ffcd8b09f53ddd4b3309d70d1348250130f5b4e0b0948cd4'

class Drawing(Sub32):
    icon_id = 'compact-disc-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'computers'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (30, 16), (16, 30), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 30), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (2, 16), (16, 2), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 2), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_arc('p2-r1-1', (20, 16), (16, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (16, 20), (12, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (12, 16), (16, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-4', (16, 12), (20, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
