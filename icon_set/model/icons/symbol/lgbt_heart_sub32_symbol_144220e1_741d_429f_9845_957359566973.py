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
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Heart with two pride stripes: flatter lobes so three bands each keep 4 units.
        self.add_arc('p1-r1-1', (2, 6), (16, 6), radius_x=7, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 6), (30, 6), radius_x=7, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 6), (30, 14))
        self.add_line('p1-r1-4', (30, 14), (23, 22))
        self.add_line('p1-r1-5', (23, 22), (16, 30))
        self.add_line('p1-r1-6', (16, 30), (9, 22))
        self.add_line('p1-r1-7', (9, 22), (2, 14))
        self.add_line('p1-r1-8', (2, 14), (2, 6))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=True)
        self.add_line('p2-r1-1', (2, 14), (30, 14))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (9, 22), (23, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-7', 'p3-r1-1')
