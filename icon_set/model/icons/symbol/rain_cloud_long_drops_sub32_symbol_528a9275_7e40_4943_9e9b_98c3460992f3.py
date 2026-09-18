"""Independent 32px profile of rain-cloud-long-drops.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '528a9275-7e40-4943-9e9b-98c3460992f3'
SOURCE_PATH = 'pictographic-primitives/symbol/rain_528a9275-7e40-4943-9e9b-98c3460992f3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('528a9275-7e40-4943-9e9b-98c3460992f3', 'pictographic-primitives/symbol/rain_528a9275-7e40-4943-9e9b-98c3460992f3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rain-cloud-long-drops',)
SOLO_SOURCE_ICON_IDS = ('rain-cloud-long-drops',)
REFERENCE_EXPORT_SHA256 = '88b911da2ffb314ebf8eb227491a58b5e0b11132a1ae03ff710f1da14265d726'

class DrawingContainerSymbol(Sub32):
    icon_id = 'rain-cloud-long-drops-sub32-symbol'
    related_origin_icon_id = 'rain-cloud-long-drops-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/rain-cloud-long-drops-sub32'
    counterpart_icon_id = 'rain-cloud-long-drops-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (8, 8), (24, 8), radius_x=8, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (24, 8), (30, 11), radius_x=6, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (30, 11), (24, 14), radius_x=6, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (24, 14), (8, 14))
        self.add_arc('p1-r1-5', (8, 14), (2, 11), radius_x=6, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (2, 11), (8, 8), radius_x=6, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (8, 21), (7, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (18, 21), (16, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (27, 21), (25, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
