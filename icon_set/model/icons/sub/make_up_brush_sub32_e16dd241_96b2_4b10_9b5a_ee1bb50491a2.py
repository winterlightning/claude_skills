"""Independent 32px profile of make-up-brush.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e16dd241-96b2-4b10-9b5a-ee1bb50491a2'
SOURCE_PATH = 'pictographic-primitives/beauty/make up brush_e16dd241-96b2-4b10-9b5a-ee1bb50491a2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e16dd241-96b2-4b10-9b5a-ee1bb50491a2', 'pictographic-primitives/beauty/make up brush_e16dd241-96b2-4b10-9b5a-ee1bb50491a2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/make-up-brush',)
SOLO_SOURCE_ICON_IDS = ('make-up-brush',)
REFERENCE_EXPORT_SHA256 = '15b5e36562673a9e61b4b1b34483fb391015a4ffa272fc1542839c4c3c08da9b'

class Drawing(Sub32):
    icon_id = 'make-up-brush-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'beauty'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (5, 8), ((5, 4), (11, 2), (16, 2)))
        self.add_bezier('p1-r1-2', (16, 2), ((21, 2), (27, 4), (27, 8)))
        self.add_line('p1-r1-3', (27, 8), (22, 13))
        self.add_line('p1-r1-4', (22, 13), (16, 13))
        self.add_line('p1-r1-5', (16, 13), (10, 13))
        self.add_line('p1-r1-6', (10, 13), (5, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_bezier('p2-r1-1', (10, 13), ((10, 16), (12, 18), (13, 19)))
        self.add_line('p2-r1-2', (13, 19), (13, 26))
        self.add_arc('p2-r1-3', (13, 26), (16, 30), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('p2-r1-4', (16, 30), (20, 26), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p2-r1-5', (20, 26), (20, 19))
        self.add_bezier('p2-r1-6', (20, 19), ((20, 18), (22, 16), (22, 13)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (16, 8), (16, 13))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-6')
        self.relate("connect", 'p1-r1-4', 'p2-r1-6')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p3-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
