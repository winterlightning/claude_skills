"""Heart (romance), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b74d773d-2544-4971-935a-c2f6b85abdcb'
SOURCE_PATH = 'icons-json/romance/heart_b74d773d-2544-4971-935a-c2f6b85abdcb.json'
AUTHOR = 'json_to_solo'

class Heart(Solo48):
    icon_id = 'heart'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('heart', 'romance')

    def build(self):
        self.add_line('e0', (22, 38), (7, 24))
        self.add_line('e1', (22, 11), (24, 13))
        self.add_line('e2', (41, 24), (24, 40))
        self.add_line('e3', (24, 40), (22, 38))
        self.add_arc('e4-1', (7, 24), (4, 18), radius_x=8)
        self.add_arc('e4-2', (4, 18), (14, 8), radius_x=10)
        self.add_line('e4-3', (14, 8), (19, 9))
        self.add_arc('e4-4', (19, 9), (22, 11), radius_x=14, sweep=False)
        self.add_arc('e5-1', (24, 13), (34, 8), radius_x=13)
        self.add_arc('e5-2', (34, 8), (42, 12), radius_x=10)
        self.add_arc('e5-3', (42, 12), (44, 17), radius_x=8)
        self.add_arc('e5-4', (44, 17), (41, 24), radius_x=10)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e1', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e2', 'e3', closed=True)
