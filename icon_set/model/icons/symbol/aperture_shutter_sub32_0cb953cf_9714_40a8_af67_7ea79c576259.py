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
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=True)
        self.add_line('p2-r1-1', (22, 16), (19, 11))
        self.add_line('p2-r1-2', (19, 11), (13, 11))
        self.add_line('p2-r1-3', (13, 11), (10, 16))
        self.add_line('p2-r1-4', (10, 16), (13, 21))
        self.add_line('p2-r1-5', (13, 21), (19, 21))
        self.add_line('p2-r1-6', (19, 21), (22, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=True)
        self.add_line('p3-r1-1', (19, 11), (16, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (13, 11), (3, 11))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (10, 16), (4, 23))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (13, 21), (16, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (19, 21), (29, 21))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (22, 16), (28, 9))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p8-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p4-r1-1')
        self.relate('connect', 'p2-r1-3', 'p4-r1-1')
        self.relate('connect', 'p2-r1-3', 'p5-r1-1')
        self.relate('connect', 'p2-r1-4', 'p5-r1-1')
        self.relate('connect', 'p2-r1-4', 'p6-r1-1')
        self.relate('connect', 'p2-r1-5', 'p6-r1-1')
        self.relate('connect', 'p2-r1-5', 'p7-r1-1')
        self.relate('connect', 'p2-r1-6', 'p7-r1-1')
        self.relate('connect', 'p2-r1-6', 'p8-r1-1')
        self.relate('connect', 'path-1-1', 'path-3-1')
        self.relate('connect', 'path-1-1', 'path-4-1')
        self.relate('connect', 'path-1-1', 'path-5-1')
        self.relate('connect', 'path-1-1', 'path-6-1')
        self.relate('connect', 'path-1-1', 'path-7-1')
        self.relate('connect', 'path-1-1', 'path-8-1')
