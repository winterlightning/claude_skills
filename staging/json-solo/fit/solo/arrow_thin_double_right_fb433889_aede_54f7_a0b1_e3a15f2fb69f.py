"""Arrow thin double right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb433889-aede-54f7-a0b1-e3a15f2fb69f'
SOURCE_PATH = 'icons-json/arrows/arrow thin double right_fb433889-aede-54f7-a0b1-e3a15f2fb69f.json'
AUTHOR = 'json_to_solo'

class ArrowThinDoubleRightArrows(Solo48):
    icon_id = 'arrow-thin-double-right-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thin', 'double', 'right', 'arrows')

    def build(self):
        self.add_line('sym-e0', (29, 8), (44, 24))
        self.add_line('sym-e1', (44, 24), (29, 40))
        self.add_line('sym-e2', (29, 24), (4, 24))
        self.add_line('sym-e3', (29, 24), (14, 40))
        self.add_line('sym-e4', (29, 24), (14, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3')
        self.add_contour('sym-c3', 'sym-e4')
        self.relate('connect', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
