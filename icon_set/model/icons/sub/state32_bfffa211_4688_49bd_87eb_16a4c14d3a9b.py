"""Independent 32px profile of state32-bfffa211-4688-49bd-87eb-16a4c14d3a9b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'bfffa211-4688-49bd-87eb-16a4c14d3a9b'
SOURCE_PATH = 'icon_set/assets/combination-state32/bfffa211-4688-49bd-87eb-16a4c14d3a9b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bfffa211-4688-49bd-87eb-16a4c14d3a9b', 'icon_set/assets/combination-state32/bfffa211-4688-49bd-87eb-16a4c14d3a9b.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'bc2faf4811e719802c5761452222d20baafcde9130a4b00cefa7104dfad48ee5'

class Drawing(Sub32):
    icon_id = 'state32-bfffa211-4688-49bd-87eb-16a4c14d3a9b'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 8), ((4, 6), (6.333333333333334, 5), (9, 5)))
        self.add_bezier('p1-r1-2', (9, 5), ((11, 5), (13.333333333333334, 6), (16, 8)))
        self.add_bezier('p1-r1-3', (16, 8), ((18.666666666666668, 9.333333333333334), (21, 10), (23, 10)))
        self.add_bezier('p1-r1-4', (23, 10), ((25.666666666666668, 10), (28, 9.333333333333334), (30, 8)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p1-r2-1', (2, 16), ((4, 14.666666666666666), (6.333333333333334, 14), (9, 14)))
        self.add_bezier('p1-r2-2', (9, 14), ((11, 14), (13.333333333333334, 14.666666666666666), (16, 16)))
        self.add_bezier('p1-r2-3', (16, 16), ((18.666666666666668, 17.333333333333332), (21, 18), (23, 18)))
        self.add_bezier('p1-r2-4', (23, 18), ((25.666666666666668, 18), (28, 17.333333333333332), (30, 16)))
        self.add_contour('path-1-2', 'p1-r2-1', 'p1-r2-2', 'p1-r2-3', 'p1-r2-4', closed=False)
        self.add_bezier('p1-r3-1', (2, 24), ((4, 22.666666666666668), (6.333333333333334, 22), (9, 22)))
        self.add_bezier('p1-r3-2', (9, 22), ((11, 22), (13.333333333333334, 22.666666666666668), (16, 24)))
        self.add_bezier('p1-r3-3', (16, 24), ((18.666666666666668, 26), (21, 27), (23, 27)))
        self.add_bezier('p1-r3-4', (23, 27), ((25.666666666666668, 27), (28, 26), (30, 24)))
        self.add_contour('path-1-3', 'p1-r3-1', 'p1-r3-2', 'p1-r3-3', 'p1-r3-4', closed=False)
