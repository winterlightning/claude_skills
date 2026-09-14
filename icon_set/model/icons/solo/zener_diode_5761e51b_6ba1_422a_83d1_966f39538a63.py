"""Zener diode (electronics), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5761e51b-6ba1-422a-83d1-966f39538a63'
SOURCE_PATH = 'icons-json/electronics/zener diode_5761e51b-6ba1-422a-83d1-966f39538a63.json'
AUTHOR = 'json_to_solo'

class ZenerDiode(Solo48):
    icon_id = 'zener-diode'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('zener', 'diode', 'electronics')

    def build(self):
        self.add_line('e0', (34, 8), (34, 24))
        self.add_line('e1', (4, 24), (14, 24))
        self.add_line('e2', (34, 40), (34, 24))
        self.add_line('e3', (44, 24), (34, 24))
        self.add_line('e4', (14, 8), (14, 40))
        self.add_line('e5', (14, 40), (32, 24))
        self.add_line('e6', (32, 24), (14, 8))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e5', 'e6', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c4')
