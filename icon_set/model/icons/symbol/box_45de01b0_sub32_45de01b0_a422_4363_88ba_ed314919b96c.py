"""Independent 32px profile of box-45de01b0.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '45de01b0-a422-4363-88ba-ed314919b96c'
SOURCE_PATH = 'pictographic-primitives/shipping/box_45de01b0-a422-4363-88ba-ed314919b96c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('45de01b0-a422-4363-88ba-ed314919b96c', 'pictographic-primitives/shipping/box_45de01b0-a422-4363-88ba-ed314919b96c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/box-45de01b0',)
SOLO_SOURCE_ICON_IDS = ('box-45de01b0',)
REFERENCE_EXPORT_SHA256 = 'd402bea8204c14063404d239f7e4c203d685b0e057beee98db4aca559db00683'

class Drawing(Sub32):
    icon_id = 'box-45de01b0-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'shipping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 2), (12, 2))
        self.add_line('p1-r1-2', (12, 2), (20, 2))
        self.add_line('p1-r1-3', (20, 2), (27, 2))
        self.add_line('p1-r1-4', (27, 2), (27, 30))
        self.add_line('p1-r1-5', (27, 30), (5, 30))
        self.add_line('p1-r1-6', (5, 30), (5, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (12, 2), (12, 15))
        self.add_line('p2-r1-2', (12, 15), (16, 12))
        self.add_line('p2-r1-3', (16, 12), (20, 15))
        self.add_line('p2-r1-4', (20, 15), (20, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-4')
        self.relate('connect', 'p1-r1-3', 'p2-r1-4')
