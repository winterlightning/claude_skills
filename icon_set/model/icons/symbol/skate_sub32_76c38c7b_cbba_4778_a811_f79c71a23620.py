"""Independent 32px profile of skate.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '76c38c7b-cbba-4778-a811-f79c71a23620'
SOURCE_PATH = 'pictographic-primitives/symbol/skate_76c38c7b-cbba-4778-a811-f79c71a23620.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('76c38c7b-cbba-4778-a811-f79c71a23620', 'pictographic-primitives/symbol/skate_76c38c7b-cbba-4778-a811-f79c71a23620.svg'),)
PROFILE_SOURCE_KEYS = ('solo/skate',)
SOLO_SOURCE_ICON_IDS = ('skate',)
REFERENCE_EXPORT_SHA256 = '8c0bb1d9bfcb7346c784029b9b658127b34e7546f061d6759cd95af0e1eb889a'

class Drawing(Sub32):
    icon_id = 'skate-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 5), ((3, 10), (4, 14), (8, 16)))
        self.add_line('p1-r1-2', (8, 16), (24, 16))
        self.add_bezier('p1-r1-3', (24, 16), ((28, 14), (29, 10), (30, 5)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (8, 27), (8, 27))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (24, 27), (24, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
