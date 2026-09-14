"""Power button (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '169cceb8-f596-5e38-8241-0caa55d29dc4'
SOURCE_PATH = 'icons-json/interface-essential/power button_169cceb8-f596-5e38-8241-0caa55d29dc4.json'
AUTHOR = 'json_to_solo'

class PowerButtonInterfaceEssential(Solo48):
    icon_id = 'power-button-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('power', 'button', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 4), (24, 23))
        self.add_arc('e1-1', (18, 10), (11, 16), radius_x=17, sweep=False)
        self.add_arc('e1-2', (11, 16), (8, 26), radius_x=19, sweep=False)
        self.add_line('e1-3', (8, 26), (10, 35))
        self.add_arc('e1-4', (10, 35), (14, 40), radius_x=19, sweep=False)
        self.add_line('e1-5', (14, 40), (18, 43))
        self.add_line('e1-6', (18, 43), (24, 44))
        self.add_line('e1-7', (24, 44), (30, 43))
        self.add_line('e1-8', (30, 43), (34, 40))
        self.add_arc('e1-9', (34, 40), (38, 35), radius_x=18, sweep=False)
        self.add_line('e1-10', (38, 35), (40, 26))
        self.add_arc('e1-11', (40, 26), (37, 16), radius_x=19, sweep=False)
        self.add_arc('e1-12', (37, 16), (30, 9), radius_x=18, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', 'e1-10', 'e1-11', 'e1-12')
