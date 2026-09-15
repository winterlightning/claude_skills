"""Bluetooth (networks), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35a7bebd-1171-5051-82f6-db63c9d31c11'
SOURCE_PATH = 'pictographic-primitives/networks/bluetooth_35a7bebd-1171-5051-82f6-db63c9d31c11.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class BluetoothNetworks(Solo48):
    icon_id = 'bluetooth-networks'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('bluetooth', 'networks')

    def build(self):
        self.add_line('e0', (8, 14), (40, 34))
        self.add_line('e1', (40, 34), (24, 44))
        self.add_line('e2', (24, 44), (24, 4))
        self.add_line('e3', (24, 4), (40, 14))
        self.add_line('e4', (40, 14), (9, 33))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4')
