"""Independent 32px profile of beamed-eighth-notes.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '16a68778-68d4-5f6b-9ce5-e5182435ed96'
SOURCE_PATH = 'pictographic-primitives/music/music note_16a68778-68d4-5f6b-9ce5-e5182435ed96.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('16a68778-68d4-5f6b-9ce5-e5182435ed96', 'pictographic-primitives/music/music note_16a68778-68d4-5f6b-9ce5-e5182435ed96.svg'),)
PROFILE_SOURCE_KEYS = ('solo/beamed-eighth-notes',)
SOLO_SOURCE_ICON_IDS = ('beamed-eighth-notes',)
REFERENCE_EXPORT_SHA256 = '7f43070370e7f320a749982831a9f4b8f0dd7e582d78830eea1900a89aef3c66'

class DrawingContainerSymbol(Sub32):
    icon_id = 'beamed-eighth-notes-sub32-symbol'
    related_origin_icon_id = 'beamed-eighth-notes-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/beamed-eighth-notes-sub32'
    counterpart_icon_id = 'beamed-eighth-notes-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'music'
    categories = ('music', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 25), (12, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (12, 25), (2, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=True)
        self.add_line('p2-r1-1', (12, 25), (12, 7))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (20, 21), (30, 21), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (30, 21), (20, 21), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=True)
        self.add_line('p4-r1-1', (30, 21), (30, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (12, 7), (30, 2))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
