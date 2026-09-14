"""Shottkey diode (electronics), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8f23851-7ae9-4939-bf46-aba37ee712d0'
SOURCE_PATH = 'icons-json/electronics/shottkey diode_a8f23851-7ae9-4939-bf46-aba37ee712d0.json'
AUTHOR = 'json_to_solo'

class ShottkeyDiodeElectronics(Solo48):
    icon_id = 'shottkey-diode-electronics'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('shottkey', 'diode', 'electronics')

    def build(self):
        self.add_line('sym-e0', (42, 6), (30, 18))
        self.add_line('sym-e1', (30, 18), (30, 19))
        self.add_line('sym-e2', (30, 19), (32, 20))
        self.add_arc('sym-e3', (32, 20), (32, 23), radius_x=2)
        self.add_line('sym-e4', (32, 23), (23, 32))
        self.add_line('sym-e5', (23, 32), (22, 33))
        self.add_arc('sym-e6', (22, 33), (18, 30), radius_x=6, sweep=False)
        self.add_line('sym-e7', (18, 30), (6, 42))
        self.add_arc('sym-e8', (18, 30), (15, 26), radius_x=6, sweep=False)
        self.add_arc('sym-e9', (15, 26), (16, 25), radius_x=2)
        self.add_line('sym-e10', (16, 25), (25, 16))
        self.add_arc('sym-e11', (25, 16), (28, 16), radius_x=2)
        self.add_line('sym-e12', (28, 16), (29, 18))
        self.add_line('sym-e13', (29, 18), (30, 18))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c1', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
