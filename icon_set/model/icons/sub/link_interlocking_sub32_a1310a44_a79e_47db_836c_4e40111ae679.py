"""Independent 32px profile of link-interlocking.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a1310a44-a79e-47db-836c-4e40111ae679'
SOURCE_PATH = 'pictographic-primitives/symbol/link_a1310a44-a79e-47db-836c-4e40111ae679.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a1310a44-a79e-47db-836c-4e40111ae679', 'pictographic-primitives/symbol/link_a1310a44-a79e-47db-836c-4e40111ae679.svg'),)
PROFILE_SOURCE_KEYS = ('solo/link-interlocking',)
SOLO_SOURCE_ICON_IDS = ('link-interlocking',)
REFERENCE_EXPORT_SHA256 = 'b153cd513d76822057a281f590fe026c25080249bcd1fc3605a230c69b119a1a'

class Drawing(Sub32):
    icon_id = 'link-interlocking-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 8), (16, 5))
        self.add_bezier('p1-r1-2', (16, 5), ((18, 3), (20, 2), (22, 2)))
        self.add_bezier('p1-r1-3', (22, 2), ((24, 2), (26, 3), (27, 4)))
        self.add_bezier('p1-r1-4', (27, 4), ((29, 5), (30, 7), (30, 10)))
        self.add_bezier('p1-r1-5', (30, 10), ((30, 11), (29, 13), (28, 14)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (7, 14), (4, 18))
        self.add_bezier('p2-r1-2', (4, 18), ((3, 19), (2, 21), (2, 22)))
        self.add_bezier('p2-r1-3', (2, 22), ((2, 25), (3, 27), (5, 28)))
        self.add_bezier('p2-r1-4', (5, 28), ((6, 29), (8, 30), (10, 30)))
        self.add_bezier('p2-r1-5', (10, 30), ((12, 30), (14, 29), (16, 27)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (11, 21), (21, 11))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
