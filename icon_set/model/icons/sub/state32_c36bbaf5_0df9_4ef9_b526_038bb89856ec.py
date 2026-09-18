"""Independent 32px profile of state32-c36bbaf5-0df9-4ef9-b526-038bb89856ec.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c36bbaf5-0df9-4ef9-b526-038bb89856ec'
SOURCE_PATH = 'icon_set/assets/combination-state32/c36bbaf5-0df9-4ef9-b526-038bb89856ec.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c36bbaf5-0df9-4ef9-b526-038bb89856ec', 'icon_set/assets/combination-state32/c36bbaf5-0df9-4ef9-b526-038bb89856ec.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '7d14372b7f6fe19b4d2248819a6420bb7fee8ee44a4188103c78f19d97915b92'

class Drawing(Sub32):
    icon_id = 'state32-c36bbaf5-0df9-4ef9-b526-038bb89856ec'
    keyshape = Keyshape.HRECT_S
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 12), (2, 17))
        self.add_bezier('p1-r1-2', (2, 17), ((2, 17), (2, 17), (2, 17)))
        self.add_line('p1-r1-3', (2, 17), (8, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (7, 12), (7, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (14, 14), (19, 14), radius_x=3, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p3-r1-2', (19, 14), (19, 18))
        self.add_arc('p3-r1-3', (19, 18), (14, 18), radius_x=3, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p3-r1-4', (14, 18), (14, 14))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (25, 12), (28, 12))
        self.add_bezier('p4-r1-2', (28, 12), ((29, 12), (30, 13), (30, 14)))
        self.add_bezier('p4-r1-3', (30, 14), ((30, 15), (29, 16), (28, 16)))
        self.add_line('p4-r1-4', (28, 16), (27, 16))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (27, 16), (28, 16))
        self.add_bezier('p5-r1-2', (28, 16), ((29, 16), (30, 17), (30, 18)))
        self.add_bezier('p5-r1-3', (30, 18), ((30, 19), (29, 20), (28, 20)))
        self.add_line('p5-r1-4', (28, 20), (25, 20))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
        self.relate("connect", 'p4-r1-3', 'p5-r1-1')
        self.relate("connect", 'p4-r1-3', 'p5-r1-2')
        self.relate("connect", 'p4-r1-4', 'p5-r1-1')
        self.relate("connect", 'p4-r1-4', 'p5-r1-2')
