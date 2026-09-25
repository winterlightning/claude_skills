"""Independent 32px profile of diagonal-dna-helix-with-end-rungs.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '0f8bad55-2188-449b-86bc-2964af338a2e'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/dna_0f8bad55-2188-449b-86bc-2964af338a2e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0f8bad55-2188-449b-86bc-2964af338a2e', 'pictographic-primitives/artificial-intelligence/dna_0f8bad55-2188-449b-86bc-2964af338a2e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/diagonal-dna-helix-with-end-rungs',)
SOLO_SOURCE_ICON_IDS = ('diagonal-dna-helix-with-end-rungs',)
REFERENCE_EXPORT_SHA256 = 'f6268bd9b2ed31030db06aec05daf019e46d4744683b61f74a2f78b68935fab6'

class Drawing(Sub32):
    icon_id = 'diagonal-dna-helix-with-end-rungs-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 21), ((4, 19), (5, 18), (7, 18)))
        self.add_bezier('p1-r1-2', (7, 18), ((8, 18), (10, 19), (11, 21)))
        self.add_bezier('p1-r1-3', (11, 21), ((13, 22), (14, 23), (16, 23)))
        self.add_bezier('p1-r1-4', (16, 23), ((18, 23), (19, 22), (21, 21)))
        self.add_bezier('p1-r1-5', (21, 21), ((22, 19), (23, 18), (23, 16)))
        self.add_bezier('p1-r1-6', (23, 16), ((23, 14), (22, 13), (21, 11)))
        self.add_bezier('p1-r1-7', (21, 11), ((19, 10), (18, 8), (18, 7)))
        self.add_bezier('p1-r1-8', (18, 7), ((18, 5), (19, 4), (21, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_bezier('p2-r1-1', (11, 30), ((13, 28), (14, 27), (14, 25)))
        self.add_bezier('p2-r1-2', (14, 25), ((14, 24), (13, 22), (11, 21)))
        self.add_bezier('p2-r1-3', (11, 21), ((10, 19), (9, 18), (9, 16)))
        self.add_bezier('p2-r1-4', (9, 16), ((9, 14), (10, 13), (11, 11)))
        self.add_bezier('p2-r1-5', (11, 11), ((13, 10), (14, 9), (16, 9)))
        self.add_bezier('p2-r1-6', (16, 9), ((18, 9), (19, 10), (21, 11)))
        self.add_bezier('p2-r1-7', (21, 11), ((22, 13), (24, 14), (25, 14)))
        self.add_bezier('p2-r1-8', (25, 14), ((27, 14), (28, 13), (30, 11)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
        self.add_line('p3-r1-1', (2, 21), (11, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (21, 2), (30, 11))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-3')
        self.relate('connect', 'p1-r1-6', 'p2-r1-6')
        self.relate('connect', 'p1-r1-6', 'p2-r1-7')
        self.relate('connect', 'p1-r1-7', 'p2-r1-6')
        self.relate('connect', 'p1-r1-7', 'p2-r1-7')
        self.relate('connect', 'p1-r1-8', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-8', 'p4-r1-1')
