"""Independent 32px profile of building-with-sloping-roofline.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '24e8a2b3-57d5-4e9a-8572-c95bc40dc8e1'
SOURCE_PATH = 'pictographic-primitives/building/building_24e8a2b3-57d5-4e9a-8572-c95bc40dc8e1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('24e8a2b3-57d5-4e9a-8572-c95bc40dc8e1', 'pictographic-primitives/building/building_24e8a2b3-57d5-4e9a-8572-c95bc40dc8e1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/building-with-sloping-roofline',)
SOLO_SOURCE_ICON_IDS = ('building-with-sloping-roofline',)
REFERENCE_EXPORT_SHA256 = 'd7101193c3c9dafe56028a7a6070da2361601d3f01858ead120671f27cb30b6e'

class Drawing(Sub32):
    icon_id = 'building-with-sloping-roofline-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'building'
    categories = ('building', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (16, 8))
        self.add_line('p1-r1-2', (16, 8), (30, 14))
        self.add_line('p1-r1-3', (30, 14), (30, 21))
        self.add_line('p1-r1-4', (30, 21), (30, 30))
        self.add_line('p1-r1-5', (30, 30), (16, 30))
        self.add_line('p1-r1-6', (16, 30), (2, 30))
        self.add_line('p1-r1-7', (2, 30), (2, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (16, 2), (16, 8))
        self.add_line('p2-r1-2', (16, 8), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (24, 21), (30, 21))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-2')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-2')
        self.relate("connect", 'p1-r1-6', 'p2-r1-2')
