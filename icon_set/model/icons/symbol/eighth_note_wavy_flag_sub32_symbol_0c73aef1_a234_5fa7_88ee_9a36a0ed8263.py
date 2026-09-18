"""Independent 32px profile of eighth-note-wavy-flag.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '0c73aef1-a234-5fa7-88ee-9a36a0ed8263'
SOURCE_PATH = 'pictographic-primitives/music/music note_0c73aef1-a234-5fa7-88ee-9a36a0ed8263.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0c73aef1-a234-5fa7-88ee-9a36a0ed8263', 'pictographic-primitives/music/music note_0c73aef1-a234-5fa7-88ee-9a36a0ed8263.svg'),)
PROFILE_SOURCE_KEYS = ('solo/eighth-note-wavy-flag',)
SOLO_SOURCE_ICON_IDS = ('eighth-note-wavy-flag',)
REFERENCE_EXPORT_SHA256 = 'f72f78d8bcbe0c60b91ef44863877b687f05c79fbd301134ecc2e2268aa2f113'

class DrawingContainerSymbol(Sub32):
    icon_id = 'eighth-note-wavy-flag-sub32-symbol'
    related_origin_icon_id = 'eighth-note-wavy-flag-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/eighth-note-wavy-flag-sub32'
    counterpart_icon_id = 'eighth-note-wavy-flag-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/music'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 24), (10, 19), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (10, 19), (16, 24), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (16, 24), (10, 30), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (10, 30), (5, 24), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (16, 24), (16, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (16, 2), ((16, 8), (27, 8), (27, 13)))
        self.add_bezier('p3-r1-2', (27, 13), ((27, 16), (24, 17), (24, 19)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
