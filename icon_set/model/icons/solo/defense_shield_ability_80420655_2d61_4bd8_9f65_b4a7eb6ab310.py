"""Defense shield ability (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80420655-2d61-4bd8-9f65-b4a7eb6ab310'
SOURCE_PATH = 'icons-json/video-games/defense shield ability_80420655-2d61-4bd8-9f65-b4a7eb6ab310.json'
AUTHOR = 'json_to_solo'

class DefenseShieldAbility(Solo48):
    icon_id = 'defense-shield-ability'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('defense', 'shield', 'ability', 'video-games')

    def build(self):
        self.add_line('e0', (14, 8), (10, 9))
        self.add_line('e1', (8, 10), (8, 19))
        self.add_line('e2', (40, 19), (40, 9))
        self.add_line('e3', (38, 9), (34, 8))
        self.add_line('e4', (27, 6), (24, 4))
        self.add_arc('e5', (10, 9), (8, 10), radius_x=2, sweep=False)
        self.add_arc('e6-1', (8, 19), (24, 44), radius_x=28, sweep=False)
        self.add_arc('e6-2', (24, 44), (40, 19), radius_x=29, sweep=False)
        self.add_line('e7', (40, 9), (38, 9))
        self.add_arc('e8', (34, 8), (27, 6), radius_x=23, sweep=False)
        self.add_line('e9', (24, 4), (14, 8))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6-1', 'e6-2', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9', closed=True)
