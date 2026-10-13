"""Independent 32px profile of pie-chart-and-square.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '17f79cde-6e3f-435d-9f0d-3ea8fa026ef2'
SOURCE_PATH = 'pictographic-primitives/symbol/pie chart and square_17f79cde-6e3f-435d-9f0d-3ea8fa026ef2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('17f79cde-6e3f-435d-9f0d-3ea8fa026ef2', 'pictographic-primitives/symbol/pie chart and square_17f79cde-6e3f-435d-9f0d-3ea8fa026ef2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pie-chart-and-square',)
SOLO_SOURCE_ICON_IDS = ('pie-chart-and-square',)
REFERENCE_EXPORT_SHA256 = '4e9a6a2bce4d0c8bd0757ec02f82a55f4de1fc40c4ed6564d48268ed0557f626'

class Drawing(Sub32):
    icon_id = 'pie-chart-and-square-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Circle passing behind a square, the visible arc 4 units clear of the square.
        self.add_polyline('square', (14, 14), (30, 14), (30, 30), (14, 30), closed=True)
        self.add_arc('circle', (20, 6), (6, 20), radius_x=10, radius_y=10, large_arc=True, sweep=False)
