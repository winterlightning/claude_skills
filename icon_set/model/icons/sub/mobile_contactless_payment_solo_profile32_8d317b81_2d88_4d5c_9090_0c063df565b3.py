"""Independent 32px profile of mobile-contactless-payment-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '8d317b81-2d88-4d5c-9090-0c063df565b3'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone dollar sign wireless_8d317b81-2d88-4d5c-9090-0c063df565b3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8d317b81-2d88-4d5c-9090-0c063df565b3', 'pictographic-primitives/other/mobile phone dollar sign wireless_8d317b81-2d88-4d5c-9090-0c063df565b3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/mobile-contactless-payment-solo',)
SOLO_SOURCE_ICON_IDS = ('mobile-contactless-payment-solo',)
REFERENCE_EXPORT_SHA256 = 'a876b26c0cc05c054034c777d3eb9a0358c522a6a9e464fc0280f5350bd3f04f'

class Drawing(Sub32):
    icon_id = 'mobile-contactless-payment-solo-profile32'
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
        self.add_line('p3-r1-1', (20, 12), (16, 12))
        self.add_arc('p3-r1-2', (16, 12), (16, 17), radius_x=4, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('p3-r1-3', (16, 17), (16, 23), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-4', (16, 23), (12, 23))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (16, 11), (16, 12))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (16, 23), (16, 24))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-3', 'p5-r1-1')
        self.relate("connect", 'p3-r1-4', 'p5-r1-1')
