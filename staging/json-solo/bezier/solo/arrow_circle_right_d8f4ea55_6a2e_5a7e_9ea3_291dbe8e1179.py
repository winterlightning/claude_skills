"""Arrow circle right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd8f4ea55-6a2e-5a7e-9ea3-291dbe8e1179'
SOURCE_PATH = 'icons-json/arrows/arrow circle right_d8f4ea55-6a2e-5a7e-9ea3-291dbe8e1179.json'
AUTHOR = 'json_to_solo'

class ArrowCircleRightArrows(Solo48):
    icon_id = 'arrow-circle-right-arrows'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'circle', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (20, 35), (29, 26))
        self.add_line('e1', (29, 23), (20, 14))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e3', (29, 26), ((29.827, 25.173), (29.4, 23.864), (29, 23)))
        self.add_contour('c0', 'e0', 'e3', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
