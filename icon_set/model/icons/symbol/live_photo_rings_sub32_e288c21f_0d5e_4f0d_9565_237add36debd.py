"""Independent 32px profile of live-photo-rings.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'e288c21f-0d5e-4f0d-9565-237add36debd'
SOURCE_PATH = 'pictographic-primitives/photography/live photos_e288c21f-0d5e-4f0d-9565-237add36debd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e288c21f-0d5e-4f0d-9565-237add36debd', 'pictographic-primitives/photography/live photos_e288c21f-0d5e-4f0d-9565-237add36debd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/live-photo-rings',)
SOLO_SOURCE_ICON_IDS = ('live-photo-rings',)
REFERENCE_EXPORT_SHA256 = 'c532fbe65507627003601d1fcf8c7610e2f97317602400c94c91ebbac3d9ca01'

class Drawing(Sub32):
    icon_id = 'live-photo-rings-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'photography'
    categories = ('photography', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (12, 3), ((13, 2), (15, 2), (16, 2)))
        self.add_bezier('p1-r1-2', (16, 2), ((17, 2), (19, 2), (20, 3)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (29, 12), ((30, 13), (30, 15), (30, 16)))
        self.add_bezier('p2-r1-2', (30, 16), ((30, 17), (30, 19), (29, 20)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (20, 29), ((19, 30), (17, 30), (16, 30)))
        self.add_bezier('p3-r1-2', (16, 30), ((15, 30), (13, 30), (12, 29)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_bezier('p4-r1-1', (3, 20), ((2, 19), (2, 17), (2, 16)))
        self.add_bezier('p4-r1-2', (2, 16), ((2, 15), (2, 13), (3, 12)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_bezier('p5-r1-1', (9, 16), ((9, 12), (12, 9), (16, 9)))
        self.add_bezier('p5-r1-2', (16, 9), ((20, 9), (23, 12), (23, 16)))
        self.add_bezier('p5-r1-3', (23, 16), ((23, 20), (20, 23), (16, 23)))
        self.add_bezier('p5-r1-4', (16, 23), ((12, 23), (9, 20), (9, 16)))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
        self.add_line('p6-r1-1', (16, 16), (16, 16))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
