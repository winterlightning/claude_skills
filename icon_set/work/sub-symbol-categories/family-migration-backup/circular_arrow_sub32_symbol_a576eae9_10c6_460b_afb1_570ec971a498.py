# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of circular-arrow.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'a576eae9-10c6-460b-afb1-570ec971a498'
SOURCE_PATH = 'pictographic-primitives/state/circular arrow_a576eae9-10c6-460b-afb1-570ec971a498.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a576eae9-10c6-460b-afb1-570ec971a498', 'pictographic-primitives/state/circular arrow_a576eae9-10c6-460b-afb1-570ec971a498.svg'), ('b4e2a04a-d4a8-40d4-a5ea-cc2cb10d5181', 'pictographic-primitives/symbol/arrow circular_b4e2a04a-d4a8-40d4-a5ea-cc2cb10d5181.svg'))
PROFILE_SOURCE_KEYS = ('solo/circular-arrow', 'solo/arrow-circular-clockwise')
SOLO_SOURCE_ICON_IDS = ('circular-arrow', 'arrow-circular-clockwise')
REFERENCE_EXPORT_SHA256 = '3acaee60a2be8c5d38e9e9793cc61a39ece86d1d41456eaa64458fa8bbb20506'

class DrawingContainerSymbol(Sub32):
    icon_id = 'circular-arrow-sub32-symbol'
    variant_of = 'circular-arrow-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/circular-arrow-sub32'
    counterpart_icon_id = 'circular-arrow-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (29, 9), (25, 6))
        self.add_bezier('p1-r1-2', (25, 6), ((25, 5), (24, 5), (23, 4)))
        self.add_bezier('p1-r1-3', (23, 4), ((21, 3), (19, 2), (17, 2)))
        self.add_bezier('p1-r1-4', (17, 2), ((16, 2), (16, 2), (16, 2)))
        self.add_bezier('p1-r1-5', (16, 2), ((16, 2), (15, 2), (15, 2)))
        self.add_bezier('p1-r1-6', (15, 2), ((14, 2), (13, 2), (12, 3)))
        self.add_bezier('p1-r1-7', (12, 3), ((8, 4), (5, 7), (3, 10)))
        self.add_bezier('p1-r1-8', (3, 10), ((2, 12), (2, 13), (2, 15)))
        self.add_bezier('p1-r1-9', (2, 15), ((2, 15), (2, 15), (2, 15)))
        self.add_bezier('p1-r1-10', (2, 15), ((2, 16), (2, 16), (2, 16)))
        self.add_bezier('p1-r1-11', (2, 16), ((2, 22), (6, 27), (11, 29)))
        self.add_bezier('p1-r1-12', (11, 29), ((13, 30), (14, 30), (15, 30)))
        self.add_bezier('p1-r1-13', (15, 30), ((16, 30), (16, 30), (16, 30)))
        self.add_bezier('p1-r1-14', (16, 30), ((16, 30), (17, 30), (17, 30)))
        self.add_bezier('p1-r1-15', (17, 30), ((21, 30), (26, 27), (28, 23)))
        self.add_bezier('p1-r1-16', (28, 23), ((28, 23), (28, 22), (28, 21)))
        self.add_line('p1-r1-17', (28, 21), (30, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', closed=False)
        self.add_line('p2-r1-1', (22, 10), (29, 10))
        self.add_line('p2-r1-2', (29, 10), (29, 3))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
