"""Independent 32px profile of binoculars.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'c302c027-d345-469d-98e7-0e924b296946'
SOURCE_PATH = 'pictographic-primitives/outdoors/binoculars_c302c027-d345-469d-98e7-0e924b296946.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c302c027-d345-469d-98e7-0e924b296946', 'pictographic-primitives/outdoors/binoculars_c302c027-d345-469d-98e7-0e924b296946.svg'),)
PROFILE_SOURCE_KEYS = ('solo/binoculars',)
SOLO_SOURCE_ICON_IDS = ('binoculars',)
REFERENCE_EXPORT_SHA256 = '24e230431f03ceced1189a42d673abece0e41c97389d2f4e544cc54763b1e6b2'

class Drawing(Sub32):
    icon_id = 'binoculars-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'outdoors'
    categories = ('outdoors', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 22), (13, 22), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (13, 22), (2, 22), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (2, 22), ((2, 17), (5, 13), (5, 9)))
        self.add_bezier('p2-r1-2', (5, 9), ((5, 6), (6, 5), (9, 5)))
        self.add_bezier('p2-r1-3', (9, 5), ((12, 5), (13, 6), (13, 9)))
        self.add_line('p2-r1-4', (13, 9), (13, 12))
        self.add_line('p2-r1-5', (13, 12), (13, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_arc('p3-r1-1', (19, 22), (30, 22), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (30, 22), (19, 22), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_bezier('p4-r1-1', (30, 22), ((30, 17), (27, 13), (27, 9)))
        self.add_bezier('p4-r1-2', (27, 9), ((27, 6), (26, 5), (23, 5)))
        self.add_bezier('p4-r1-3', (23, 5), ((20, 5), (19, 6), (19, 9)))
        self.add_line('p4-r1-4', (19, 9), (19, 12))
        self.add_line('p4-r1-5', (19, 12), (19, 22))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_line('p5-r1-1', (13, 12), (19, 12))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-5')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-5')
        self.relate('connect', 'p2-r1-4', 'p5-r1-1')
        self.relate('connect', 'p2-r1-5', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-5')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-5')
        self.relate('connect', 'p4-r1-4', 'p5-r1-1')
        self.relate('connect', 'p4-r1-5', 'p5-r1-1')
