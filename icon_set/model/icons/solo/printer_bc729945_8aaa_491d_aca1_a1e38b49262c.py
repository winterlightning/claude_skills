"""Printer (devices), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bc729945-8aaa-491d-aca1-a1e38b49262c'
SOURCE_PATH = 'icons-json/devices/printer_bc729945-8aaa-491d-aca1-a1e38b49262c.json'
AUTHOR = 'gpt-6'

class Printer(Solo48):
    icon_id = 'printer'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    aliases = ()
    keywords = ('printer', 'devices')

    def build(self):
        self.add_line('e0', (34, 18), (34, 10))
        self.add_line('e1', (33, 9), (29, 4))
        self.add_line('e3', (14, 5), (14, 18))
        self.add_line('e4', (35, 30), (38, 44))
        self.add_line('e5', (38, 44), (9, 44))
        self.add_line('e6', (9, 44), (13, 30))
        self.add_line('e7', (40, 18), (40, 28))
        self.add_line('e8', (38, 30), (10, 30))
        self.add_line('e9', (8, 28), (8, 18))
        self.add_line('e10', (8, 18), (40, 18))
        self.add_line('e11', (34, 10), (33, 9))
        self.add_line('e12', (29, 4), (16, 4))
        self.add_arc('e13', (16, 4), (14, 5), radius_x=17, radius_y=17, large_arc=False, sweep=False)
        self.add_arc('e14', (40, 28), (38, 30), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('e15', (10, 30), (8, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('c0', 'e0', 'e11', 'e1', 'e12', 'e13', 'e3', closed=False)
        self.add_contour('c1', 'e4', 'e5', 'e6', closed=False)
        self.add_contour('c2', 'e7', 'e14', 'e8', 'e15', 'e9', 'e10', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
