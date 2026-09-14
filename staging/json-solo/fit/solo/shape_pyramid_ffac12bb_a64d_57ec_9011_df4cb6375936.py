"""Shape pyramid (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffac12bb-a64d-57ec-9011-df4cb6375936'
SOURCE_PATH = 'icons-json/design/shape pyramid_ffac12bb-a64d-57ec-9011-df4cb6375936.json'
AUTHOR = 'json_to_solo'

class ShapePyramidDesign(Solo48):
    icon_id = 'shape-pyramid-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('shape', 'pyramid', 'design')

    def build(self):
        self.add_line('e0', (4, 40), (24, 29))
        self.add_line('e1', (24, 29), (44, 40))
        self.add_line('e2', (44, 40), (4, 40))
        self.add_line('e3', (24, 29), (24, 8))
        self.add_line('e4', (24, 8), (44, 40))
        self.add_line('e5', (24, 8), (4, 40))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
        self.add_contour('c1', 'e3', 'e4')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c2')
