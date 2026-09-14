"""End point triangle arrow (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5bbb4936-8e64-448b-a983-a3110668f576'
SOURCE_PATH = 'icons-json/arrows/end point triangle arrow_5bbb4936-8e64-448b-a983-a3110668f576.json'
AUTHOR = 'json_to_solo'

class EndPointTriangleArrowArrows(Solo48):
    icon_id = 'end-point-triangle-arrow-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('end', 'point', 'triangle', 'arrow', 'arrows')

    def build(self):
        self.add_line('e0', (4, 24), (33, 24))
        self.add_line('e1', (29, 8), (33, 24))
        self.add_line('e2', (33, 24), (29, 40))
        self.add_line('e3', (29, 40), (44, 24))
        self.add_line('e4', (44, 24), (29, 8))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
