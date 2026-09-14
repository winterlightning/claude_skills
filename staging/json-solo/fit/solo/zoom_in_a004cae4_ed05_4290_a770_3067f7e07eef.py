"""Zoom in (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a004cae4-ed05-4290-a770-3067f7e07eef'
SOURCE_PATH = 'icons-json/interface-essential/zoom in_a004cae4-ed05-4290-a770-3067f7e07eef.json'
AUTHOR = 'json_to_solo'

class ZoomInA004cae4(Solo48):
    icon_id = 'zoom-in-a004cae4'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('zoom', 'in', 'interface-essential')

    def build(self):
        self.add_line('e0', (42, 42), (29, 31))
        self.add_line('e1', (20, 13), (20, 20))
        self.add_line('e2', (13, 20), (20, 20))
        self.add_line('e3', (20, 26), (20, 20))
        self.add_line('e4', (26, 20), (20, 20))
        self.add_arc('e5-top', (6, 20), (34, 20), radius_x=14)
        self.add_arc('e5-bottom', (34, 20), (6, 20), radius_x=14)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c0', 'e5')
