"""Text format capital (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bfb4c541-a3af-5992-a52c-5f432b9045cd'
SOURCE_PATH = 'icons-json/interface-essential/text format capital_bfb4c541-a3af-5992-a52c-5f432b9045cd.json'
AUTHOR = 'json_to_solo'

class TextFormatCapitalInterfaceEssential(Solo48):
    icon_id = 'text-format-capital-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'format', 'capital', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (35, 30), (13, 30))
        self.add_bezier('sym-e1', (24, 4), ((23.975, 4), (24.025, 4), (24, 4)))
        self.add_bezier('sym-e2', (24, 4), ((23.882, 4), (24.118, 4.009), (24, 4)))
        self.add_bezier('sym-e3', (24, 4), ((23.933, 4), (23.059, 4), (23, 4)))
        self.add_bezier('sym-e4', (23, 4), ((21.24, 4), (21.488, 6.609), (21, 8)))
        self.add_line('sym-e5', (21, 8), (8, 44))
        self.add_bezier('sym-e6', (24, 4), ((24.025, 4), (23.975, 4), (24, 4)))
        self.add_bezier('sym-e7', (24, 4), ((24.118, 4), (23.882, 4.009), (24, 4)))
        self.add_bezier('sym-e8', (24, 4), ((24.067, 4), (24.941, 4), (25, 4)))
        self.add_bezier('sym-e9', (25, 4), ((26.76, 4), (26.512, 6.609), (27, 8)))
        self.add_line('sym-e10', (27, 8), (40, 44))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c2', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
