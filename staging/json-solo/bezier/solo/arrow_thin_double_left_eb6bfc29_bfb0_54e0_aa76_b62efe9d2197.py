"""Arrow thin double left (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb6bfc29-bfb0-54e0-aa76-b62efe9d2197'
SOURCE_PATH = 'icons-json/arrows/arrow thin double left_eb6bfc29-bfb0-54e0-aa76-b62efe9d2197.json'
AUTHOR = 'json_to_solo'

class ArrowThinDoubleLeftArrows(Solo48):
    icon_id = 'arrow-thin-double-left-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thin', 'double', 'left', 'arrows')

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
