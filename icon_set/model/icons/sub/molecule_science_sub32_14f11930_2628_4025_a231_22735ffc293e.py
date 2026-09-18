"""Independent 32px profile of molecule-science.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '14f11930-2628-4025-a231-22735ffc293e'
SOURCE_PATH = 'pictographic-primitives/science/molecule_14f11930-2628-4025-a231-22735ffc293e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('14f11930-2628-4025-a231-22735ffc293e', 'pictographic-primitives/science/molecule_14f11930-2628-4025-a231-22735ffc293e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/molecule-science',)
SOLO_SOURCE_ICON_IDS = ('molecule-science',)
REFERENCE_EXPORT_SHA256 = '27efd11e433eb03658a32f52951937d48201b522b13d943e64ac4c53203d8112'

class Drawing(Sub32):
    icon_id = 'molecule-science-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'science'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (12, 21), (16, 17), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 17), (20, 21), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (20, 21), (16, 25), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 25), (12, 21), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_arc('p2-r1-1', (2, 21), (5, 19), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (5, 19), (7, 21), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (7, 21), (5, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-4', (5, 24), (2, 21), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_arc('p3-r1-1', (25, 21), (27, 19), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (27, 19), (30, 21), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (30, 21), (27, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (27, 24), (25, 21), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_arc('p4-r1-1', (13, 10), (16, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (16, 7), (19, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p4-r1-3', (19, 10), (16, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p4-r1-4', (16, 12), (13, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (7, 21), (12, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (20, 21), (25, 21))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (16, 12), (16, 17))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p5-r1-1')
        self.relate("connect", 'p1-r1-1', 'p7-r1-1')
        self.relate("connect", 'p1-r1-2', 'p6-r1-1')
        self.relate("connect", 'p1-r1-2', 'p7-r1-1')
        self.relate("connect", 'p1-r1-3', 'p6-r1-1')
        self.relate("connect", 'p1-r1-4', 'p5-r1-1')
        self.relate("connect", 'p2-r1-2', 'p5-r1-1')
        self.relate("connect", 'p2-r1-3', 'p5-r1-1')
        self.relate("connect", 'p3-r1-1', 'p6-r1-1')
        self.relate("connect", 'p3-r1-4', 'p6-r1-1')
        self.relate("connect", 'p4-r1-3', 'p7-r1-1')
        self.relate("connect", 'p4-r1-4', 'p7-r1-1')
