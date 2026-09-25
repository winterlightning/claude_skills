"""Independent 32px profile of pills-tablet-capsule.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e9e353dc-a7a8-4b37-b10f-58d242cf890c'
SOURCE_PATH = 'pictographic-primitives/symbol/two pill_e9e353dc-a7a8-4b37-b10f-58d242cf890c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e9e353dc-a7a8-4b37-b10f-58d242cf890c', 'pictographic-primitives/symbol/two pill_e9e353dc-a7a8-4b37-b10f-58d242cf890c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pills-tablet-capsule',)
SOLO_SOURCE_ICON_IDS = ('pills-tablet-capsule',)
REFERENCE_EXPORT_SHA256 = '24582887a93c3ff8634a2850c706b0d9df906d4a5e9423ab942afd8bb20a8dbf'

class Drawing(Sub32):
    icon_id = 'pills-tablet-capsule-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 8), ((2, 5), (5, 2), (8, 2)))
        self.add_bezier('p1-r1-2', (8, 2), ((12, 2), (14, 5), (14, 8)))
        self.add_bezier('p1-r1-3', (14, 8), ((14, 12), (12, 14), (8, 14)))
        self.add_bezier('p1-r1-4', (8, 14), ((5, 14), (2, 12), (2, 8)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, 8), (14, 8))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (14, 24), (18, 18))
        self.add_line('p3-r1-2', (18, 18), (23, 11))
        self.add_bezier('p3-r1-3', (23, 11), ((24, 10), (25, 10), (26, 10)))
        self.add_bezier('p3-r1-4', (26, 10), ((27, 10), (28, 10), (28, 11)))
        self.add_bezier('p3-r1-5', (28, 11), ((29, 11), (30, 12), (30, 14)))
        self.add_bezier('p3-r1-6', (30, 14), ((30, 14), (30, 15), (29, 16)))
        self.add_line('p3-r1-7', (29, 16), (25, 22))
        self.add_line('p3-r1-8', (25, 22), (20, 28))
        self.add_bezier('p3-r1-9', (20, 28), ((19, 29), (18, 30), (17, 30)))
        self.add_bezier('p3-r1-10', (17, 30), ((16, 30), (15, 30), (14, 29)))
        self.add_bezier('p3-r1-11', (14, 29), ((13, 28), (13, 27), (13, 26)))
        self.add_bezier('p3-r1-12', (13, 26), ((13, 25), (13, 24), (14, 24)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', 'p3-r1-9', 'p3-r1-10', 'p3-r1-11', 'p3-r1-12', closed=False)
        self.add_line('p4-r1-1', (18, 18), (25, 22))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-7', 'p4-r1-1')
        self.relate("connect", 'p3-r1-8', 'p4-r1-1')
