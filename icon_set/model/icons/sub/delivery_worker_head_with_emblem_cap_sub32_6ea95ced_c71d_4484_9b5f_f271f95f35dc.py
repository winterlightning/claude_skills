"""Independent 32px profile of delivery-worker-head-with-emblem-cap.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6ea95ced-c71d-4484-9b5f-f271f95f35dc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/delivery/delivery man give_6ea95ced-c71d-4484-9b5f-f271f95f35dc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6ea95ced-c71d-4484-9b5f-f271f95f35dc', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/delivery/delivery man give_6ea95ced-c71d-4484-9b5f-f271f95f35dc.svg'),)
PROFILE_SOURCE_KEYS = ('solo/delivery-worker-head-with-emblem-cap',)
SOLO_SOURCE_ICON_IDS = ('delivery-worker-head-with-emblem-cap',)
REFERENCE_EXPORT_SHA256 = 'f5ca168663e039620b80c906f20a62deceb074fe5e3512a8f339cbdac76408eb'

class Drawing(Sub32):
    icon_id = 'delivery-worker-head-with-emblem-cap-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/people'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 16), (5, 5))
        self.add_line('p1-r1-2', (5, 5), (10, 2))
        self.add_line('p1-r1-3', (10, 2), (22, 2))
        self.add_line('p1-r1-4', (22, 2), (27, 5))
        self.add_line('p1-r1-5', (27, 5), (27, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (5, 16), (27, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (15, 9), (17, 9), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (17, 9), (15, 9), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_arc('p4-r1-1', (5, 19), (10, 30), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (5, 16), (5, 19))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_arc('p6-r1-1', (27, 19), (22, 30), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (27, 16), (27, 19))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p5-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p7-r1-1')
        self.relate("connect", 'p2-r1-1', 'p5-r1-1')
        self.relate("connect", 'p2-r1-1', 'p7-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
        self.relate("connect", 'p6-r1-1', 'p7-r1-1')
