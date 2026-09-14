"""Flame (fire), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '949214a5-cd3d-46da-8416-617e71942aa0'
SOURCE_PATH = 'icons-json/fire/flame_949214a5-cd3d-46da-8416-617e71942aa0.json'
AUTHOR = 'json_to_solo'

class Flame949214a5(Solo48):
    icon_id = 'flame-949214a5'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'fire'
    aliases = ()
    keywords = ('flame', 'fire')

    def build(self):
        self.add_line('e0', (31, 26), (33, 22))
        self.add_line('e1', (27, 6), (23, 4))
        self.add_arc('e2', (33, 22), (27, 6), radius_x=13, sweep=False)
        self.add_arc('e3-1', (23, 4), (22, 13), radius_x=11)
        self.add_line('e3-2', (22, 13), (10, 23))
        self.add_line('e3-3', (10, 23), (8, 30))
        self.add_arc('e3-4', (8, 30), (12, 39), radius_x=13, sweep=False)
        self.add_arc('e3-5', (12, 39), (23, 44), radius_x=17, sweep=False)
        self.add_line('e3-6', (23, 44), (30, 43))
        self.add_arc('e3-7', (30, 43), (35, 40), radius_x=17, sweep=False)
        self.add_arc('e3-8', (35, 40), (40, 30), radius_x=13, sweep=False)
        self.add_arc('e3-9', (40, 30), (39, 24), radius_x=35, sweep=False)
        self.add_arc('e3-10', (39, 24), (33, 29), radius_x=10)
        self.add_arc('e3-11', (33, 29), (31, 26), radius_x=2)
        self.add_contour('c0', 'e0', 'e2', 'e1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9', 'e3-10', 'e3-11', closed=True)
