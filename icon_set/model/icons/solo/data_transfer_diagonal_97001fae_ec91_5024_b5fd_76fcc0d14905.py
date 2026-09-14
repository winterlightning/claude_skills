"""Data transfer diagonal (networks), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97001fae-ec91-5024-b5fd-76fcc0d14905'
SOURCE_PATH = 'icons-json/networks/data transfer diagonal_97001fae-ec91-5024-b5fd-76fcc0d14905.json'
AUTHOR = 'json_to_solo'

class DataTransferDiagonal(Solo48):
    icon_id = 'data-transfer-diagonal'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('data', 'transfer', 'diagonal', 'networks')

    def build(self):
        self.add_line('e0', (27, 4), (40, 4))
        self.add_line('e1', (40, 4), (40, 17))
        self.add_line('e2', (22, 21), (40, 4))
        self.add_line('e3', (8, 29), (8, 44))
        self.add_line('e4', (23, 44), (8, 44))
        self.add_line('e5', (24, 29), (11, 41))
        self.add_line('e6', (11, 41), (8, 44))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5', 'e6')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c0')
