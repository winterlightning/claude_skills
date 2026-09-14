"""Double arrow 1 left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b2acc3d0-a3e7-5607-990d-3617d23e1ebe'
SOURCE_PATH = 'icons-json/arrows/double arrow 1 left_b2acc3d0-a3e7-5607-990d-3617d23e1ebe.json'
AUTHOR = 'json_to_solo'

class DoubleArrow1Left(Solo48):
    icon_id = 'double-arrow-1-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('double', 'arrow', 'left', 'arrows')

    def build(self):
        self.add_line('sym-e0', (19, 40), (4, 24))
        self.add_line('sym-e1', (4, 24), (19, 8))
        self.add_line('sym-e2', (19, 24), (44, 24))
        self.add_line('sym-e3', (19, 24), (34, 8))
        self.add_line('sym-e4', (19, 24), (34, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3')
        self.add_contour('sym-c3', 'sym-e4')
        self.relate('connect', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
