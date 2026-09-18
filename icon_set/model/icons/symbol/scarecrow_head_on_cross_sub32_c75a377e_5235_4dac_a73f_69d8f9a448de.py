"""Independent 32px profile of scarecrow-head-on-cross.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'c75a377e-5235-4dac-a73f-69d8f9a448de'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/scarecrow_c75a377e-5235-4dac-a73f-69d8f9a448de.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c75a377e-5235-4dac-a73f-69d8f9a448de', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/scarecrow_c75a377e-5235-4dac-a73f-69d8f9a448de.svg'),)
PROFILE_SOURCE_KEYS = ('solo/scarecrow-head-on-cross',)
SOLO_SOURCE_ICON_IDS = ('scarecrow-head-on-cross',)
REFERENCE_EXPORT_SHA256 = '7dd9e81ad942bd7a2635b2867cfca6e07d7dc611d1bb20628d4c5c9dd4bda89b'

class Drawing(Sub32):
    icon_id = 'scarecrow-head-on-cross-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/agriculture'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 8), (16, 12), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 12), (16, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (9, 8), (12, 8))
        self.add_line('p2-r1-2', (12, 8), (16, 8))
        self.add_line('p2-r1-3', (16, 8), (20, 8))
        self.add_line('p2-r1-4', (20, 8), (23, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (12, 8), (13, 2))
        self.add_line('p3-r1-2', (13, 2), (19, 2))
        self.add_line('p3-r1-3', (19, 2), (20, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (5, 17), (16, 17))
        self.add_line('p4-r1-2', (16, 17), (27, 17))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (16, 17), (16, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p3-r1-3')
        self.relate('connect', 'p2-r1-4', 'p3-r1-3')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-2', 'p5-r1-1')
