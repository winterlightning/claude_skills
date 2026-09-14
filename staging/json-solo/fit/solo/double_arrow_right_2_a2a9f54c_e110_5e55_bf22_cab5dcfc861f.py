"""Double arrow right 2 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2a9f54c-e110-5e55-bf22-cab5dcfc861f'
SOURCE_PATH = 'icons-json/arrows/double arrow right 2_a2a9f54c-e110-5e55-bf22-cab5dcfc861f.json'
AUTHOR = 'json_to_solo'

class DoubleArrowRight2Arrows(Solo48):
    icon_id = 'double-arrow-right-2-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('double', 'arrow', 'right', 'arrows')

    def build(self):
        self.add_line('sym-e0', (26, 24), (24, 21))
        self.add_line('sym-e1', (24, 21), (8, 4))
        self.add_line('sym-e2', (23, 4), (39, 22))
        self.add_arc('sym-e3', (39, 22), (40, 24), radius_x=3)
        self.add_arc('sym-e8', (40, 24), (39, 26), radius_x=3)
        self.add_line('sym-e9', (39, 26), (23, 44))
        self.add_line('sym-e10', (26, 24), (24, 27))
        self.add_line('sym-e11', (24, 27), (8, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c2', 'sym-e10', 'sym-e11')
        self.relate('connect', 'sym-c0', 'sym-c2')
