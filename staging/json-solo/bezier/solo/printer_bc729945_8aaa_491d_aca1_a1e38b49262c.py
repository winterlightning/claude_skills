"""Printer (devices), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc729945-8aaa-491d-aca1-a1e38b49262c'
SOURCE_PATH = 'icons-json/devices/printer_bc729945-8aaa-491d-aca1-a1e38b49262c.json'
AUTHOR = 'json_to_solo'

class PrinterDevices(Solo48):
    icon_id = 'printer-devices'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    aliases = ()
    keywords = ('printer', 'devices')

    def build(self):
        self.add_line('e0', (34, 18), (34, 10))
        self.add_line('e1', (33, 9), (29, 4))
        self.add_line('e2', (28, 4), (16, 4))
        self.add_line('e3', (14, 5), (14, 18))
        self.add_line('e4', (35, 30), (38, 44))
        self.add_line('e5', (38, 44), (9, 44))
        self.add_line('e6', (9, 44), (13, 30))
        self.add_line('e7', (40, 18), (40, 28))
        self.add_line('e8', (38, 30), (10, 30))
        self.add_line('e9', (8, 28), (8, 18))
        self.add_line('e10', (8, 18), (40, 18))
        self.add_bezier('e11', (34, 10), ((33.731, 9.7), (33.278, 9.3), (33, 9)))
        self.add_bezier('e12', (29, 4), ((28.722, 4), (28.278, 4), (28, 4)))
        self.add_bezier('e13', (16, 4), ((15.411, 4.318), (14.657, 4.582), (14, 5)))
        self.add_bezier('e14', (40, 28), ((40, 28.236), (39.992, 28.118), (39.992, 28.355)), ((39.992, 28.4), (39.992, 28.445), (39.983, 28.491)), ((39.983, 29.264), (38.724, 30), (38, 30)))
        self.add_bezier('e15', (10, 30), ((9.141, 30), (8.008, 28.845), (8.008, 28.055)), ((8.008, 28.036), (8, 28.009), (8, 27.991)), ((8, 27.873), (8, 28.118), (8, 28)))
        self.add_contour('c0', 'e0', 'e11', 'e1', 'e12', 'e2', 'e13', 'e3')
        self.add_contour('c1', 'e4', 'e5', 'e6')
        self.add_contour('c2', 'e7', 'e14', 'e8', 'e15', 'e9', 'e10', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
