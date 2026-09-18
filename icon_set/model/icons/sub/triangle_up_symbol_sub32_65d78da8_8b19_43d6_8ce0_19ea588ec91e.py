"""Independent 32px profile of triangle-up-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '65d78da8-8b19-43d6-8ce0-19ea588ec91e'
SOURCE_PATH = 'pictographic-primitives/symbol/triangle up_65d78da8-8b19-43d6-8ce0-19ea588ec91e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('65d78da8-8b19-43d6-8ce0-19ea588ec91e', 'pictographic-primitives/symbol/triangle up_65d78da8-8b19-43d6-8ce0-19ea588ec91e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/triangle-up-symbol',)
SOLO_SOURCE_ICON_IDS = ('triangle-up-symbol',)
REFERENCE_EXPORT_SHA256 = '355d144b0932d4c4dfb3912b5340b648e85b4f4aebf64dbc0ae870d1e237b886'

class Drawing(Sub32):
    icon_id = 'triangle-up-symbol-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 27), (15, 5))
        self.add_arc('p1-r1-2', (15, 5), (17, 5), radius_x=28, radius_y=28, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (17, 5), (30, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
