"""Independent 32px profile of state32-72d899a4-6d14-40d7-81f0-a36e3773ca36.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '72d899a4-6d14-40d7-81f0-a36e3773ca36'
SOURCE_PATH = 'icon_set/assets/combination-state32/72d899a4-6d14-40d7-81f0-a36e3773ca36.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('72d899a4-6d14-40d7-81f0-a36e3773ca36', 'icon_set/assets/combination-state32/72d899a4-6d14-40d7-81f0-a36e3773ca36.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'b7b239f2367197a709a91549995e86ec720a775c09ba13e3f863b37fea9fe66d'

class Drawing(Sub32):
    icon_id = 'state32-72d899a4-6d14-40d7-81f0-a36e3773ca36'
    keyshape = Keyshape.HRECT_M
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 23), (7, 10))
        self.add_bezier('p1-r1-2', (7, 10), ((7, 9.333333333333334), (7, 9), (7, 9)))
        self.add_bezier('p1-r1-3', (7, 9), ((7, 9), (7.333333333333333, 9.333333333333334), (8, 10)))
        self.add_line('p1-r1-4', (8, 10), (12, 23))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (4, 17), (10, 17))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (18, 9), (18, 18))
        self.add_bezier('p3-r1-2', (18, 18), ((18, 18), (19, 18), (19, 18)))
        self.add_line('p3-r1-3', (19, 18), (30, 18))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (28, 9), (28, 23))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
