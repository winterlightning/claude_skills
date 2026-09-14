"""Diode (electronics), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d318b74-8678-4d78-ba8b-db8cb33830b5'
SOURCE_PATH = 'icons-json/electronics/diode_5d318b74-8678-4d78-ba8b-db8cb33830b5.json'
AUTHOR = 'json_to_solo'

class DiodeElectronics(Solo48):
    icon_id = 'diode-electronics'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('diode', 'electronics')

    def build(self):
        self.add_line('sym-e0', (4, 24), (13, 24))
        self.add_line('sym-e1', (13, 24), (13, 38))
        self.add_bezier('sym-e2', (13, 38), ((13.327, 38.443), (13.609, 38.545), (14, 39)))
        self.add_line('sym-e3', (14, 39), (33, 24))
        self.add_bezier('sym-e4', (33, 24), ((33.609, 24), (34.391, 24), (35, 24)))
        self.add_line('sym-e5', (35, 24), (44, 24))
        self.add_line('sym-e6', (35, 40), (35, 24))
        self.add_line('sym-e7', (35, 24), (35, 8))
        self.add_line('sym-e8', (13, 24), (13, 10))
        self.add_bezier('sym-e9', (13, 10), ((13.327, 9.557), (13.609, 9.455), (14, 9)))
        self.add_line('sym-e10', (14, 9), (33, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c2', 'sym-e8', 'sym-e9', 'sym-e10')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
