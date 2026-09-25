"""Independent 32px profile of hairpin-turn-right.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3fe88fdd-16b8-494f-b26e-461659c58008'
SOURCE_PATH = 'pictographic-primitives/transportation/hairpin turn right_3fe88fdd-16b8-494f-b26e-461659c58008.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3fe88fdd-16b8-494f-b26e-461659c58008', 'pictographic-primitives/transportation/hairpin turn right_3fe88fdd-16b8-494f-b26e-461659c58008.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hairpin-turn-right',)
SOLO_SOURCE_ICON_IDS = ('hairpin-turn-right',)
REFERENCE_EXPORT_SHA256 = '1857ef5f72b9e24b5cb1768d986c1d83331ef5fe8615435393320a80f666c8a9'

class Drawing(Sub32):
    icon_id = 'hairpin-turn-right-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'transportation'
    categories = ('transportation', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (18, 17), (23, 23))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (23, 23), (27, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (23, 23), (23, 12))
        self.add_bezier('p3-r1-2', (23, 12), ((23, 11), (23, 10), (23, 9)))
        self.add_bezier('p3-r1-3', (23, 9), ((21, 5), (18, 2), (14, 2)))
        self.add_bezier('p3-r1-4', (14, 2), ((14, 2), (14, 2), (14, 2)))
        self.add_bezier('p3-r1-5', (14, 2), ((12, 2), (11, 2), (10, 3)))
        self.add_bezier('p3-r1-6', (10, 3), ((7, 5), (5, 8), (5, 12)))
        self.add_bezier('p3-r1-7', (5, 12), ((5, 12), (5, 12), (5, 13)))
        self.add_line('p3-r1-8', (5, 13), (5, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
