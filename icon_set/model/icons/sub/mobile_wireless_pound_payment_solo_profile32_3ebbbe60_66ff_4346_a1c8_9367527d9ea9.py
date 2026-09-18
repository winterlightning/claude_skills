"""Independent 32px profile of mobile-wireless-pound-payment-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3ebbbe60-66ff-4346-a1c8-9367527d9ea9'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone pound sign wireless_3ebbbe60-66ff-4346-a1c8-9367527d9ea9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3ebbbe60-66ff-4346-a1c8-9367527d9ea9', 'pictographic-primitives/other/mobile phone pound sign wireless_3ebbbe60-66ff-4346-a1c8-9367527d9ea9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/mobile-wireless-pound-payment-solo',)
SOLO_SOURCE_ICON_IDS = ('mobile-wireless-pound-payment-solo',)
REFERENCE_EXPORT_SHA256 = '29749699c767f28e1029d9ab391a263486c9f4c9a99ec4b6267829fa49b27803'

class Drawing(Sub32):
    icon_id = 'mobile-wireless-pound-payment-solo-profile32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/finance'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (5, 6), ((8, 3), (12, 2), (16, 2)))
        self.add_bezier('p1-r1-2', (16, 2), ((20, 2), (24, 3), (27, 6)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (5, 13), (5, 26))
        self.add_arc('p2-r1-2', (5, 26), (9, 30), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p2-r1-3', (9, 30), (23, 30))
        self.add_arc('p2-r1-4', (23, 30), (27, 26), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p2-r1-5', (27, 26), (27, 13))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_arc('p3-r1-1', (20, 16), (14, 16), radius_x=3, radius_y=2, large_arc=False, sweep=False)
        self.add_line('p3-r1-2', (14, 16), (14, 18))
        self.add_line('p3-r1-3', (14, 18), (14, 24))
        self.add_line('p3-r1-4', (14, 24), (18, 24))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (13, 18), (14, 18))
        self.add_line('p4-r1-2', (14, 18), (17, 18))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-2')
        self.relate("connect", 'p3-r1-3', 'p4-r1-1')
        self.relate("connect", 'p3-r1-3', 'p4-r1-2')
