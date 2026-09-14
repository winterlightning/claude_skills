"""Pie (design), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0869dbd7-3c0e-5868-9ca5-c53d7c8e2cdf'
SOURCE_PATH = 'icons-json/design/pie_0869dbd7-3c0e-5868-9ca5-c53d7c8e2cdf.json'
AUTHOR = 'json_to_solo'

class PieDesign(Solo48):
    icon_id = 'pie-design'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pie', 'design')

    def build(self):
        self.add_line('e0', (44, 24), (24, 24))
        self.add_line('e1', (24, 24), (10, 38))
        self.add_line('e2', (24, 24), (24, 4))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c1', 'e3')
        self.relate('connect', 'c2', 'e3')
