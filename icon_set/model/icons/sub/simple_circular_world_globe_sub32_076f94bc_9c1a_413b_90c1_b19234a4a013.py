"""Independent 32px profile of simple-circular-world-globe-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '076f94bc-9c1a-413b-90c1-b19234a4a013'
SOURCE_PATH = 'pictographic-primitives/other/globe_076f94bc-9c1a-413b-90c1-b19234a4a013.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('076f94bc-9c1a-413b-90c1-b19234a4a013', 'pictographic-primitives/other/globe_076f94bc-9c1a-413b-90c1-b19234a4a013.svg'),)
PROFILE_SOURCE_KEYS = ('solo/simple-circular-world-globe-solo',)
SOLO_SOURCE_ICON_IDS = ('simple-circular-world-globe-solo',)
REFERENCE_EXPORT_SHA256 = '3451a22be3e3e7a85b085e9af7b2d07d5d12ffe3cfe55bc9038095d637f6759e'

class Drawing(Sub32):
    icon_id = 'simple-circular-world-globe-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 16), (16, 16))
        self.add_line('p2-r1-2', (16, 16), (30, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 2), (16, 16))
        self.add_line('p3-r1-2', (16, 16), (16, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-2')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-2')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-2')
