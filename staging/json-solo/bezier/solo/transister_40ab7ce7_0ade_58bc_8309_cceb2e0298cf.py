"""Transister (electronics), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '40ab7ce7-0ade-58bc-8309-cceb2e0298cf'
SOURCE_PATH = 'icons-json/electronics/transister_40ab7ce7-0ade-58bc-8309-cceb2e0298cf.json'
AUTHOR = 'json_to_solo'

class TransisterElectronics(Solo48):
    icon_id = 'transister-electronics'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('transister', 'electronics')

    def build(self):
        self.add_line('e0', (38, 23), (38, 7))
        self.add_line('e1', (35, 4), (12, 4))
        self.add_line('e2', (10, 6), (10, 23))
        self.add_line('e3', (40, 23), (8, 23))
        self.add_line('e4', (15, 23), (15, 44))
        self.add_line('e5', (24, 23), (24, 44))
        self.add_line('e6', (33, 23), (33, 44))
        self.add_bezier('e7', (38, 7), ((38, 5.727), (37.29, 4.009), (35.66, 4.009)), ((35.58, 4.009), (35.51, 4), (35.44, 4)), ((35.29, 4), (35.15, 4), (35, 4)))
        self.add_bezier('e8', (12, 4), ((10.77, 4), (10.35, 5.145), (10, 6)))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c1')
        self.relate('connect', 'c4', 'c1')
