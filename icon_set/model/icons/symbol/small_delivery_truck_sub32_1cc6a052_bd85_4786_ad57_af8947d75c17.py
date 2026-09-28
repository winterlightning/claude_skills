"""Independent 32px profile of small-delivery-truck.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '1cc6a052-bd85-4786-ad57-af8947d75c17'
SOURCE_PATH = 'pictographic-primitives/transportation/truck_1cc6a052-bd85-4786-ad57-af8947d75c17.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1cc6a052-bd85-4786-ad57-af8947d75c17', 'pictographic-primitives/transportation/truck_1cc6a052-bd85-4786-ad57-af8947d75c17.svg'), ('7fa4b356-9d73-4875-94fd-29e892bef9d8', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/transportation/truck_7fa4b356-9d73-4875-94fd-29e892bef9d8.svg'))
PROFILE_SOURCE_KEYS = ('solo/small-delivery-truck',)
SOLO_SOURCE_ICON_IDS = ('small-delivery-truck',)
REFERENCE_EXPORT_SHA256 = 'cdd9f7ee05102abff53fe456b3fbcee263b835b459ca19a7d69e1200e45cfb71'

class Drawing(Sub32):
    icon_id = 'small-delivery-truck-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (3, 24), (2, 24))
        self.add_line('p1-r1-2', (2, 24), (2, 5))
        self.add_line('p1-r1-3', (2, 5), (16, 5))
        self.add_line('p1-r1-4', (16, 5), (16, 10))
        self.add_line('p1-r1-5', (16, 10), (16, 24))
        self.add_line('p1-r1-6', (16, 24), (10, 24))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (16, 10), (22, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (22, 10), ((26, 11), (30, 15), (30, 19)))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (30, 19), (30, 24))
        self.add_line('p4-r1-2', (30, 24), (29, 24))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (16, 24), (22, 24))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_bezier('p6-r1-1', (3, 24), ((4, 23), (5, 22), (7, 22)))
        self.add_bezier('p6-r1-2', (7, 22), ((9, 22), (10, 23), (10, 24)))
        self.add_bezier('p6-r1-3', (10, 24), ((10, 26), (9, 27), (7, 27)))
        self.add_bezier('p6-r1-4', (7, 27), ((5, 27), (4, 26), (3, 24)))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', closed=False)
        self.add_bezier('p7-r1-1', (22, 24), ((22, 23), (23, 22), (25, 22)))
        self.add_bezier('p7-r1-2', (25, 22), ((27, 22), (28, 23), (29, 24)))
        self.add_bezier('p7-r1-3', (29, 24), ((28, 26), (27, 27), (25, 27)))
        self.add_bezier('p7-r1-4', (25, 27), ((23, 27), (22, 26), (22, 24)))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', 'p7-r1-3', 'p7-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p6-r1-1')
        self.relate('connect', 'p1-r1-1', 'p6-r1-4')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p5-r1-1')
        self.relate('connect', 'p1-r1-6', 'p5-r1-1')
        self.relate('connect', 'p1-r1-6', 'p6-r1-2')
        self.relate('connect', 'p1-r1-6', 'p6-r1-3')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p4-r1-2', 'p7-r1-2')
        self.relate('connect', 'p4-r1-2', 'p7-r1-3')
        self.relate('connect', 'p5-r1-1', 'p7-r1-1')
        self.relate('connect', 'p5-r1-1', 'p7-r1-4')
