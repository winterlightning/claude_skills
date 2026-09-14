"""Keyboard arrow left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e1067c8-00df-510b-aad0-0a8a854e4b8c'
SOURCE_PATH = 'icons-json/interface-essential/keyboard arrow left_8e1067c8-00df-510b-aad0-0a8a854e4b8c.json'
AUTHOR = 'json_to_solo'

class KeyboardArrowLeft8e1067c8(Solo48):
    icon_id = 'keyboard-arrow-left-8e1067c8'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 30), (13, 21))
        self.add_line('e1', (13, 40), (4, 31))
        self.add_line('e2', (4, 31), (34, 31))
        self.add_line('e3', (33, 8), (25, 8))
        self.add_bezier('e4', (34, 31), ((38.027, 31), (41.036, 29.42), (42.909, 25.38)), ((43.536, 24.04), (43.982, 22.41), (43.982, 20.88)), ((43.991, 20.8), (43.991, 20.72), (44, 20.64)), ((44, 20.639), (44, 20.638), (44, 20.636)), ((44, 20.558), (43.991, 20.479), (43.991, 20.4)), ((43.991, 15.01), (40.282, 10.35), (35.8, 8.65)), ((34.955, 8.34), (33.9, 8), (33, 8)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e4', 'e3')
