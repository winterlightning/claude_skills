"""Shottkey diode (electronics), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e1', (30, 18), ((30.286, 18.286), (29.705, 18.722), (30, 19)))
        self.add_bezier('sym-e2', (30, 19), ((30.442, 19.417), (31.591, 19.55), (32, 20)))
        self.add_bezier('sym-e3', (32, 20), ((32.63, 20.687), (32.769, 22.231), (32, 23)))
        self.add_line('sym-e4', (32, 23), (23, 32))
        self.add_bezier('sym-e5', (23, 32), ((22.828, 32.172), (22.237, 32.951), (22, 33)))
        self.add_bezier('sym-e6', (22, 33), ((20.225, 33.385), (19.072, 31.072), (18, 30)))
        self.add_line('sym-e7', (18, 30), (6, 42))
        self.add_bezier('sym-e8', (18, 30), ((16.928, 28.928), (14.615, 27.775), (15, 26)))
        self.add_bezier('sym-e9', (15, 26), ((15.049, 25.763), (15.828, 25.172), (16, 25)))
        self.add_line('sym-e10', (16, 25), (25, 16))
        self.add_bezier('sym-e11', (25, 16), ((25.769, 15.231), (27.313, 15.37), (28, 16)))
        self.add_bezier('sym-e12', (28, 16), ((28.45, 16.409), (28.583, 17.558), (29, 18)))
        self.add_bezier('sym-e13', (29, 18), ((29.278, 18.295), (29.714, 17.714), (30, 18)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c1', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
