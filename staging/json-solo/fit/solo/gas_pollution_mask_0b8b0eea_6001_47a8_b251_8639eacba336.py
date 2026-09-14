"""Gas pollution mask (protection), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0b8b0eea-6001-47a8-b251-8639eacba336'
SOURCE_PATH = 'icons-json/protection/gas pollution mask_0b8b0eea-6001-47a8-b251-8639eacba336.json'
AUTHOR = 'json_to_solo'

class GasPollutionMaskProtection(Solo48):
    icon_id = 'gas-pollution-mask-protection'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('gas', 'pollution', 'mask', 'protection')

    def build(self):
        self.add_line('e0', (8, 28), (8, 20))
        self.add_line('e1', (40, 28), (40, 20))
        self.add_line('e2', (40, 20), (31, 20))
        self.add_arc('e3', (10, 35), (38, 35), radius_x=20)
        self.add_arc('e4-1', (10, 35), (24, 44), radius_x=16, sweep=False)
        self.add_arc('e4-2', (24, 44), (38, 35), radius_x=16, sweep=False)
        self.add_arc('e5', (10, 35), (8, 28), radius_x=20)
        self.add_arc('e6', (38, 35), (40, 28), radius_x=19, sweep=False)
        self.add_arc('e7-1', (31, 20), (18, 14), radius_x=18)
        self.add_arc('e7-2', (18, 14), (8, 20), radius_x=11)
        self.add_arc('e8-1', (40, 20), (24, 4), radius_x=17, sweep=False)
        self.add_arc('e8-2', (24, 4), (8, 19), radius_x=17, sweep=False)
        self.add_line('e8-3', (8, 19), (8, 20))
        self.add_contour('c0', 'e3')
        self.add_contour('c1', 'e4-1', 'e4-2')
        self.add_contour('c2', 'e5', 'e0')
        self.add_contour('c3', 'e6', 'e1')
        self.add_contour('c4', 'e2', 'e7-1', 'e7-2')
        self.add_contour('c5', 'e8-1', 'e8-2', 'e8-3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
