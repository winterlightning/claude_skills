"""Zoom out (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd05e7aa2-4c1e-43d5-8943-5f63cebcd390'
SOURCE_PATH = 'icons-json/interface-essential/zoom out_d05e7aa2-4c1e-43d5-8943-5f63cebcd390.json'
AUTHOR = 'json_to_solo'

class ZoomOutInterfaceEssential(Solo48):
    icon_id = 'zoom-out-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('zoom', 'out', 'interface-essential')

    def build(self):
        self.add_line('e0', (42, 42), (34, 34))
        self.add_line('e1', (13, 22), (30, 22))
        self.add_arc('e2-top', (6, 22), (38, 22), radius_x=16)
        self.add_arc('e2-bottom', (38, 22), (6, 22), radius_x=16)
        self.add_bezier('e3', (34, 34), ((33.566, 33.566), (33.27, 32.548), (33, 32)))
        self.add_contour('c0', 'e0', 'e3')
        self.add_contour('c1', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.relate('connect', 'c0', 'e2')
