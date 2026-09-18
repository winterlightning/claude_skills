"""Independent 32px profile of circle-half-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '031da5e5-a8c4-45af-9b74-e8c1dae95201'
SOURCE_PATH = 'pictographic-primitives/symbol/circle half_031da5e5-a8c4-45af-9b74-e8c1dae95201.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('031da5e5-a8c4-45af-9b74-e8c1dae95201', 'pictographic-primitives/symbol/circle half_031da5e5-a8c4-45af-9b74-e8c1dae95201.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circle-half-symbol',)
SOLO_SOURCE_ICON_IDS = ('circle-half-symbol',)
REFERENCE_EXPORT_SHA256 = '9a30803427845e3ff74742cfd3daef328feb41fd02bc202cb1fcfe6b48bc2c33'

class DrawingVariant2(Sub32):
    icon_id = 'circle-half-symbol-sub32-v2'
    related_origin_icon_id = 'circle-half-symbol-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        right, axis_y, radius_x, radius_y = (28, 16, 24, 14)
        top, left, bottom = ((right, axis_y - radius_y), (right - radius_x, axis_y), (right, axis_y + radius_y))
        self.add_arc('half-upper', top, left, radius_x=radius_x, radius_y=radius_y, sweep=False)
        self.add_arc('half-lower', left, bottom, radius_x=radius_x, radius_y=radius_y, sweep=False)
        self.add_line('diameter', bottom, top)
        self.add_contour('path-1-1', 'half-upper', 'half-lower', 'diameter', closed=True)
