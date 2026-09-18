"""Independent 32px profile of chart.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'e6769cc6-7edd-4638-9a68-d793ea0c3ccc'
SOURCE_PATH = 'pictographic-primitives/symbol/chart_e6769cc6-7edd-4638-9a68-d793ea0c3ccc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e6769cc6-7edd-4638-9a68-d793ea0c3ccc', 'pictographic-primitives/symbol/chart_e6769cc6-7edd-4638-9a68-d793ea0c3ccc.svg'),)
PROFILE_SOURCE_KEYS = ('solo/chart',)
SOLO_SOURCE_ICON_IDS = ('chart',)
REFERENCE_EXPORT_SHA256 = '6b4b517380ad3f8457c9b855151dcd5b641a872d0739fb5e778502b6bf0c99e4'

class DrawingVariant2(Sub32):
    icon_id = 'chart-sub32-v2'
    related_origin_icon_id = 'chart-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        peak_y, base_y, axis = (4, 28, 16)
        self.add_bezier('wave-left-rise', (2, base_y), ((6, base_y), (5, peak_y), (9, peak_y)))
        self.add_bezier('wave-left-fall', (9, peak_y), ((13, peak_y), (12, base_y), (axis, base_y)))
        self.add_bezier('wave-right-rise', (axis, base_y), ((20, base_y), (19, peak_y), (23, peak_y)))
        self.add_bezier('wave-right-fall', (23, peak_y), ((27, peak_y), (26, base_y), (30, base_y)))
        self.add_contour('path-1-1', 'wave-left-rise', 'wave-left-fall', 'wave-right-rise', 'wave-right-fall', closed=False)
