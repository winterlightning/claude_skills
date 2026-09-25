"""Independent 32px profile of handshake.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '533cf846-1648-4bd0-a7f9-03a05d166f40'
SOURCE_PATH = 'pictographic-primitives/symbol/handshake_533cf846-1648-4bd0-a7f9-03a05d166f40.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('533cf846-1648-4bd0-a7f9-03a05d166f40', 'pictographic-primitives/symbol/handshake_533cf846-1648-4bd0-a7f9-03a05d166f40.svg'),)
PROFILE_SOURCE_KEYS = ('solo/handshake',)
SOLO_SOURCE_ICON_IDS = ('handshake',)
REFERENCE_EXPORT_SHA256 = '077c4f9d384671bb3528d64eee4262f2fd44507b57afb4c65bedd634b7fc51c5'

class Drawing(Sub32):
    icon_id = 'handshake-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (6, 9), (10, 5))
        self.add_line('p1-r1-2', (10, 5), (19, 5))
        self.add_line('p1-r1-3', (19, 5), (26, 9))
        self.add_line('p1-r1-4', (26, 9), (26, 19))
        self.add_line('p1-r1-5', (26, 19), (20, 22))
        self.add_line('p1-r1-6', (20, 22), (19, 26))
        self.add_line('p1-r1-7', (19, 26), (15, 27))
        self.add_line('p1-r1-8', (15, 27), (6, 19))
        self.add_line('p1-r1-9', (6, 19), (6, 9))
        self.add_line('p1-r1-10', (6, 9), (6, 9))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (2, 8), (6, 8))
        self.add_line('p2-r1-2', (6, 8), (6, 9))
        self.add_line('p2-r1-3', (6, 9), (6, 19))
        self.add_line('p2-r1-4', (6, 19), (6, 22))
        self.add_line('p2-r1-5', (6, 22), (2, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (30, 8), (26, 8))
        self.add_line('p3-r1-2', (26, 8), (26, 9))
        self.add_line('p3-r1-3', (26, 9), (26, 19))
        self.add_line('p3-r1-4', (26, 19), (26, 22))
        self.add_line('p3-r1-5', (26, 22), (30, 22))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (19, 5), (13, 12))
        self.add_arc('p4-r1-2', (13, 12), (16, 16), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p4-r1-3', (16, 16), (20, 15))
        self.add_line('p4-r1-4', (20, 15), (20, 22))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-2')
        self.relate('connect', 'p1-r1-3', 'p3-r1-3')
        self.relate('connect', 'p1-r1-3', 'p4-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-2')
        self.relate('connect', 'p1-r1-4', 'p3-r1-3')
        self.relate('connect', 'p1-r1-4', 'p3-r1-4')
        self.relate('connect', 'p1-r1-5', 'p3-r1-3')
        self.relate('connect', 'p1-r1-5', 'p3-r1-4')
        self.relate('connect', 'p1-r1-5', 'p4-r1-4')
        self.relate('connect', 'p1-r1-6', 'p4-r1-4')
        self.relate('connect', 'p1-r1-8', 'p2-r1-3')
        self.relate('connect', 'p1-r1-8', 'p2-r1-4')
        self.relate('connect', 'p1-r1-9', 'p2-r1-2')
        self.relate('connect', 'p1-r1-9', 'p2-r1-3')
        self.relate('connect', 'p1-r1-9', 'p2-r1-4')
        self.relate('connect', 'p1-r1-10', 'p2-r1-2')
        self.relate('connect', 'p1-r1-10', 'p2-r1-3')
