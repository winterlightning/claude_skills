"""Independent 32px profile of two-lines.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '1a1a483f-948c-443e-b5c1-de11dd76cdc8'
SOURCE_PATH = 'pictographic-primitives/symbol/two lines_1a1a483f-948c-443e-b5c1-de11dd76cdc8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1a1a483f-948c-443e-b5c1-de11dd76cdc8', 'pictographic-primitives/symbol/two lines_1a1a483f-948c-443e-b5c1-de11dd76cdc8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/two-lines',)
SOLO_SOURCE_ICON_IDS = ('two-lines',)
REFERENCE_EXPORT_SHA256 = 'be5842a1629a2c92cee176f49108bb1139c186dbb9152e4b7b52abacb53a05ec'

class Drawing(Sub32):
    icon_id = 'two-lines-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (27, 2), (27, 30))
        self.add_line('p1-r1-2', (27, 30), (5, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
