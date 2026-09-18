"""Independent 32px profile of briefcase-with-central-clasp.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0e065604-cef0-4168-88bd-c1578cd53419'
SOURCE_PATH = 'pictographic-primitives/business/briefcase_0e065604-cef0-4168-88bd-c1578cd53419.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0e065604-cef0-4168-88bd-c1578cd53419', 'pictographic-primitives/business/briefcase_0e065604-cef0-4168-88bd-c1578cd53419.svg'),)
PROFILE_SOURCE_KEYS = ('solo/briefcase-with-central-clasp',)
SOLO_SOURCE_ICON_IDS = ('briefcase-with-central-clasp',)
REFERENCE_EXPORT_SHA256 = 'd22103870bbebc47ceeb0e8dc746602a8bc24fcd12e56a87f31953e4f9eca500'

class Drawing(Sub32):
    icon_id = 'briefcase-with-central-clasp-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'business'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 10), (10, 10))
        self.add_line('p1-r1-2', (10, 10), (22, 10))
        self.add_line('p1-r1-3', (22, 10), (27, 10))
        self.add_arc('p1-r1-4', (27, 10), (30, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (30, 13), (30, 17))
        self.add_line('p1-r1-6', (30, 17), (30, 24))
        self.add_arc('p1-r1-7', (30, 24), (27, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (27, 27), (5, 27))
        self.add_arc('p1-r1-9', (5, 27), (2, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-10', (2, 24), (2, 17))
        self.add_line('p1-r1-11', (2, 17), (2, 13))
        self.add_arc('p1-r1-12', (2, 13), (5, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_line('p2-r1-1', (10, 10), (10, 8))
        self.add_arc('p2-r1-2', (10, 8), (13, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (13, 5), (19, 5))
        self.add_arc('p2-r1-4', (19, 5), (22, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (22, 8), (22, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (2, 17), (16, 17))
        self.add_line('p3-r1-2', (16, 17), (30, 17))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (16, 17), (16, 22))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-5')
        self.relate("connect", 'p1-r1-3', 'p2-r1-5')
        self.relate("connect", 'p1-r1-5', 'p3-r1-2')
        self.relate("connect", 'p1-r1-6', 'p3-r1-2')
        self.relate("connect", 'p1-r1-10', 'p3-r1-1')
        self.relate("connect", 'p1-r1-11', 'p3-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
