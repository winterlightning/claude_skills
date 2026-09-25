"""Independent 32px profile of zigzag-interface-essential.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '4ba83493-5971-4220-bddb-eb4384430fd7'
SOURCE_PATH = 'pictographic-primitives/interface-essential/zigzag_4ba83493-5971-4220-bddb-eb4384430fd7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4ba83493-5971-4220-bddb-eb4384430fd7', 'pictographic-primitives/interface-essential/zigzag_4ba83493-5971-4220-bddb-eb4384430fd7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/zigzag-interface-essential',)
SOLO_SOURCE_ICON_IDS = ('zigzag-interface-essential',)
REFERENCE_EXPORT_SHA256 = '3ffe3c9893e2b36525431966b61b233f9831ed0197b782d24deab00e0f9a0d34'

class Drawing(Sub32):
    icon_id = 'zigzag-interface-essential-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (23, 17), (27, 21))
        self.add_line('p1-r1-2', (27, 21), (22, 24))
        self.add_line('p1-r1-3', (22, 24), (27, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (8, 16), (11, 21))
        self.add_line('p2-r1-2', (11, 21), (5, 24))
        self.add_line('p2-r1-3', (5, 24), (9, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (13, 2), (18, 6))
        self.add_line('p3-r1-2', (18, 6), (13, 10))
        self.add_line('p3-r1-3', (13, 10), (18, 14))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
