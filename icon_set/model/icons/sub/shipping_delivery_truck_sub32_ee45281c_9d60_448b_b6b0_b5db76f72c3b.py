"""Independent 32px profile of shipping-delivery-truck-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ee45281c-9d60-448b-b6b0-b5db76f72c3b'
SOURCE_PATH = 'pictographic-primitives/transportation/truck_ee45281c-9d60-448b-b6b0-b5db76f72c3b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ee45281c-9d60-448b-b6b0-b5db76f72c3b', 'pictographic-primitives/transportation/truck_ee45281c-9d60-448b-b6b0-b5db76f72c3b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shipping-delivery-truck-solo',)
SOLO_SOURCE_ICON_IDS = ('shipping-delivery-truck-solo',)
REFERENCE_EXPORT_SHA256 = '31be7a040ee3c4051d74facabcd9943541ce14e4dd3e6344d00cf732a3ad892f'

class Drawing(Sub32):
    icon_id = 'shipping-delivery-truck-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 17), (2, 5))
        self.add_line('p1-r1-2', (2, 5), (18, 5))
        self.add_line('p1-r1-3', (18, 5), (18, 10))
        self.add_line('p1-r1-4', (18, 10), (24, 10))
        self.add_line('p1-r1-5', (24, 10), (30, 17))
        self.add_line('p1-r1-6', (30, 17), (2, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (18, 10), (18, 17))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (6, 25), (10, 25), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (10, 25), (6, 25), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_arc('p4-r1-1', (22, 25), (26, 25), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (26, 25), (22, 25), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
