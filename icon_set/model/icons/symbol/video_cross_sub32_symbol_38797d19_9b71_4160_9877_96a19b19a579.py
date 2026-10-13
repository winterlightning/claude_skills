"""Independent 32px profile of video-cross.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '38797d19-9b71-4160-9877-96a19b19a579'
SOURCE_PATH = 'pictographic-primitives/symbol/video cross_38797d19-9b71-4160-9877-96a19b19a579.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('38797d19-9b71-4160-9877-96a19b19a579', 'pictographic-primitives/symbol/video cross_38797d19-9b71-4160-9877-96a19b19a579.svg'),)
PROFILE_SOURCE_KEYS = ('solo/video-cross',)
SOLO_SOURCE_ICON_IDS = ('video-cross',)
REFERENCE_EXPORT_SHA256 = 'd2ca9280949924a9afa3a43e09fb3c198f1d0913054a20d8c3627b5c2002dd6e'

class DrawingContainerSymbol(Sub32):
    icon_id = 'video-cross-sub32-symbol'
    related_origin_icon_id = 'video-cross-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/video-cross-sub32'
    counterpart_icon_id = 'video-cross-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (22, 12), (22, 20))
        self.add_line('p1-r1-2', (22, 20), (29, 23))
        self.add_arc('p1-r1-3', (29, 23), (30, 22), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_line('p1-r1-4', (30, 22), (30, 10))
        self.add_arc('p1-r1-5', (30, 10), (29, 9), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_line('p1-r1-6', (29, 9), (22, 12))
        self.add_line('p1-r1-7', (22, 12), (22, 7))
        self.add_arc('p1-r1-8', (22, 7), (20, 4), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-9', (20, 4), (4, 4))
        self.add_arc('p1-r1-10', (4, 4), (2, 7), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p1-r1-11', (2, 7), (2, 25))
        self.add_arc('p1-r1-12', (2, 25), (4, 28), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p1-r1-13', (4, 28), (20, 28))
        self.add_arc('p1-r1-14', (20, 28), (22, 25), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-15', (22, 25), (22, 20))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', closed=False)
        self.add_line('p2-r1-1', (12, 12), (12, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (10, 16), (14, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
