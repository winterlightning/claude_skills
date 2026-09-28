"""Independent 32px profile of slider.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'deca21f2-e97c-497e-b7e0-b915823149ae'
SOURCE_PATH = 'pictographic-primitives/symbol/slider_deca21f2-e97c-497e-b7e0-b915823149ae.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('deca21f2-e97c-497e-b7e0-b915823149ae', 'pictographic-primitives/symbol/slider_deca21f2-e97c-497e-b7e0-b915823149ae.svg'),)
PROFILE_SOURCE_KEYS = ('solo/slider',)
SOLO_SOURCE_ICON_IDS = ('slider',)
REFERENCE_EXPORT_SHA256 = '76ba943f150a3731d3b32e22a1cbaec306e2d311fc8d58ed54e08cc610633ffd'

class Drawing(Sub32):
    icon_id = 'slider-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (7, 8), (10, 5), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (10, 5), (14, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (14, 8), (10, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (10, 12), (7, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, 8), (7, 8))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (14, 8), (30, 8))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (18, 18), (22, 15), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (22, 15), (25, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p4-r1-3', (25, 18), (22, 22), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p4-r1-4', (22, 22), (18, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (2, 18), (18, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (25, 18), (30, 18))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (2, 27), (30, 27))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-2', 'p6-r1-1')
        self.relate('connect', 'p4-r1-3', 'p6-r1-1')
        self.relate('connect', 'p4-r1-4', 'p5-r1-1')
