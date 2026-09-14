"""Arrow thick circle top 1 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aafea0c2-ca76-51ce-8e98-1f25087e8091'
SOURCE_PATH = 'icons-json/arrows/arrow thick circle top 1_aafea0c2-ca76-51ce-8e98-1f25087e8091.json'
AUTHOR = 'json_to_solo'

class ArrowThickCircleTop1Arrows(Solo48):
    icon_id = 'arrow-thick-circle-top-1-arrows'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'circle', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (33, 24), (24, 15))
        self.add_line('e1', (15, 24), (24, 15))
        self.add_line('e2', (24, 15), (24, 35))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
