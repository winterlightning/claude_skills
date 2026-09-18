"""Independent 32px profile of stethoscope.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd302c6d8-a92a-4d28-bbf2-86fef555f93f'
SOURCE_PATH = 'pictographic-primitives/symbol/stethoscope_d302c6d8-a92a-4d28-bbf2-86fef555f93f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d302c6d8-a92a-4d28-bbf2-86fef555f93f', 'pictographic-primitives/symbol/stethoscope_d302c6d8-a92a-4d28-bbf2-86fef555f93f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/stethoscope',)
SOLO_SOURCE_ICON_IDS = ('stethoscope',)
REFERENCE_EXPORT_SHA256 = '41b12e62b7ad988e90811b3e82a5d0ebf1efa864f1509281bbf4b90cfed740d0'

class Drawing(Sub32):
    icon_id = 'stethoscope-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (6, 2), (2, 4))
        self.add_line('p1-r1-2', (2, 4), (2, 11))
        self.add_arc('p1-r1-3', (2, 11), (10, 18), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('p1-r1-4', (10, 18), (18, 11), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (18, 11), (18, 4))
        self.add_line('p1-r1-6', (18, 4), (14, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (10, 18), (10, 21))
        self.add_arc('p2-r1-2', (10, 21), (27, 21), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_line('p2-r1-3', (27, 21), (27, 12))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_arc('p3-r1-1', (27, 12), (24, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (24, 9), (27, 6), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (27, 6), (30, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (30, 9), (27, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
        self.relate("connect", 'p2-r1-3', 'p3-r1-4')
