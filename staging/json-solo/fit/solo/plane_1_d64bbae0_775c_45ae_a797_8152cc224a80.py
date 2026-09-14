"""Plane 1 (travel), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd64bbae0-775c-45ae-a797-8152cc224a80'
SOURCE_PATH = 'icons-json/travel/plane 1_d64bbae0-775c-45ae-a797-8152cc224a80.json'
AUTHOR = 'json_to_solo'

class Plane1D64bbae0(Solo48):
    icon_id = 'plane-1-d64bbae0'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('plane', 'travel')

    def build(self):
        self.add_line('e0', (30, 20), (27, 16))
        self.add_line('e1', (27, 16), (19, 9))
        self.add_line('e2', (14, 8), (18, 21))
        self.add_line('e3', (7, 18), (4, 18))
        self.add_line('e4', (4, 18), (7, 24))
        self.add_line('e5', (7, 24), (4, 30))
        self.add_line('e6', (4, 30), (7, 30))
        self.add_line('e7', (12, 27), (18, 27))
        self.add_line('e8', (18, 27), (14, 40))
        self.add_line('e9', (14, 40), (18, 40))
        self.add_line('e10', (20, 38), (30, 28))
        self.add_line('e11', (30, 28), (39, 28))
        self.add_line('e12', (39, 20), (30, 20))
        self.add_line('e13-1', (19, 9), (15, 8))
        self.add_arc('e13-2', (15, 8), (14, 8), radius_x=17)
        self.add_arc('e14-1', (18, 21), (11, 21), radius_x=51)
        self.add_arc('e14-2', (11, 21), (7, 18), radius_x=9)
        self.add_arc('e15', (7, 30), (12, 27), radius_x=9)
        self.add_arc('e16', (18, 40), (20, 38), radius_x=3, sweep=False)
        self.add_arc('e17-1', (39, 28), (44, 24), radius_x=5, sweep=False)
        self.add_arc('e17-2', (44, 24), (39, 20), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e13-1', 'e13-2', 'e2', 'e14-1', 'e14-2', 'e3', 'e4', 'e5', 'e6', 'e15', 'e7', 'e8', 'e9', 'e16', 'e10', 'e11', 'e17-1', 'e17-2', 'e12', closed=True)
