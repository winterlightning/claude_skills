"""Independent 32px profile of state32-53668ec4-a104-4d57-8154-81e216c068e3.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '53668ec4-a104-4d57-8154-81e216c068e3'
SOURCE_PATH = 'icon_set/assets/combination-state32/53668ec4-a104-4d57-8154-81e216c068e3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('53668ec4-a104-4d57-8154-81e216c068e3', 'icon_set/assets/combination-state32/53668ec4-a104-4d57-8154-81e216c068e3.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'd252e99d8ac3a0f0fcaa989a4259bcb1238da1612be0b5f4e6c15cf917966b51'

class Drawing(Sub32):
    icon_id = 'state32-53668ec4-a104-4d57-8154-81e216c068e3'
    keyshape = Keyshape.HRECT_S
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 14), (9, 14), radius_x=3.5, radius_y=3.5, large_arc=True, sweep=True)
        self.add_arc('p1-r1-2', (9, 14), (2, 14), radius_x=3.5, radius_y=3.5, large_arc=True, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (9, 14), (9, 17))
        self.add_bezier('p2-r1-2', (9, 17), ((9, 19), (7, 21), (5, 21)))
        self.add_line('p2-r1-3', (5, 21), (3, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (17, 21), (17, 11))
        self.add_bezier('p3-r1-2', (17, 11), ((17, 11), (17, 11), (17, 11)))
        self.add_line('p3-r1-3', (17, 11), (15, 11))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (15, 21), (19, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (28, 21), (28, 11))
        self.add_bezier('p5-r1-2', (28, 11), ((28, 11), (28, 11), (27, 11)))
        self.add_line('p5-r1-3', (27, 11), (25, 11))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.add_line('p6-r1-1', (25, 21), (30, 21))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
