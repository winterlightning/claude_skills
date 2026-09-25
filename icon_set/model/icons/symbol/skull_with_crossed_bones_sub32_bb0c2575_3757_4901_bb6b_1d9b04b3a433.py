"""Independent 32px profile of skull-with-crossed-bones.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'bb0c2575-3757-4901-bb6b-1d9b04b3a433'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/skull_bb0c2575-3757-4901-bb6b-1d9b04b3a433.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bb0c2575-3757-4901-bb6b-1d9b04b3a433', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/skull_bb0c2575-3757-4901-bb6b-1d9b04b3a433.svg'),)
PROFILE_SOURCE_KEYS = ('solo/skull-with-crossed-bones',)
SOLO_SOURCE_ICON_IDS = ('skull-with-crossed-bones',)
REFERENCE_EXPORT_SHA256 = '331dbcf163d11adc08d6e034c1269b8832cdd30964e245bf432d937a1340d2ab'

class Drawing(Sub32):
    icon_id = 'skull-with-crossed-bones-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (8, 8), ((10, 6), (13, 5), (16, 5)))
        self.add_bezier('p1-r1-2', (16, 5), ((19, 5), (22, 6), (24, 8)))
        self.add_bezier('p1-r1-3', (24, 8), ((25, 10), (26, 13), (26, 16)))
        self.add_bezier('p1-r1-4', (26, 16), ((26, 18), (25, 21), (22, 22)))
        self.add_line('p1-r1-5', (22, 22), (22, 27))
        self.add_line('p1-r1-6', (22, 27), (16, 27))
        self.add_line('p1-r1-7', (16, 27), (10, 27))
        self.add_line('p1-r1-8', (10, 27), (10, 22))
        self.add_bezier('p1-r1-9', (10, 22), ((7, 21), (5, 18), (5, 16)))
        self.add_bezier('p1-r1-10', (5, 16), ((5, 13), (7, 10), (8, 8)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (12, 15), (12, 15))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (8, 8), (2, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (10, 22), (2, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (20, 15), (20, 15))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (24, 8), (30, 2))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (22, 22), (30, 30))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (16, 21), (16, 27))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p6-r1-1')
        self.relate('connect', 'p1-r1-3', 'p6-r1-1')
        self.relate('connect', 'p1-r1-4', 'p7-r1-1')
        self.relate('connect', 'p1-r1-5', 'p7-r1-1')
        self.relate('connect', 'p1-r1-6', 'p8-r1-1')
        self.relate('connect', 'p1-r1-7', 'p8-r1-1')
        self.relate('connect', 'p1-r1-8', 'p4-r1-1')
        self.relate('connect', 'p1-r1-9', 'p4-r1-1')
        self.relate('connect', 'p1-r1-10', 'p3-r1-1')
