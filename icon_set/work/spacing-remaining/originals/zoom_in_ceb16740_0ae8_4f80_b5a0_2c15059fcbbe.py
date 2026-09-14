"""Zoom in (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ceb16740-0ae8-4f80-b5a0-2c15059fcbbe'
SOURCE_PATH = 'icons-json/interface-essential/zoom in_ceb16740-0ae8-4f80-b5a0-2c15059fcbbe.json'
AUTHOR = 'json_to_solo'

class ZoomInInterfaceEssential(Solo48):
    icon_id = 'zoom-in-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('zoom', 'in', 'interface-essential')

    def build(self):
        self.add_line('e0', (42, 42), (33, 32))
        self.add_line('e1', (22, 14), (22, 29))
        self.add_line('e2', (13, 22), (29, 22))
        self.add_arc('e3-top', (6, 22), (38, 22), radius_x=16)
        self.add_arc('e3-bottom', (38, 22), (6, 22), radius_x=16)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'e3')
