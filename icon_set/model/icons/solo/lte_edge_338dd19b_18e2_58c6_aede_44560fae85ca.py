"""Lte edge (mobile), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '338dd19b-18e2-58c6-aede-44560fae85ca'
SOURCE_PATH = 'icons-json/mobile/lte edge_338dd19b-18e2-58c6-aede-44560fae85ca.json'
AUTHOR = 'json_to_solo'

class LteEdge(Solo48):
    icon_id = 'lte-edge'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    aliases = ()
    keywords = ('lte', 'edge', 'mobile')

    def build(self):
        self.add_line('e0', (40, 4), (8, 4))
        self.add_line('e1', (8, 4), (8, 44))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_line('e3', (8, 23), (34, 23))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.relate('connect', 'c1', 'c0')
