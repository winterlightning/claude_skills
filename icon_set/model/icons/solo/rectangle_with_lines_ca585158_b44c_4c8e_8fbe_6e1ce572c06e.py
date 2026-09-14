"""Rectangle with lines (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca585158-b44c-4c8e-8fbe-6e1ce572c06e'
SOURCE_PATH = 'icons-json/state/rectangle with lines_ca585158-b44c-4c8e-8fbe-6e1ce572c06e.json'
AUTHOR = 'json_to_solo'

class RectangleWithLines(Solo48):
    icon_id = 'rectangle-with-lines'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('rectangle', 'with', 'lines', 'state')

    def build(self):
        self.add_line('e0', (16, 15), (31, 15))
        self.add_line('e1', (16, 23), (31, 23))
        self.add_line('e2', (16, 32), (27, 32))
        self.add_line('e3', (40, 4), (8, 4))
        self.add_line('e4', (8, 4), (8, 44))
        self.add_line('e5', (8, 44), (40, 44))
        self.add_line('e6', (40, 44), (40, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e5', 'e6', closed=True)
