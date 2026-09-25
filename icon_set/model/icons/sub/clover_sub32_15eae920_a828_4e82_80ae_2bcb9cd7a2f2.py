"""Independent 32px profile of clover.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '15eae920-a828-4e82-80ae-2bcb9cd7a2f2'
SOURCE_PATH = 'pictographic-primitives/state/clover_15eae920-a828-4e82-80ae-2bcb9cd7a2f2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('15eae920-a828-4e82-80ae-2bcb9cd7a2f2', 'pictographic-primitives/state/clover_15eae920-a828-4e82-80ae-2bcb9cd7a2f2.svg'), ('36097aaf-e256-48a1-aaeb-0f09bc96bc72', 'pictographic-primitives/symbol/clover_36097aaf-e256-48a1-aaeb-0f09bc96bc72.svg'))
PROFILE_SOURCE_KEYS = ('solo/clover', 'solo/clover-symbol')
SOLO_SOURCE_ICON_IDS = ('clover', 'clover-symbol')
REFERENCE_EXPORT_SHA256 = '1b109757499259458248590e04c7395bdc46e2dab7a938fb20e9d043905799ee'

class Drawing(Sub32):
    icon_id = 'clover-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 16), (8, 8))
        self.add_bezier('p1-r1-2', (8, 8), ((8, 4), (9, 2), (12, 2)))
        self.add_bezier('p1-r1-3', (12, 2), ((14, 2), (15, 4), (16, 4)))
        self.add_bezier('p1-r1-4', (16, 4), ((17, 4), (18, 2), (20, 2)))
        self.add_bezier('p1-r1-5', (20, 2), ((23, 2), (24, 4), (24, 8)))
        self.add_line('p1-r1-6', (24, 8), (16, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (16, 16), (24, 8))
        self.add_bezier('p2-r1-2', (24, 8), ((28, 8), (30, 9), (30, 12)))
        self.add_bezier('p2-r1-3', (30, 12), ((30, 14), (28, 15), (28, 16)))
        self.add_bezier('p2-r1-4', (28, 16), ((28, 17), (30, 18), (30, 20)))
        self.add_bezier('p2-r1-5', (30, 20), ((30, 23), (28, 24), (24, 24)))
        self.add_line('p2-r1-6', (24, 24), (16, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (16, 16), (24, 24))
        self.add_bezier('p3-r1-2', (24, 24), ((24, 28), (23, 30), (20, 30)))
        self.add_bezier('p3-r1-3', (20, 30), ((18, 30), (17, 28), (16, 28)))
        self.add_bezier('p3-r1-4', (16, 28), ((15, 28), (14, 30), (12, 30)))
        self.add_bezier('p3-r1-5', (12, 30), ((9, 30), (8, 28), (8, 24)))
        self.add_line('p3-r1-6', (8, 24), (16, 16))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.add_line('p4-r1-1', (16, 16), (8, 24))
        self.add_bezier('p4-r1-2', (8, 24), ((4, 24), (2, 23), (2, 20)))
        self.add_bezier('p4-r1-3', (2, 20), ((2, 18), (4, 17), (4, 16)))
        self.add_bezier('p4-r1-4', (4, 16), ((4, 15), (2, 14), (2, 12)))
        self.add_bezier('p4-r1-5', (2, 12), ((2, 9), (4, 8), (8, 8)))
        self.add_line('p4-r1-6', (8, 8), (16, 16))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-6')
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-1', 'p3-r1-6')
        self.relate("connect", 'p1-r1-1', 'p4-r1-1')
        self.relate("connect", 'p1-r1-1', 'p4-r1-5')
        self.relate("connect", 'p1-r1-1', 'p4-r1-6')
        self.relate("connect", 'p1-r1-2', 'p4-r1-5')
        self.relate("connect", 'p1-r1-2', 'p4-r1-6')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-2')
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-2')
        self.relate("connect", 'p1-r1-6', 'p2-r1-6')
        self.relate("connect", 'p1-r1-6', 'p3-r1-1')
        self.relate("connect", 'p1-r1-6', 'p3-r1-6')
        self.relate("connect", 'p1-r1-6', 'p4-r1-1')
        self.relate("connect", 'p1-r1-6', 'p4-r1-6')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-6')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-6')
        self.relate("connect", 'p2-r1-5', 'p3-r1-1')
        self.relate("connect", 'p2-r1-5', 'p3-r1-2')
        self.relate("connect", 'p2-r1-6', 'p3-r1-1')
        self.relate("connect", 'p2-r1-6', 'p3-r1-2')
        self.relate("connect", 'p2-r1-6', 'p3-r1-6')
        self.relate("connect", 'p2-r1-6', 'p4-r1-1')
        self.relate("connect", 'p2-r1-6', 'p4-r1-6')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-6')
        self.relate("connect", 'p3-r1-5', 'p4-r1-1')
        self.relate("connect", 'p3-r1-5', 'p4-r1-2')
        self.relate("connect", 'p3-r1-6', 'p4-r1-1')
        self.relate("connect", 'p3-r1-6', 'p4-r1-2')
        self.relate("connect", 'p3-r1-6', 'p4-r1-6')
