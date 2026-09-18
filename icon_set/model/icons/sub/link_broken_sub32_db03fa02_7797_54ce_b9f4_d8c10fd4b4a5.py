"""Independent 32px profile of link-broken.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'db03fa02-7797-54ce-b9f4-d8c10fd4b4a5'
SOURCE_PATH = 'pictographic-primitives/interface-essential/link broken_db03fa02-7797-54ce-b9f4-d8c10fd4b4a5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('db03fa02-7797-54ce-b9f4-d8c10fd4b4a5', 'pictographic-primitives/interface-essential/link broken_db03fa02-7797-54ce-b9f4-d8c10fd4b4a5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/link-broken',)
SOLO_SOURCE_ICON_IDS = ('link-broken',)
REFERENCE_EXPORT_SHA256 = '80e294c2ee1bcefe095796b4e3262b87a294657bd1638a3a2b04fcb29e95ef3b'

class Drawing(Sub32):
    icon_id = 'link-broken-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 12), ((18, 9), (20, 5), (22, 5)))
        self.add_bezier('p1-r1-2', (22, 5), ((25, 5), (27, 7), (27, 10)))
        self.add_bezier('p1-r1-3', (27, 10), ((27, 13), (24, 15), (21, 18)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_bezier('p2-r1-1', (10, 17), ((8, 20), (5, 23), (5, 26)))
        self.add_bezier('p2-r1-2', (5, 26), ((5, 29), (7, 30), (10, 30)))
        self.add_bezier('p2-r1-3', (10, 30), ((13, 30), (15, 26), (17, 24)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (10, 2), (10, 6))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (5, 11), (8, 11))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
