"""Data transfer three back forth back (networks), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db8e7561-89f7-4546-b8de-e5bd680cb29c'
SOURCE_PATH = 'icons-json/networks/data transfer three back forth back_db8e7561-89f7-4546-b8de-e5bd680cb29c.json'
AUTHOR = 'json_to_solo'

class DataTransferThreeBackForthBackNetworks(Solo48):
    icon_id = 'data-transfer-three-back-forth-back-networks'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('data', 'transfer', 'three', 'back', 'forth', 'networks')

    def build(self):
        self.add_line('e0', (33, 8), (38, 13))
        self.add_line('e1', (4, 13), (38, 13))
        self.add_line('e2', (33, 17), (38, 13))
        self.add_line('e3', (18, 20), (12, 24))
        self.add_line('e4', (17, 28), (12, 24))
        self.add_line('e5', (44, 24), (12, 24))
        self.add_line('e6', (32, 31), (38, 36))
        self.add_line('e7', (4, 36), (38, 36))
        self.add_line('e8', (32, 40), (38, 36))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
