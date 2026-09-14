"""Bluetooth (networks), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '222af285-7f62-4cb6-b105-310d0892074c'
SOURCE_PATH = 'icons-json/networks/bluetooth_222af285-7f62-4cb6-b105-310d0892074c.json'
AUTHOR = 'json_to_solo'

class Bluetooth222af285(Solo48):
    icon_id = 'bluetooth-222af285'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('bluetooth', 'networks')

    def build(self):
        self.add_line('e0', (8, 17), (21, 24))
        self.add_line('e1', (9, 30), (21, 24))
        self.add_line('e2', (21, 24), (40, 34))
        self.add_line('e3', (40, 34), (21, 44))
        self.add_line('e4', (21, 44), (21, 24))
        self.add_line('e5', (21, 24), (21, 4))
        self.add_line('e6', (21, 4), (40, 14))
        self.add_line('e7', (40, 14), (21, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4')
        self.add_contour('c3', 'e5', 'e6', 'e7')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
