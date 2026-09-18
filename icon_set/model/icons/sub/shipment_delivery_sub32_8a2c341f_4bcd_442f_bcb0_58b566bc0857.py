"""Independent 32px profile of shipment-delivery.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '8a2c341f-4bcd-442f-bcb0-58b566bc0857'
SOURCE_PATH = 'pictographic-primitives/delivery/shipment_8a2c341f-4bcd-442f-bcb0-58b566bc0857.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8a2c341f-4bcd-442f-bcb0-58b566bc0857', 'pictographic-primitives/delivery/shipment_8a2c341f-4bcd-442f-bcb0-58b566bc0857.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shipment-delivery',)
SOLO_SOURCE_ICON_IDS = ('shipment-delivery',)
REFERENCE_EXPORT_SHA256 = '959f1a72a8d530bf1cef6a2c3b271d2ad890ede3db426b28b8cb0a999cfab05d'

class Drawing(Sub32):
    icon_id = 'shipment-delivery-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'delivery'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (17, 5))
        self.add_line('p1-r1-2', (17, 5), (17, 11))
        self.add_line('p1-r1-3', (17, 11), (25, 11))
        self.add_line('p1-r1-4', (25, 11), (30, 17))
        self.add_bezier('p1-r1-5', (30, 17), ((30, 20), (29, 22), (29, 24)))
        self.add_arc('p1-r1-6', (29, 24), (22, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (22, 24), (17, 24))
        self.add_line('p1-r1-8', (17, 24), (11, 24))
        self.add_arc('p1-r1-9', (11, 24), (4, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-10', (4, 24), ((4, 21), (2, 20), (2, 16)))
        self.add_line('p1-r1-11', (2, 16), (2, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
        self.add_arc('p2-r1-1', (4, 24), (11, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (22, 24), (29, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (17, 11), (17, 24))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-2', 'p4-r1-1')
        self.relate("connect", 'p1-r1-3', 'p4-r1-1')
        self.relate("connect", 'p1-r1-5', 'p3-r1-1')
        self.relate("connect", 'p1-r1-6', 'p3-r1-1')
        self.relate("connect", 'p1-r1-7', 'p3-r1-1')
        self.relate("connect", 'p1-r1-7', 'p4-r1-1')
        self.relate("connect", 'p1-r1-8', 'p2-r1-1')
        self.relate("connect", 'p1-r1-8', 'p4-r1-1')
        self.relate("connect", 'p1-r1-9', 'p2-r1-1')
        self.relate("connect", 'p1-r1-10', 'p2-r1-1')
