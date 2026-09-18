"""Independent 32px profile of loading-bar-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a0e10581-e9da-4ad2-86ee-9fb92f7f28f3'
SOURCE_PATH = 'pictographic-primitives/interface-essential/loading bar 1_a0e10581-e9da-4ad2-86ee-9fb92f7f28f3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a0e10581-e9da-4ad2-86ee-9fb92f7f28f3', 'pictographic-primitives/interface-essential/loading bar 1_a0e10581-e9da-4ad2-86ee-9fb92f7f28f3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/loading-bar-1',)
SOLO_SOURCE_ICON_IDS = ('loading-bar-1',)
REFERENCE_EXPORT_SHA256 = 'fcfe06951f6fb5a902e6d72293d5967d601599f5ae411ce8a35ce3fe8c4eca69'

class Drawing(Sub32):
    icon_id = 'loading-bar-1-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (6, 5), (17, 5))
        self.add_line('p1-r1-2', (17, 5), (26, 5))
        self.add_line('p1-r1-3', (26, 5), (26, 5))
        self.add_bezier('p1-r1-4', (26, 5), ((29, 5), (30, 9), (30, 16)))
        self.add_bezier('p1-r1-5', (30, 16), ((30, 23), (29, 27), (26, 27)))
        self.add_line('p1-r1-6', (26, 27), (17, 27))
        self.add_line('p1-r1-7', (17, 27), (7, 27))
        self.add_line('p1-r1-8', (7, 27), (6, 27))
        self.add_bezier('p1-r1-9', (6, 27), ((3, 27), (2, 23), (2, 16)))
        self.add_bezier('p1-r1-10', (2, 16), ((2, 9), (3, 5), (6, 5)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (17, 5), (7, 27))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (26, 5), (17, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
        self.relate("connect", 'p1-r1-6', 'p3-r1-1')
        self.relate("connect", 'p1-r1-7', 'p2-r1-1')
        self.relate("connect", 'p1-r1-7', 'p3-r1-1')
        self.relate("connect", 'p1-r1-8', 'p2-r1-1')
