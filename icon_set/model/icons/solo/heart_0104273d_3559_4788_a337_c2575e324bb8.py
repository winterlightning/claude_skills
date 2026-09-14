"""Heart (romance), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0104273d-3559-4788-a337-c2575e324bb8'
SOURCE_PATH = 'icons-json/romance/heart_0104273d-3559-4788-a337-c2575e324bb8.json'
AUTHOR = 'json_to_solo'

class Heart(Solo48):
    icon_id = 'heart-0104273d'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('heart', 'romance')

    def build(self):
        self.add_line('e0', (24, 14), (20, 11))
        self.add_line('e1', (7, 24), (24, 40))
        self.add_line('e2', (24, 40), (39, 26))
        self.add_arc('e3-1', (20, 11), (14, 8), radius_x=11, sweep=False)
        self.add_arc('e3-2', (14, 8), (4, 18), radius_x=10, sweep=False)
        self.add_arc('e3-3', (4, 18), (7, 24), radius_x=8, sweep=False)
        self.add_arc('e4-1', (39, 26), (44, 17), radius_x=11, sweep=False)
        self.add_arc('e4-2', (44, 17), (40, 10), radius_x=9, sweep=False)
        self.add_arc('e4-3', (40, 10), (34, 8), radius_x=10, sweep=False)
        self.add_arc('e4-4', (34, 8), (24, 14), radius_x=13, sweep=False)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e1', 'e2', 'e4-1', 'e4-2', 'e4-3', 'e4-4', closed=True)
