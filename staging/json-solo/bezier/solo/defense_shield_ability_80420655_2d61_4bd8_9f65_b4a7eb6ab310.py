"""Defense shield ability (video-games), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80420655-2d61-4bd8-9f65-b4a7eb6ab310'
SOURCE_PATH = 'icons-json/video-games/defense shield ability_80420655-2d61-4bd8-9f65-b4a7eb6ab310.json'
AUTHOR = 'json_to_solo'

class DefenseShieldAbilityVideoGames(Solo48):
    icon_id = 'defense-shield-ability-video-games'
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
        self.add_bezier('e5', (10, 9), ((9.318, 9.264), (8.008, 9.209), (8.008, 10.2)), ((8.008, 10.255), (8, 9.945), (8, 10)))
        self.add_bezier('e6', (8, 19), ((8, 27.327), (12.093, 35.164), (18.156, 40.2)), ((19.057, 40.945), (22.939, 44), (23.983, 44)), ((23.984, 44), (23.984, 44), (23.985, 44)), ((24.026, 44), (24.06, 44), (24.101, 44)), ((25.027, 44), (29.128, 40.827), (29.971, 40.091)), ((35.781, 35.027), (39.983, 27.036), (39.983, 18.818)), ((39.992, 18.727), (39.992, 19.091), (40, 19)))
        self.add_bezier('e7', (40, 9), ((39.907, 8.9), (39.874, 9.182), (39.781, 9.082)), ((39.385, 8.6), (38.514, 9.109), (38, 9)))
        self.add_bezier('e8', (34, 8), ((31.743, 7.509), (29.097, 7.136), (27, 6)))
        self.add_bezier('e9', (24, 4), ((23.84, 4), (23.672, 4), (23.512, 4)), ((23.259, 4), (23.057, 4.464), (22.855, 4.636)), ((22.265, 5.136), (21.465, 5.445), (20.783, 5.764)), ((18.585, 6.8), (16.324, 7.5), (14, 8)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9', closed=True)
