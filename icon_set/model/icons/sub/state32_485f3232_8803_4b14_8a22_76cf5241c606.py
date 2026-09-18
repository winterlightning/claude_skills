"""Independent 32px profile of state32-485f3232-8803-4b14-8a22-76cf5241c606.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '485f3232-8803-4b14-8a22-76cf5241c606'
SOURCE_PATH = 'icon_set/assets/combination-state32/485f3232-8803-4b14-8a22-76cf5241c606.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('485f3232-8803-4b14-8a22-76cf5241c606', 'icon_set/assets/combination-state32/485f3232-8803-4b14-8a22-76cf5241c606.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '36c6cca73b4b01360081807e6272832da57eedae4e81364402721716a1fcc9b1'

class Drawing(Sub32):
    icon_id = 'state32-485f3232-8803-4b14-8a22-76cf5241c606'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (3, 2), (9, 2))
        self.add_bezier('p1-r1-2', (9, 2), ((11, 2), (11, 4), (11, 5)))
        self.add_bezier('p1-r1-3', (11, 5), ((11, 6), (11, 6), (10, 7)))
        self.add_line('p1-r1-4', (10, 7), (5, 11))
        self.add_bezier('p1-r1-5', (5, 11), ((4, 12), (3, 13), (3, 14)))
        self.add_line('p1-r1-6', (3, 14), (3, 14))
        self.add_bezier('p1-r1-7', (3, 14), ((3, 14), (3, 15), (4, 15)))
        self.add_line('p1-r1-8', (4, 15), (11, 15))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (17, 15), (17, 2))
        self.add_line('p2-r1-2', (17, 2), (23, 10))
        self.add_line('p2-r1-3', (23, 10), (29, 2))
        self.add_line('p2-r1-4', (29, 2), (29, 15))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 25), (30, 25))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p3-r2-1', (7, 20), (2, 25))
        self.add_line('p3-r2-2', (2, 25), (7, 30))
        self.add_contour('path-3-2', 'p3-r2-1', 'p3-r2-2', closed=False)
        self.add_line('p3-r3-1', (25, 20), (30, 25))
        self.add_line('p3-r3-2', (30, 25), (25, 30))
        self.add_contour('path-3-3', 'p3-r3-1', 'p3-r3-2', closed=False)
        self.relate("connect", 'p3-r1-1', 'p3-r2-1')
        self.relate("connect", 'p3-r1-1', 'p3-r2-2')
        self.relate("connect", 'p3-r1-1', 'p3-r3-1')
        self.relate("connect", 'p3-r1-1', 'p3-r3-2')
