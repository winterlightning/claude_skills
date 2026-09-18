"""Independent 32px profile of building.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '18b35c04-4431-44f3-9c6e-e6b8f421efaa'
SOURCE_PATH = 'pictographic-primitives/building/building_18b35c04-4431-44f3-9c6e-e6b8f421efaa.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('18b35c04-4431-44f3-9c6e-e6b8f421efaa', 'pictographic-primitives/building/building_18b35c04-4431-44f3-9c6e-e6b8f421efaa.svg'),)
PROFILE_SOURCE_KEYS = ('solo/building',)
SOLO_SOURCE_ICON_IDS = ('building',)
REFERENCE_EXPORT_SHA256 = 'e1143185a448471579457b69cb9f93509d07b5f239f9784e1bc67b71e37d6e4f'

class Drawing(Sub32):
    icon_id = 'building-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'building'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 30), (8, 6))
        self.add_line('p1-r1-2', (8, 6), (24, 16))
        self.add_line('p1-r1-3', (24, 16), (24, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (8, 2), (8, 6))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (13, 30), (13, 22))
        self.add_line('p3-r1-2', (13, 22), (19, 22))
        self.add_line('p3-r1-3', (19, 22), (19, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (5, 30), (8, 30))
        self.add_line('p4-r1-2', (8, 30), (13, 30))
        self.add_line('p4-r1-3', (13, 30), (19, 30))
        self.add_line('p4-r1-4', (19, 30), (24, 30))
        self.add_line('p4-r1-5', (24, 30), (27, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p4-r1-1')
        self.relate("connect", 'p1-r1-1', 'p4-r1-2')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p4-r1-4')
        self.relate("connect", 'p1-r1-3', 'p4-r1-5')
        self.relate("connect", 'p3-r1-1', 'p4-r1-2')
        self.relate("connect", 'p3-r1-1', 'p4-r1-3')
        self.relate("connect", 'p3-r1-3', 'p4-r1-3')
        self.relate("connect", 'p3-r1-3', 'p4-r1-4')
