"""Data transfer horizontal (networks), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '72d23812-3e76-4ef8-8e5d-604c11965659'
SOURCE_PATH = 'icons-json/networks/data transfer horizontal_72d23812-3e76-4ef8-8e5d-604c11965659.json'
AUTHOR = 'json_to_solo'

class DataTransferHorizontalNetworks(Solo48):
    icon_id = 'data-transfer-horizontal-networks'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('data', 'transfer', 'horizontal', 'networks')

    def build(self):
        self.add_line('e0', (10, 8), (4, 17))
        self.add_line('e1', (10, 26), (4, 17))
        self.add_line('e2', (29, 17), (4, 17))
        self.add_line('e3', (38, 23), (44, 31))
        self.add_line('e4', (18, 31), (44, 31))
        self.add_line('e5', (38, 40), (44, 31))
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
