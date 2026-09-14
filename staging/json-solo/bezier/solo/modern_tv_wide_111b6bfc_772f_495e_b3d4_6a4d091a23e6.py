"""Modern tv wide (tv), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '111b6bfc-772f-495e-b3d4-6a4d091a23e6'
SOURCE_PATH = 'icons-json/tv/modern tv wide_111b6bfc-772f-495e-b3d4-6a4d091a23e6.json'
AUTHOR = 'json_to_solo'

class ModernTvWideTv(Solo48):
    icon_id = 'modern-tv-wide-tv'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tv'
    aliases = ()
    keywords = ('modern', 'tv', 'wide')

    def build(self):
        self.add_line('sym-e0', (9, 35), (39, 35))
        self.add_line('sym-e1', (39, 35), (41, 40))
        self.add_line('sym-e2', (24, 8), (43, 8))
        self.add_bezier('sym-e3', (43, 8), ((43.427, 8.49), (44, 9.2), (44, 10)))
        self.add_bezier('sym-e4', (44, 10), ((44, 10.13), (44, 9.87), (44, 10)))
        self.add_line('sym-e5', (44, 10), (44, 33))
        self.add_bezier('sym-e6', (44, 33), ((44, 33.11), (44, 32.89), (44, 33)))
        self.add_bezier('sym-e7', (44, 33), ((44, 33.78), (43.427, 34.5), (43, 35)))
        self.add_line('sym-e8', (43, 35), (39, 35))
        self.add_line('sym-e9', (7, 40), (9, 35))
        self.add_line('sym-e10', (9, 35), (5, 35))
        self.add_bezier('sym-e11', (5, 35), ((4.573, 34.5), (4, 33.78), (4, 33)))
        self.add_bezier('sym-e12', (4, 33), ((4, 32.89), (4, 33.11), (4, 33)))
        self.add_line('sym-e13', (4, 33), (4, 10))
        self.add_bezier('sym-e14', (4, 10), ((4, 9.87), (4, 10.13), (4, 10)))
        self.add_bezier('sym-e15', (4, 10), ((4, 9.2), (4.573, 8.49), (5, 8)))
        self.add_line('sym-e16', (5, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8')
        self.add_contour('sym-c2', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
