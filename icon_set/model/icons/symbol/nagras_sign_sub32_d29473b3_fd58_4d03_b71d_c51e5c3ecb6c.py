"""Independent 32px profile of nagras-sign.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'd29473b3-fd58-4d03-b71d-c51e5c3ecb6c'
SOURCE_PATH = 'pictographic-primitives/symbol/nagras sign_d29473b3-fd58-4d03-b71d-c51e5c3ecb6c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d29473b3-fd58-4d03-b71d-c51e5c3ecb6c', 'pictographic-primitives/symbol/nagras sign_d29473b3-fd58-4d03-b71d-c51e5c3ecb6c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/nagras-sign',)
SOLO_SOURCE_ICON_IDS = ('nagras-sign',)
REFERENCE_EXPORT_SHA256 = '99880d4bea0692ff5804b3202efdbd72ea34e80aa3e8445074ba47fa84e6f1ba'

class Drawing(Sub32):
    icon_id = 'nagras-sign-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (25, 29), (17, 16))
        self.add_line('p1-r1-2', (17, 16), (2, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (25, 29), (25, 16))
        self.add_line('p2-r1-2', (25, 16), (30, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (7, 30), (7, 2))
        self.add_line('p3-r1-2', (7, 2), (16, 16))
        self.add_line('p3-r1-3', (16, 16), (25, 16))
        self.add_line('p3-r1-4', (25, 16), (25, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-3')
        self.relate('connect', 'p2-r1-1', 'p3-r1-4')
        self.relate('connect', 'p2-r1-2', 'p3-r1-3')
        self.relate('connect', 'p2-r1-2', 'p3-r1-4')
