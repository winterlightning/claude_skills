# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of baby-head.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '454b702c-a035-5fa0-a3ec-ac065587fca8'
SOURCE_PATH = 'pictographic-primitives/babies/baby_454b702c-a035-5fa0-a3ec-ac065587fca8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('454b702c-a035-5fa0-a3ec-ac065587fca8', 'pictographic-primitives/babies/baby_454b702c-a035-5fa0-a3ec-ac065587fca8.svg'), ('5393b57b-1ff9-4e16-b855-128e09e91ba7', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/baby face_5393b57b-1ff9-4e16-b855-128e09e91ba7.svg'))
PROFILE_SOURCE_KEYS = ('solo/baby-head',)
SOLO_SOURCE_ICON_IDS = ('baby-head',)
REFERENCE_EXPORT_SHA256 = 'c68e2a7d40d4e7ea30956ae407215e1929527232a33f01a28390ff1f6647ba72'

class DrawingVariant2ContainerSymbol(Sub32):
    icon_id = 'baby-head-sub32-v2-symbol'
    variant_of = 'baby-head-sub32-v2'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/baby-head-sub32-v2'
    counterpart_icon_id = 'baby-head-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'babies'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('head-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'head-top', 'head-bottom', closed=True)
        self.add_bezier('hair', (16, 2), ((16, 6), (16, 8), (12, 8)))
        self.add_contour('path-2-1', 'hair', closed=False)
        self.relate('connect', 'head-top', 'hair')
        self.add_line('p3-r1-1', (10, 16), (10, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (22, 16), (22, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_bezier('p5-r1-1', (13, 22), ((14, 23), (15, 23), (16, 23)))
        self.add_bezier('p5-r1-2', (16, 23), ((17, 23), (18, 23), (19, 22)))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate('connect', 'path-1-1', 'path-2-1')
