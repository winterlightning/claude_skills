"""Independent 32px profile of water-skier.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'a0a86c5e-f6ab-4aef-80ad-0ea729f25840'
SOURCE_PATH = 'pictographic-primitives/sports/skating_a0a86c5e-f6ab-4aef-80ad-0ea729f25840.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a0a86c5e-f6ab-4aef-80ad-0ea729f25840', 'pictographic-primitives/sports/skating_a0a86c5e-f6ab-4aef-80ad-0ea729f25840.svg'),)
PROFILE_SOURCE_KEYS = ('solo/water-skier',)
SOLO_SOURCE_ICON_IDS = ('water-skier',)
REFERENCE_EXPORT_SHA256 = 'f6760282f2933c613cc9c2d3a4de3112970eeb34c16fa176f58121184039cd12'

class Drawing(Sub32):
    icon_id = 'water-skier-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/sports'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (7, 8), (13, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (13, 8), (7, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (10, 16), ((10, 18), (9, 20), (9, 22)))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (9, 22), (15, 22))
        self.add_line('p3-r1-2', (15, 22), (16, 27))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (3, 18), (10, 16))
        self.add_line('p4-r1-2', (10, 16), (20, 16))
        self.add_line('p4-r1-3', (20, 16), (30, 14))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.add_line('p5-r1-1', (2, 27), (16, 27))
        self.add_line('p5-r1-2', (16, 27), (24, 27))
        self.add_arc('p5-r1-3', (24, 27), (30, 22), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-2')
        self.relate('connect', 'p3-r1-2', 'p5-r1-1')
        self.relate('connect', 'p3-r1-2', 'p5-r1-2')
