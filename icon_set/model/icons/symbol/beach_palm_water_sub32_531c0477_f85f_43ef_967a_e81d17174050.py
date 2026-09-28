"""Independent 32px profile of beach-palm-water.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '531c0477-f85f-43ef-967a-e81d17174050'
SOURCE_PATH = 'pictographic-primitives/recreation/beach palm water_531c0477-f85f-43ef-967a-e81d17174050.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('531c0477-f85f-43ef-967a-e81d17174050', 'pictographic-primitives/recreation/beach palm water_531c0477-f85f-43ef-967a-e81d17174050.svg'),)
PROFILE_SOURCE_KEYS = ('solo/beach-palm-water',)
SOLO_SOURCE_ICON_IDS = ('beach-palm-water',)
REFERENCE_EXPORT_SHA256 = 'e606b9ad00c6f5a2863de036f6880e419401b3402c42eb9493def12f72d53452'

class Drawing(Sub32):
    icon_id = 'beach-palm-water-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'recreation'
    categories = ('primitives', 'recreation')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (5, 16), ((5, 7), (13, 2), (20, 2)))
        self.add_bezier('p1-r1-2', (20, 2), ((23, 2), (25, 4), (27, 7)))
        self.add_line('p1-r1-3', (27, 7), (16, 11))
        self.add_line('p1-r1-4', (16, 11), (5, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (16, 11), (20, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (2, 30), ((4, 30), (4, 27), (7, 27)))
        self.add_bezier('p3-r1-2', (7, 27), ((9, 27), (9, 30), (11, 30)))
        self.add_bezier('p3-r1-3', (11, 30), ((14, 30), (14, 27), (16, 27)))
        self.add_bezier('p3-r1-4', (16, 27), ((18, 27), (18, 30), (21, 30)))
        self.add_bezier('p3-r1-5', (21, 30), ((23, 30), (23, 27), (25, 27)))
        self.add_bezier('p3-r1-6', (25, 27), ((28, 27), (28, 30), (30, 30)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
