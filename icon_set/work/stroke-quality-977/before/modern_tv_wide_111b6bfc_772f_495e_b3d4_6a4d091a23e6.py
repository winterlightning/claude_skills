"""Modern tv wide (tv), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '111b6bfc-772f-495e-b3d4-6a4d091a23e6'
SOURCE_PATH = 'pictographic-primitives/tv/modern tv wide_111b6bfc-772f-495e-b3d4-6a4d091a23e6.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ModernTvWide(Solo48):
    icon_id = 'modern-tv-wide'
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
        self.add_arc('sym-e3', (43, 8), (44, 10), radius_x=3)
        self.add_line('sym-e5', (44, 10), (44, 33))
        self.add_arc('sym-e7', (44, 33), (43, 35), radius_x=3)
        self.add_line('sym-e8', (43, 35), (39, 35))
        self.add_line('sym-e9', (7, 40), (9, 35))
        self.add_line('sym-e10', (9, 35), (5, 35))
        self.add_arc('sym-e11', (5, 35), (4, 33), radius_x=3)
        self.add_line('sym-e13', (4, 33), (4, 10))
        self.add_arc('sym-e15', (4, 10), (5, 8), radius_x=3)
        self.add_line('sym-e16', (5, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e7', 'sym-e8')
        self.add_contour('sym-c2', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e15', 'sym-e16')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
