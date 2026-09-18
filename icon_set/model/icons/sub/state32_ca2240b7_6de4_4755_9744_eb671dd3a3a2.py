"""Independent 32px profile of state32-ca2240b7-6de4-4755-9744-eb671dd3a3a2.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ca2240b7-6de4-4755-9744-eb671dd3a3a2'
SOURCE_PATH = 'icon_set/assets/combination-state32/ca2240b7-6de4-4755-9744-eb671dd3a3a2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ca2240b7-6de4-4755-9744-eb671dd3a3a2', 'icon_set/assets/combination-state32/ca2240b7-6de4-4755-9744-eb671dd3a3a2.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '7f5274f7373c93b5a492dfc3afc16c6feaca3b917804ed1421eb8a203feb182a'

class Drawing(Sub32):
    icon_id = 'state32-ca2240b7-6de4-4755-9744-eb671dd3a3a2'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (15, 3), ((15, 3), (15.333333333333334, 3), (16, 3)))
        self.add_bezier('p1-r1-2', (16, 3), ((16.666666666666668, 3), (17, 3), (17, 3)))
        self.add_line('p1-r1-3', (17, 3), (22, 8))
        self.add_line('p1-r1-4', (22, 8), (26, 8))
        self.add_bezier('p1-r1-5', (26, 8), ((27.333333333333332, 8), (28, 8.333333333333334), (28, 9)))
        self.add_line('p1-r1-6', (28, 9), (28, 14))
        self.add_line('p1-r1-7', (28, 14), (30, 16))
        self.add_line('p1-r1-8', (30, 16), (28, 18))
        self.add_line('p1-r1-9', (28, 18), (28, 23))
        self.add_bezier('p1-r1-10', (28, 23), ((28, 23.666666666666668), (27.333333333333332, 24), (26, 24)))
        self.add_line('p1-r1-11', (26, 24), (22, 24))
        self.add_line('p1-r1-12', (22, 24), (17, 29))
        self.add_bezier('p1-r1-13', (17, 29), ((17, 29), (16.666666666666668, 29), (16, 29)))
        self.add_bezier('p1-r1-14', (16, 29), ((15.333333333333334, 29), (15, 29), (15, 29)))
        self.add_line('p1-r1-15', (15, 29), (10, 24))
        self.add_line('p1-r1-16', (10, 24), (6, 24))
        self.add_bezier('p1-r1-17', (6, 24), ((4.666666666666667, 24), (4, 23.666666666666668), (4, 23)))
        self.add_line('p1-r1-18', (4, 23), (4, 18))
        self.add_line('p1-r1-19', (4, 18), (2, 16))
        self.add_line('p1-r1-20', (2, 16), (4, 14))
        self.add_line('p1-r1-21', (4, 14), (4, 9))
        self.add_bezier('p1-r1-22', (4, 9), ((4, 8.333333333333334), (4.666666666666667, 8), (6, 8)))
        self.add_line('p1-r1-23', (6, 8), (10, 8))
        self.add_line('p1-r1-24', (10, 8), (15, 3))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', 'p1-r1-19', 'p1-r1-20', 'p1-r1-21', 'p1-r1-22', 'p1-r1-23', 'p1-r1-24', closed=False)
        self.add_line('p2-r1-1', (16, 11), (16, 17))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 21), (16, 21))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
