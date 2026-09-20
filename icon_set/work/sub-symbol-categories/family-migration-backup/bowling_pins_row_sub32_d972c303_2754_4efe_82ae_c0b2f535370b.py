"""Independent 32px profile of bowling-pins-row.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd972c303-2754-4efe-82ae-c0b2f535370b'
SOURCE_PATH = 'pictographic-primitives/symbol/three bowlings_d972c303-2754-4efe-82ae-c0b2f535370b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d972c303-2754-4efe-82ae-c0b2f535370b', 'pictographic-primitives/symbol/three bowlings_d972c303-2754-4efe-82ae-c0b2f535370b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bowling-pins-row',)
SOLO_SOURCE_ICON_IDS = ('bowling-pins-row',)
REFERENCE_EXPORT_SHA256 = '7e2266793a3782340fe034c864ad5074b7828bfad71d94754eeda6b08ae177c4'

class Drawing(Sub32):
    icon_id = 'bowling-pins-row-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (3, 7), (5, 5), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (5, 5), (7, 7), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (7, 7), (5, 9), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (5, 9), (3, 7), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_arc('p2-r1-1', (2, 20), (5, 12), radius_x=3, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (5, 12), (8, 20), radius_x=3, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (8, 20), (5, 27), radius_x=3, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p2-r1-4', (5, 27), (2, 20), radius_x=3, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_arc('p3-r1-1', (14, 7), (16, 5), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (16, 5), (18, 7), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (18, 7), (16, 9), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (16, 9), (14, 7), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_arc('p4-r1-1', (13, 20), (16, 12), radius_x=3, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (16, 12), (19, 20), radius_x=3, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p4-r1-3', (19, 20), (16, 27), radius_x=3, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p4-r1-4', (16, 27), (13, 20), radius_x=3, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_arc('p5-r1-1', (25, 7), (27, 5), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p5-r1-2', (27, 5), (29, 7), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p5-r1-3', (29, 7), (27, 9), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p5-r1-4', (27, 9), (25, 7), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
        self.add_arc('p6-r1-1', (24, 20), (27, 12), radius_x=3, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p6-r1-2', (27, 12), (30, 20), radius_x=3, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p6-r1-3', (30, 20), (27, 27), radius_x=3, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p6-r1-4', (27, 27), (24, 20), radius_x=3, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', closed=False)
