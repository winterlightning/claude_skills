"""Independent 32px profile of moon-right.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '97ddca27-a201-4081-8fac-1c56fa33848a'
SOURCE_PATH = 'pictographic-primitives/symbol/moon right_97ddca27-a201-4081-8fac-1c56fa33848a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('97ddca27-a201-4081-8fac-1c56fa33848a', 'pictographic-primitives/symbol/moon right_97ddca27-a201-4081-8fac-1c56fa33848a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/moon-right',)
SOLO_SOURCE_ICON_IDS = ('moon-right',)
REFERENCE_EXPORT_SHA256 = '015340a72213864764c5ab737f967069f1b0fc9d5aea98620ad9bc5600482c14'

class Drawing(Sub32):
    icon_id = 'moon-right-sub32'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (7, 2), ((17, 2), (25, 6), (25, 16)))
        self.add_bezier('p1-r1-2', (25, 16), ((25, 26), (17, 30), (7, 30)))
        self.add_bezier('p1-r1-3', (7, 30), ((15, 28), (18, 23), (18, 16)))
        self.add_bezier('p1-r1-4', (18, 16), ((18, 9), (15, 4), (7, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
