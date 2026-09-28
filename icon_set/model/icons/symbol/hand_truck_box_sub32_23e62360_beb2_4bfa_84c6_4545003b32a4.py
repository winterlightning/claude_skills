"""Independent 32px profile of hand-truck-box.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '23e62360-beb2-4bfa-84c6-4545003b32a4'
SOURCE_PATH = 'pictographic-primitives/symbol/logistic_23e62360-beb2-4bfa-84c6-4545003b32a4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('23e62360-beb2-4bfa-84c6-4545003b32a4', 'pictographic-primitives/symbol/logistic_23e62360-beb2-4bfa-84c6-4545003b32a4.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hand-truck-box',)
SOLO_SOURCE_ICON_IDS = ('hand-truck-box',)
REFERENCE_EXPORT_SHA256 = '3fc4a2044b65106ecba6e921fd7ad6e2626201746b4eee81c872d7171e5d9afb'

class Drawing(Sub32):
    icon_id = 'hand-truck-box-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (9, 22), ((11, 22), (13, 24), (13, 26)))
        self.add_bezier('p1-r1-2', (13, 26), ((13, 29), (11, 30), (9, 30)))
        self.add_bezier('p1-r1-3', (9, 30), ((7, 30), (5, 29), (5, 26)))
        self.add_bezier('p1-r1-4', (5, 26), ((5, 24), (7, 22), (9, 22)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (5, 2), (6, 2))
        self.add_bezier('p2-r1-2', (6, 2), ((7, 2), (8, 3), (9, 3)))
        self.add_line('p2-r1-3', (9, 3), (9, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (20, 26), (20, 10))
        self.add_line('p3-r1-2', (20, 10), (27, 10))
        self.add_line('p3-r1-3', (27, 10), (27, 26))
        self.add_line('p3-r1-4', (27, 26), (20, 26))
        self.add_line('p3-r1-5', (20, 26), (20, 26))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (13, 26), (19, 26))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-3')
