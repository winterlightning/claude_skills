"""Independent 32px profile of state32-970a6cde-a55d-4c40-bc6d-1f90c47200b1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '970a6cde-a55d-4c40-bc6d-1f90c47200b1'
SOURCE_PATH = 'icon_set/assets/combination-state32/970a6cde-a55d-4c40-bc6d-1f90c47200b1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('970a6cde-a55d-4c40-bc6d-1f90c47200b1', 'icon_set/assets/combination-state32/970a6cde-a55d-4c40-bc6d-1f90c47200b1.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'eef346c0377585d112b606d44d227d4ec4be8dfbeb560d5389d3dbdd7579213b'

class Drawing(Sub32):
    icon_id = 'state32-970a6cde-a55d-4c40-bc6d-1f90c47200b1'
    keyshape = Keyshape.HRECT_M
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 24), (7, 9))
        self.add_bezier('p1-r1-2', (7, 9), ((7, 8.333333333333334), (7.333333333333333, 8), (8, 8)))
        self.add_bezier('p1-r1-3', (8, 8), ((8, 8), (8, 8.333333333333334), (8, 9)))
        self.add_line('p1-r1-4', (8, 9), (13, 24))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (4, 17), (11, 17))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (29, 8), (20, 8))
        self.add_bezier('p3-r1-2', (20, 8), ((20, 8), (19, 9), (19, 9)))
        self.add_line('p3-r1-3', (19, 9), (19, 14))
        self.add_bezier('p3-r1-4', (19, 14), ((19, 15), (20, 15), (20, 15)))
        self.add_line('p3-r1-5', (20, 15), (26, 15))
        self.add_bezier('p3-r1-6', (26, 15), ((28, 15), (30, 17), (30, 19)))
        self.add_bezier('p3-r1-7', (30, 19), ((30, 20), (30, 21), (29, 22)))
        self.add_bezier('p3-r1-8', (29, 22), ((28, 23), (27, 24), (26, 24)))
        self.add_line('p3-r1-9', (26, 24), (20, 24))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', 'p3-r1-9', closed=False)
