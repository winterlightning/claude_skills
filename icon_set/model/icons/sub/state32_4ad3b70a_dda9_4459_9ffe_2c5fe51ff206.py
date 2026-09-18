"""Independent 32px profile of state32-4ad3b70a-dda9-4459-9ffe-2c5fe51ff206.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4ad3b70a-dda9-4459-9ffe-2c5fe51ff206'
SOURCE_PATH = 'icon_set/assets/combination-state32/4ad3b70a-dda9-4459-9ffe-2c5fe51ff206.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4ad3b70a-dda9-4459-9ffe-2c5fe51ff206', 'icon_set/assets/combination-state32/4ad3b70a-dda9-4459-9ffe-2c5fe51ff206.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '82ab85df570f71cfaeaa34e8852108cae95413ddef18f65a9dd82e1f3a064d7f'

class Drawing(Sub32):
    icon_id = 'state32-4ad3b70a-dda9-4459-9ffe-2c5fe51ff206'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (3, 3), (9, 3))
        self.add_bezier('p1-r1-2', (9, 3), ((10, 3), (11, 4), (11, 5)))
        self.add_bezier('p1-r1-3', (11, 5), ((11, 6), (11, 6), (10, 7)))
        self.add_line('p1-r1-4', (10, 7), (4, 11))
        self.add_bezier('p1-r1-5', (4, 11), ((4, 11), (3, 12), (3, 14)))
        self.add_line('p1-r1-6', (3, 14), (3, 14))
        self.add_bezier('p1-r1-7', (3, 14), ((3, 14), (3, 14), (4, 14)))
        self.add_line('p1-r1-8', (4, 14), (11, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (23, 7), (23, 13))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (17, 13), (17, 7))
        self.add_bezier('p3-r1-2', (17, 7), ((17, 6), (19, 4), (20, 4)))
        self.add_bezier('p3-r1-3', (20, 4), ((22, 4), (23, 6), (23, 7)))
        self.add_bezier('p3-r1-4', (23, 7), ((23, 6), (24, 4), (26, 4)))
        self.add_bezier('p3-r1-5', (26, 4), ((28, 4), (29, 6), (29, 7)))
        self.add_line('p3-r1-6', (29, 7), (29, 13))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.add_line('p4-r1-1', (2, 24), (30, 24))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p4-r2-1', (7, 19), (2, 24))
        self.add_line('p4-r2-2', (2, 24), (7, 29))
        self.add_contour('path-4-2', 'p4-r2-1', 'p4-r2-2', closed=False)
        self.add_line('p4-r3-1', (25, 19), (30, 24))
        self.add_line('p4-r3-2', (30, 24), (25, 29))
        self.add_contour('path-4-3', 'p4-r3-1', 'p4-r3-2', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-3')
        self.relate("connect", 'p2-r1-1', 'p3-r1-4')
        self.relate("connect", 'p4-r1-1', 'p4-r2-1')
        self.relate("connect", 'p4-r1-1', 'p4-r2-2')
        self.relate("connect", 'p4-r1-1', 'p4-r3-1')
        self.relate("connect", 'p4-r1-1', 'p4-r3-2')
