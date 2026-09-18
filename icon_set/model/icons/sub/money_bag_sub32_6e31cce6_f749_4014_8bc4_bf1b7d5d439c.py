"""Independent 32px profile of money-bag.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6e31cce6-f749-4014-8bc4-bf1b7d5d439c'
SOURCE_PATH = 'pictographic-primitives/symbol/money bag_6e31cce6-f749-4014-8bc4-bf1b7d5d439c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6e31cce6-f749-4014-8bc4-bf1b7d5d439c', 'pictographic-primitives/symbol/money bag_6e31cce6-f749-4014-8bc4-bf1b7d5d439c.svg'), ('e362c0ea-dba3-4194-90fc-c3ab21b70d2b', 'pictographic-primitives/other/pouch dollar_e362c0ea-dba3-4194-90fc-c3ab21b70d2b.svg'))
PROFILE_SOURCE_KEYS = ('solo/money-bag', 'solo/money-bag-with-dollar-sign-solo')
SOLO_SOURCE_ICON_IDS = ('money-bag', 'money-bag-with-dollar-sign-solo')
REFERENCE_EXPORT_SHA256 = '0e2c5e13d6bbd9c804573a7efed2f30626824cad34a4b2376b257e0c7b72e3b7'

class Drawing(Sub32):
    icon_id = 'money-bag-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (10, 5), (5, 16), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_line('p1-r1-2', (5, 16), (5, 23))
        self.add_arc('p1-r1-3', (5, 23), (12, 30), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('p1-r1-4', (12, 30), (20, 30))
        self.add_arc('p1-r1-5', (20, 30), (27, 23), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('p1-r1-6', (27, 23), (27, 16))
        self.add_arc('p1-r1-7', (27, 16), (22, 5), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (10, 5), (8, 2))
        self.add_line('p2-r1-2', (8, 2), (24, 2))
        self.add_line('p2-r1-3', (24, 2), (22, 5))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (17, 12), (16, 12))
        self.add_line('p3-r1-2', (16, 12), (15, 12))
        self.add_arc('p3-r1-3', (15, 12), (15, 17), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p3-r1-4', (15, 17), (17, 17))
        self.add_arc('p3-r1-5', (17, 17), (17, 23), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-6', (17, 23), (16, 23))
        self.add_line('p3-r1-7', (16, 23), (15, 23))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
        self.add_line('p4-r1-1', (16, 11), (16, 12))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (16, 23), (16, 24))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-7', 'p2-r1-3')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-6', 'p5-r1-1')
        self.relate("connect", 'p3-r1-7', 'p5-r1-1')
