"""Independent 32px profile of arrow-thick-top-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e3d7b5b6-09dd-4914-98aa-6e9e8e9481e4'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow thick top_e3d7b5b6-09dd-4914-98aa-6e9e8e9481e4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e3d7b5b6-09dd-4914-98aa-6e9e8e9481e4', 'pictographic-primitives/symbol/arrow thick top_e3d7b5b6-09dd-4914-98aa-6e9e8e9481e4.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-thick-top-symbol',)
SOLO_SOURCE_ICON_IDS = ('arrow-thick-top-symbol',)
REFERENCE_EXPORT_SHA256 = '7690b702c11ba7e4cb38754a98175ca6e2d7343c3152d11919603615570f48ae'

class Drawing(Sub32):
    icon_id = 'arrow-thick-top-symbol-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 16), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (26, 15))
        self.add_line('p1-r1-3', (26, 15), (27, 16))
        self.add_line('p1-r1-4', (27, 16), (22, 16))
        self.add_line('p1-r1-5', (22, 16), (22, 30))
        self.add_line('p1-r1-6', (22, 30), (10, 30))
        self.add_line('p1-r1-7', (10, 30), (10, 16))
        self.add_line('p1-r1-8', (10, 16), (5, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
