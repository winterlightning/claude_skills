"""Independent 32px profile of aperture-shutter.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '0cb953cf-9714-40a8-af67-7ea79c576259'
SOURCE_PATH = 'pictographic-primitives/symbol/lens shutter_0cb953cf-9714-40a8-af67-7ea79c576259.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0cb953cf-9714-40a8-af67-7ea79c576259', 'pictographic-primitives/symbol/lens shutter_0cb953cf-9714-40a8-af67-7ea79c576259.svg'),)
PROFILE_SOURCE_KEYS = ('solo/aperture-shutter',)
SOLO_SOURCE_ICON_IDS = ('aperture-shutter',)
REFERENCE_EXPORT_SHA256 = 'c81ebca7ccf0bdc02ca2477f49a83a41fbf31e5251e30cc74db15ee147353af1'

class Drawing(Sub32):
    icon_id = 'aperture-shutter-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (27, 8), (27, 24), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (27, 24), (16, 30), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (16, 30), (5, 24), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (5, 24), (5, 8), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (5, 8), (16, 2), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (16, 2), (27, 8), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (27, 8), (20, 9))
        self.add_line('p2-r1-2', (20, 9), (12, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (27, 24), (23, 16))
        self.add_line('p3-r1-2', (23, 16), (20, 9))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (16, 30), (20, 22))
        self.add_line('p4-r1-2', (20, 22), (23, 16))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (5, 24), (13, 23))
        self.add_line('p5-r1-2', (13, 23), (20, 22))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (5, 8), (9, 16))
        self.add_line('p6-r1-2', (9, 16), (13, 23))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_line('p7-r1-1', (16, 2), (12, 10))
        self.add_line('p7-r1-2', (12, 10), (9, 16))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p1-r1-3', 'p4-r1-1')
        self.relate('connect', 'p1-r1-3', 'p5-r1-1')
        self.relate('connect', 'p1-r1-4', 'p5-r1-1')
        self.relate('connect', 'p1-r1-4', 'p6-r1-1')
        self.relate('connect', 'p1-r1-5', 'p6-r1-1')
        self.relate('connect', 'p1-r1-5', 'p7-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p7-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p7-r1-1')
        self.relate('connect', 'p2-r1-2', 'p7-r1-2')
        self.relate('connect', 'p3-r1-1', 'p4-r1-2')
        self.relate('connect', 'p3-r1-2', 'p4-r1-2')
        self.relate('connect', 'p4-r1-1', 'p5-r1-2')
        self.relate('connect', 'p4-r1-2', 'p5-r1-2')
        self.relate('connect', 'p5-r1-1', 'p6-r1-2')
        self.relate('connect', 'p5-r1-2', 'p6-r1-2')
        self.relate('connect', 'p6-r1-1', 'p7-r1-2')
        self.relate('connect', 'p6-r1-2', 'p7-r1-2')
