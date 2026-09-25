"""Independent 32px profile of transgender-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '5506bb6a-8955-4820-92f3-2aa260d6fd32'
SOURCE_PATH = 'pictographic-primitives/users/gender transgender_5506bb6a-8955-4820-92f3-2aa260d6fd32.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5506bb6a-8955-4820-92f3-2aa260d6fd32', 'pictographic-primitives/users/gender transgender_5506bb6a-8955-4820-92f3-2aa260d6fd32.svg'),)
PROFILE_SOURCE_KEYS = ('solo/transgender-symbol',)
SOLO_SOURCE_ICON_IDS = ('transgender-symbol',)
REFERENCE_EXPORT_SHA256 = '216190f5f7c5e561b34bbf5cc13af381d3693ff10f5b0faf536f7578e8b6ffac'

class Drawing(Sub32):
    icon_id = 'transgender-symbol-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'users'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (11, 11), (21, 11), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (21, 11), (16, 25), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (16, 25), (11, 11), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (11, 11), (7, 7))
        self.add_line('p2-r1-2', (7, 7), (2, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (21, 11), (30, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 7), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (7, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (25, 2), (30, 2))
        self.add_line('p5-r1-2', (30, 2), (30, 7))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (4, 11), (7, 7))
        self.add_line('p6-r1-2', (7, 7), (11, 4))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_line('p7-r1-1', (16, 25), (16, 30))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p7-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p7-r1-1')
        self.relate('connect', 'p2-r1-1', 'p6-r1-1')
        self.relate('connect', 'p2-r1-1', 'p6-r1-2')
        self.relate('connect', 'p2-r1-2', 'p4-r1-1')
        self.relate('connect', 'p2-r1-2', 'p4-r1-2')
        self.relate('connect', 'p2-r1-2', 'p6-r1-1')
        self.relate('connect', 'p2-r1-2', 'p6-r1-2')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-2')
