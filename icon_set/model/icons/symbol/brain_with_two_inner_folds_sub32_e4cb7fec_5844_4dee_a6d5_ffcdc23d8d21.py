"""Independent 32px profile of brain-with-two-inner-folds.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'e4cb7fec-5844-4dee-a6d5-ffcdc23d8d21'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/brain_e4cb7fec-5844-4dee-a6d5-ffcdc23d8d21.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e4cb7fec-5844-4dee-a6d5-ffcdc23d8d21', 'pictographic-primitives/artificial-intelligence/brain_e4cb7fec-5844-4dee-a6d5-ffcdc23d8d21.svg'),)
PROFILE_SOURCE_KEYS = ('solo/brain-with-two-inner-folds',)
SOLO_SOURCE_ICON_IDS = ('brain-with-two-inner-folds',)
REFERENCE_EXPORT_SHA256 = '4a9791de607bcaa9907ce0b7ee0ac7ed47e5558b1979956d781234898d0ae0b8'

class Drawing(Sub32):
    icon_id = 'brain-with-two-inner-folds-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'artificial-intelligence'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 5), ((14, 2), (13, 2), (10, 2)))
        self.add_bezier('p1-r1-2', (10, 2), ((10, 2), (10, 2), (10, 2)))
        self.add_bezier('p1-r1-3', (10, 2), ((5, 2), (4, 5), (4, 8)))
        self.add_bezier('p1-r1-4', (4, 8), ((2, 10), (2, 13), (2, 16)))
        self.add_bezier('p1-r1-5', (2, 16), ((2, 19), (2, 22), (4, 24)))
        self.add_bezier('p1-r1-6', (4, 24), ((4, 27), (5, 30), (10, 30)))
        self.add_bezier('p1-r1-7', (10, 30), ((13, 30), (14, 30), (16, 27)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_bezier('p2-r1-1', (16, 5), ((18, 2), (19, 2), (22, 2)))
        self.add_bezier('p2-r1-2', (22, 2), ((22, 2), (22, 2), (22, 2)))
        self.add_bezier('p2-r1-3', (22, 2), ((27, 2), (28, 5), (28, 8)))
        self.add_bezier('p2-r1-4', (28, 8), ((30, 10), (30, 13), (30, 16)))
        self.add_bezier('p2-r1-5', (30, 16), ((30, 19), (30, 22), (28, 24)))
        self.add_bezier('p2-r1-6', (28, 24), ((28, 27), (27, 30), (22, 30)))
        self.add_bezier('p2-r1-7', (22, 30), ((19, 30), (18, 30), (16, 27)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_line('p3-r1-1', (16, 5), (16, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_bezier('p4-r1-1', (4, 8), ((4, 12), (6, 14), (9, 14)))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_bezier('p5-r1-1', (23, 14), ((23, 14), (24, 14), (24, 15)))
        self.add_bezier('p5-r1-2', (24, 15), ((24, 16), (23, 18), (23, 18)))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p4-r1-1')
        self.relate('connect', 'p1-r1-4', 'p4-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-7')
        self.relate('connect', 'p1-r1-7', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-7', 'p3-r1-1')
