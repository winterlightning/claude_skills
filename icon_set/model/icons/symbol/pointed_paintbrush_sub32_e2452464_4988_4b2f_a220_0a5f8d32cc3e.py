"""Independent 32px profile of pointed-paintbrush.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'e2452464-4988-4b2f-a220-0a5f8d32cc3e'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/brush_e2452464-4988-4b2f-a220-0a5f8d32cc3e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e2452464-4988-4b2f-a220-0a5f8d32cc3e', 'pictographic-primitives/decoration/batch-01/brush_e2452464-4988-4b2f-a220-0a5f8d32cc3e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pointed-paintbrush',)
SOLO_SOURCE_ICON_IDS = ('pointed-paintbrush',)
REFERENCE_EXPORT_SHA256 = 'c08360479dd7b1b10a838fb970123073510b81133fec70f30615988d16ed0729'

class Drawing(Sub32):
    icon_id = 'pointed-paintbrush-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/decoration'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 12), (24, 3))
        self.add_bezier('p1-r1-2', (24, 3), ((24, 2), (25, 2), (26, 2)))
        self.add_bezier('p1-r1-3', (26, 2), ((27, 2), (28, 3), (29, 4)))
        self.add_bezier('p1-r1-4', (29, 4), ((30, 4), (30, 5), (30, 6)))
        self.add_bezier('p1-r1-5', (30, 6), ((30, 7), (29, 8), (28, 9)))
        self.add_line('p1-r1-6', (28, 9), (16, 18))
        self.add_line('p1-r1-7', (16, 18), (11, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_bezier('p2-r1-1', (11, 12), ((9, 13), (7, 14), (6, 16)))
        self.add_bezier('p2-r1-2', (6, 16), ((4, 18), (4, 20), (4, 22)))
        self.add_line('p2-r1-3', (4, 22), (2, 30))
        self.add_line('p2-r1-4', (2, 30), (14, 30))
        self.add_bezier('p2-r1-5', (14, 30), ((16, 28), (16, 26), (17, 24)))
        self.add_bezier('p2-r1-6', (17, 24), ((17, 24), (17, 23), (17, 23)))
        self.add_bezier('p2-r1-7', (17, 23), ((17, 21), (17, 20), (16, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-7')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-7')
