"""Independent 32px profile of bars-chart.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'c4684d55-3c14-4506-a1f7-229b8c33ab85'
SOURCE_PATH = 'pictographic-primitives/symbol/bars chart_c4684d55-3c14-4506-a1f7-229b8c33ab85.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c4684d55-3c14-4506-a1f7-229b8c33ab85', 'pictographic-primitives/symbol/bars chart_c4684d55-3c14-4506-a1f7-229b8c33ab85.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bars-chart',)
SOLO_SOURCE_ICON_IDS = ('bars-chart',)
REFERENCE_EXPORT_SHA256 = 'f017f7059068174897768af1da8d0446d281e63ae4ab8477256cb40f5de93ee7'

class DrawingVariant2(Sub32):
    icon_id = 'bars-chart-sub32-v2'
    related_origin_icon_id = 'bars-chart-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (30, short_high), (2, short_high))
        self.add_line('p1-r1-2', (2, short_high), (2, short_low))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (22, 17), (22, short_high))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (10, 12), (10, short_high))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
