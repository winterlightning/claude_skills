"""Independent 32px profile of ice-skate-boot.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '727add99-ce34-4828-932a-d2567ed13149'
SOURCE_PATH = 'pictographic-primitives/symbol/skate ice_727add99-ce34-4828-932a-d2567ed13149.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('727add99-ce34-4828-932a-d2567ed13149', 'pictographic-primitives/symbol/skate ice_727add99-ce34-4828-932a-d2567ed13149.svg'),)
PROFILE_SOURCE_KEYS = ('solo/ice-skate-boot',)
SOLO_SOURCE_ICON_IDS = ('ice-skate-boot',)
REFERENCE_EXPORT_SHA256 = '2872a9220f2385bfba19b677c720df7e63305766b37321ebfb124849a54bd444'

class Drawing(Sub32):
    icon_id = 'ice-skate-boot-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 5), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (16, 11))
        self.add_arc('p1-r1-3', (16, 11), (21, 16), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('p1-r1-4', (21, 16), (25, 21), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (25, 21), (22, 21))
        self.add_line('p1-r1-6', (22, 21), (11, 21))
        self.add_line('p1-r1-7', (11, 21), (5, 21))
        self.add_line('p1-r1-8', (5, 21), (5, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (2, 30), (11, 30))
        self.add_line('p2-r1-2', (11, 30), (22, 30))
        self.add_line('p2-r1-3', (22, 30), (25, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_arc('p3-r1-1', (25, 30), (30, 25), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (11, 21), (11, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (22, 21), (22, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p1-r1-5', 'p5-r1-1')
        self.relate("connect", 'p1-r1-6', 'p4-r1-1')
        self.relate("connect", 'p1-r1-6', 'p5-r1-1')
        self.relate("connect", 'p1-r1-7', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-2', 'p4-r1-1')
        self.relate("connect", 'p2-r1-2', 'p5-r1-1')
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
        self.relate("connect", 'p2-r1-3', 'p5-r1-1')
