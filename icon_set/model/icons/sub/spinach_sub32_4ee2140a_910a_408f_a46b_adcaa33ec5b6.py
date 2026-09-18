"""Independent 32px profile of spinach.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4ee2140a-910a-408f-a46b-adcaa33ec5b6'
SOURCE_PATH = 'pictographic-primitives/symbol/spinach_4ee2140a-910a-408f-a46b-adcaa33ec5b6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4ee2140a-910a-408f-a46b-adcaa33ec5b6', 'pictographic-primitives/symbol/spinach_4ee2140a-910a-408f-a46b-adcaa33ec5b6.svg'),)
PROFILE_SOURCE_KEYS = ('solo/spinach',)
SOLO_SOURCE_ICON_IDS = ('spinach',)
REFERENCE_EXPORT_SHA256 = 'f5483bb9b0b7bc6f62582cef886a2d2905b0b161739395b38e0d301b9f0810dc'

class Drawing(Sub32):
    icon_id = 'spinach-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (17, 12), (8, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (8, 22), (10, 25))
        self.add_bezier('p2-r1-2', (10, 25), ((10, 25), (11, 25), (11, 25)))
        self.add_bezier('p2-r1-3', (11, 25), ((13, 25), (15, 25), (16, 25)))
        self.add_bezier('p2-r1-4', (16, 25), ((23, 24), (27, 19), (27, 14)))
        self.add_bezier('p2-r1-5', (27, 14), ((27, 13), (27, 13), (27, 13)))
        self.add_bezier('p2-r1-6', (27, 13), ((27, 13), (27, 12), (27, 12)))
        self.add_bezier('p2-r1-7', (27, 12), ((27, 10), (26, 6), (24, 4)))
        self.add_bezier('p2-r1-8', (24, 4), ((24, 3), (24, 3), (23, 2)))
        self.add_bezier('p2-r1-9', (23, 2), ((23, 2), (23, 2), (23, 2)))
        self.add_bezier('p2-r1-10', (23, 2), ((22, 2), (18, 4), (17, 4)))
        self.add_bezier('p2-r1-11', (17, 4), ((12, 6), (7, 9), (5, 13)))
        self.add_bezier('p2-r1-12', (5, 13), ((5, 14), (5, 15), (5, 16)))
        self.add_bezier('p2-r1-13', (5, 16), ((5, 16), (5, 16), (5, 16)))
        self.add_bezier('p2-r1-14', (5, 16), ((5, 16), (5, 16), (5, 17)))
        self.add_bezier('p2-r1-15', (5, 17), ((5, 18), (6, 21), (8, 22)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', 'p2-r1-11', 'p2-r1-12', 'p2-r1-13', 'p2-r1-14', 'p2-r1-15', closed=False)
