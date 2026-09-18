"""Independent 32px profile of state32-00d83c6d-7ad8-492b-9d49-4bc79c61758b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '00d83c6d-7ad8-492b-9d49-4bc79c61758b'
SOURCE_PATH = 'icon_set/assets/combination-state32/00d83c6d-7ad8-492b-9d49-4bc79c61758b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('00d83c6d-7ad8-492b-9d49-4bc79c61758b', 'icon_set/assets/combination-state32/00d83c6d-7ad8-492b-9d49-4bc79c61758b.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '270644c5b67465bc14c379ac68f34c67e9bef897b4bdb1c2d8576ec6faf7a340'

class Drawing(Sub32):
    icon_id = 'state32-00d83c6d-7ad8-492b-9d49-4bc79c61758b'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (8, 8), ((9, 6), (10, 6), (11, 6)))
        self.add_bezier('p1-r1-2', (11, 6), ((13, 6), (15, 7), (16, 9)))
        self.add_bezier('p1-r1-3', (16, 9), ((18, 7), (20, 6), (22, 6)))
        self.add_bezier('p1-r1-4', (22, 6), ((26, 6), (29, 9), (29, 12)))
        self.add_bezier('p1-r1-5', (29, 12), ((29, 14), (28, 16), (27, 17)))
        self.add_line('p1-r1-6', (27, 17), (22, 23))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_bezier('p1-r2-1', (5, 16), ((5, 20), (8.666666666666668, 24.333333333333336), (16, 29)))
        self.add_line('p1-r2-2', (16, 29), (19, 26))
        self.add_contour('path-1-2', 'p1-r2-1', 'p1-r2-2', closed=False)
        self.add_line('p2-r1-1', (2, 2), (30, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
