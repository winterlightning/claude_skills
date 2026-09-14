"""Data transfer vertical (networks), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '54e0e79f-4cc9-4499-9605-6b950ba9fec1'
SOURCE_PATH = 'icons-json/networks/data transfer vertical_54e0e79f-4cc9-4499-9605-6b950ba9fec1.json'
AUTHOR = 'json_to_solo'

class DataTransferVertical54e0e79f(Solo48):
    icon_id = 'data-transfer-vertical-54e0e79f'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('data', 'transfer', 'vertical', 'networks')

    def build(self):
        self.add_line('e0', (8, 11), (16, 4))
        self.add_line('e1', (16, 29), (16, 4))
        self.add_line('e2', (25, 11), (16, 4))
        self.add_line('e3', (32, 19), (32, 44))
        self.add_line('e4', (23, 37), (32, 44))
        self.add_line('e5', (40, 37), (32, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
