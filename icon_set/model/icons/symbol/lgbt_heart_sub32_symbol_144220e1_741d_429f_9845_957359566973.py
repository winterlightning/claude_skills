"""Independent 32px profile of lgbt-heart.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '144220e1-741d-429f-9845-957359566973'
SOURCE_PATH = 'pictographic-primitives/symbol/lgbt heart_144220e1-741d-429f-9845-957359566973.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('144220e1-741d-429f-9845-957359566973', 'pictographic-primitives/symbol/lgbt heart_144220e1-741d-429f-9845-957359566973.svg'),)
PROFILE_SOURCE_KEYS = ('solo/lgbt-heart',)
SOLO_SOURCE_ICON_IDS = ('lgbt-heart',)
REFERENCE_EXPORT_SHA256 = '50f73b05417bfaade2793749f2bdeaf7563bfe4318472bff8f357c2e8c957fb8'

class DrawingContainerSymbol(Sub32):
    icon_id = 'lgbt-heart-sub32-symbol'
    related_origin_icon_id = 'lgbt-heart-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/lgbt-heart-sub32'
    counterpart_icon_id = 'lgbt-heart-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 9), ((14, 6), (12, 5), (9, 5)))
        self.add_arc('p1-r1-2', (9, 5), (2, 13), radius_x=7, radius_y=8, large_arc=False, sweep=False)
        self.add_bezier('p1-r1-3', (2, 13), ((2, 15), (4, 17), (6, 19)))
        self.add_line('p1-r1-4', (6, 19), (16, 27))
        self.add_line('p1-r1-5', (16, 27), (26, 19))
        self.add_bezier('p1-r1-6', (26, 19), ((28, 17), (30, 15), (30, 13)))
        self.add_arc('p1-r1-7', (30, 13), (23, 5), radius_x=7, radius_y=8, large_arc=False, sweep=False)
        self.add_bezier('p1-r1-8', (23, 5), ((20, 5), (18, 6), (16, 9)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (2, 13), (30, 13))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (6, 19), (26, 19))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
