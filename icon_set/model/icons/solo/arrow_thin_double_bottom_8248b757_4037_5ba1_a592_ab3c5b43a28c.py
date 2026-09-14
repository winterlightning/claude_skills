"""Arrow thin double bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8248b757-4037-5ba1-a592-ab3c5b43a28c'
SOURCE_PATH = 'icons-json/arrows/arrow thin double bottom_8248b757-4037-5ba1-a592-ab3c5b43a28c.json'
AUTHOR = 'json_to_solo'

class ArrowThinDoubleBottom(Solo48):
    icon_id = 'arrow-thin-double-bottom'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thin', 'double', 'bottom', 'arrows')

    def build(self):
        self.add_line('sym-e0', (40, 29), (24, 44))
        self.add_line('sym-e1', (24, 44), (8, 29))
        self.add_line('sym-e2', (24, 29), (24, 4))
        self.add_line('sym-e3', (24, 29), (8, 14))
        self.add_line('sym-e4', (24, 29), (40, 14))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3')
        self.add_contour('sym-c3', 'sym-e4')
        self.relate('connect', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
