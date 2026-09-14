"""3 d box corner (technology), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24eacefe-dd6d-5abc-8f9f-cbf83f22e180'
SOURCE_PATH = 'icons-json/technology/3 d box corner_24eacefe-dd6d-5abc-8f9f-cbf83f22e180.json'
AUTHOR = 'json_to_solo'

class Icon3DBoxCornerTechnology(Solo48):
    icon_id = 'icon-3-d-box-corner-technology'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('d', 'box', 'corner', 'technology')

    def build(self):
        self.add_line('sym-e0', (24, 28), (24, 42))
        self.add_line('sym-e1', (24, 42), (36, 35))
        self.add_line('sym-e2', (36, 35), (36, 22))
        self.add_line('sym-e3', (24, 14), (24, 6))
        self.add_line('sym-e4', (24, 28), (36, 21))
        self.add_line('sym-e5', (36, 21), (24, 14))
        self.add_line('sym-e6', (24, 14), (12, 21))
        self.add_line('sym-e7', (12, 21), (24, 28))
        self.add_line('sym-e8', (36, 35), (42, 39))
        self.add_line('sym-e9', (24, 42), (12, 35))
        self.add_line('sym-e10', (12, 35), (12, 22))
        self.add_line('sym-e11', (12, 35), (6, 39))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', closed=True)
        self.add_contour('sym-c3', 'sym-e8')
        self.add_contour('sym-c4', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c5', 'sym-e11')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c3')
