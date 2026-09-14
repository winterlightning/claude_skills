"""Arrow double left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3666dac-329a-571b-9047-59dc76fac708'
SOURCE_PATH = 'icons-json/arrows/arrow double left_e3666dac-329a-571b-9047-59dc76fac708.json'
AUTHOR = 'json_to_solo'

class ArrowDoubleLeftArrows(Solo48):
    icon_id = 'arrow-double-left-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'double', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (19, 9), (4, 24))
        self.add_line('e1', (4, 24), (20, 40))
        self.add_line('e2', (44, 8), (28, 24))
        self.add_line('e3', (28, 24), (44, 40))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
