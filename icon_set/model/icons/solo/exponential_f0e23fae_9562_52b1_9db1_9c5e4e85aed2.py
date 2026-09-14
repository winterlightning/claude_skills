"""Exponential (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0e23fae-9562-52b1-9db1-9c5e4e85aed2'
SOURCE_PATH = 'icons-json/interface-essential/exponential_f0e23fae-9562-52b1-9db1-9c5e4e85aed2.json'
AUTHOR = 'json_to_solo'

class ExponentialInterfaceEssential(Solo48):
    icon_id = 'exponential-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('exponential', 'interface-essential')

    def build(self):
        self.add_line('e0', (44, 8), (34, 18))
        self.add_line('e1', (35, 8), (44, 18))
        self.add_line('e2', (4, 25), (9, 21))
        self.add_line('e3', (9, 21), (9, 40))
        self.add_line('e4', (4, 40), (13, 40))
        self.add_line('e5', (30, 33), (30, 27))
        self.add_arc('e6-1', (30, 27), (20, 22), radius_x=6, sweep=False)
        self.add_arc('e6-2', (20, 22), (17, 33), radius_x=13, sweep=False)
        self.add_arc('e6-3', (17, 33), (24, 40), radius_x=7, sweep=False)
        self.add_arc('e6-4', (24, 40), (30, 33), radius_x=7, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5', 'e6-1', 'e6-2', 'e6-3', 'e6-4', closed=True)
        self.relate('connect', 'c2', 'c3')
