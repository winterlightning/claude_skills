"""Independent 32px profile of microchip.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2b5c422f-8509-4a8c-b6e7-26b6c0d4494b'
SOURCE_PATH = 'pictographic-primitives/symbol/microchip_2b5c422f-8509-4a8c-b6e7-26b6c0d4494b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2b5c422f-8509-4a8c-b6e7-26b6c0d4494b', 'pictographic-primitives/symbol/microchip_2b5c422f-8509-4a8c-b6e7-26b6c0d4494b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/microchip',)
SOLO_SOURCE_ICON_IDS = ('microchip',)
REFERENCE_EXPORT_SHA256 = '3dbd78fc90621d824880920aac9bf6a4f1b6b8d289a72af155189ac326ef56b5'

class Drawing(Sub32):
    icon_id = 'microchip-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 7), (11, 7))
        self.add_line('p1-r1-2', (11, 7), (21, 7))
        self.add_line('p1-r1-3', (21, 7), (22, 7))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_arc('p2-r1-1', (22, 7), (25, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (25, 10), (25, 11))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (25, 11), (25, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (25, 21), (25, 22))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_arc('p6-r1-1', (25, 22), (22, 25), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (22, 25), (21, 25))
        self.add_line('p7-r1-2', (21, 25), (11, 25))
        self.add_line('p7-r1-3', (11, 25), (10, 25))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', 'p7-r1-3', closed=False)
        self.add_arc('p8-r1-1', (10, 25), (7, 22), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (7, 22), (7, 21))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
        self.add_line('p10-r1-1', (7, 21), (7, 11))
        self.add_contour('path-10-1', 'p10-r1-1', closed=False)
        self.add_line('p11-r1-1', (7, 11), (7, 10))
        self.add_contour('path-11-1', 'p11-r1-1', closed=False)
        self.add_arc('p12-r1-1', (7, 10), (10, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-12-1', 'p12-r1-1', closed=False)
        self.add_line('p13-r1-1', (11, 2), (11, 7))
        self.add_contour('path-13-1', 'p13-r1-1', closed=False)
        self.add_line('p14-r1-1', (11, 25), (11, 30))
        self.add_contour('path-14-1', 'p14-r1-1', closed=False)
        self.add_line('p15-r1-1', (21, 2), (21, 7))
        self.add_contour('path-15-1', 'p15-r1-1', closed=False)
        self.add_line('p16-r1-1', (21, 25), (21, 30))
        self.add_contour('path-16-1', 'p16-r1-1', closed=False)
        self.add_line('p17-r1-1', (2, 11), (7, 11))
        self.add_contour('path-17-1', 'p17-r1-1', closed=False)
        self.add_line('p18-r1-1', (25, 11), (30, 11))
        self.add_contour('path-18-1', 'p18-r1-1', closed=False)
        self.add_line('p19-r1-1', (2, 21), (7, 21))
        self.add_contour('path-19-1', 'p19-r1-1', closed=False)
        self.add_line('p20-r1-1', (25, 21), (30, 21))
        self.add_contour('path-20-1', 'p20-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p12-r1-1')
        self.relate("connect", 'p1-r1-1', 'p13-r1-1')
        self.relate("connect", 'p1-r1-2', 'p13-r1-1')
        self.relate("connect", 'p1-r1-2', 'p15-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p15-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p18-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-1', 'p18-r1-1')
        self.relate("connect", 'p4-r1-1', 'p20-r1-1')
        self.relate("connect", 'p5-r1-1', 'p6-r1-1')
        self.relate("connect", 'p5-r1-1', 'p20-r1-1')
        self.relate("connect", 'p6-r1-1', 'p7-r1-1')
        self.relate("connect", 'p7-r1-1', 'p16-r1-1')
        self.relate("connect", 'p7-r1-2', 'p14-r1-1')
        self.relate("connect", 'p7-r1-2', 'p16-r1-1')
        self.relate("connect", 'p7-r1-3', 'p8-r1-1')
        self.relate("connect", 'p7-r1-3', 'p14-r1-1')
        self.relate("connect", 'p8-r1-1', 'p9-r1-1')
        self.relate("connect", 'p9-r1-1', 'p10-r1-1')
        self.relate("connect", 'p9-r1-1', 'p19-r1-1')
        self.relate("connect", 'p10-r1-1', 'p11-r1-1')
        self.relate("connect", 'p10-r1-1', 'p17-r1-1')
        self.relate("connect", 'p10-r1-1', 'p19-r1-1')
        self.relate("connect", 'p11-r1-1', 'p12-r1-1')
        self.relate("connect", 'p11-r1-1', 'p17-r1-1')
