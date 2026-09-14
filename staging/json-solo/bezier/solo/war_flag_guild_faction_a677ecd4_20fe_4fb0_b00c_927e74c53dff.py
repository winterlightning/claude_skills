"""War flag guild faction (video-games), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a677ecd4-20fe-4fb0-b00c-927e74c53dff'
SOURCE_PATH = 'icons-json/video-games/war flag guild faction_a677ecd4-20fe-4fb0-b00c-927e74c53dff.json'
AUTHOR = 'json_to_solo'

class WarFlagGuildFactionVideoGames(Solo48):
    icon_id = 'war-flag-guild-faction-video-games'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('war', 'flag', 'guild', 'faction', 'video-games')

    def build(self):
        self.add_line('e0', (11, 44), (11, 29))
        self.add_line('e1', (11, 11), (40, 11))
        self.add_line('e2', (40, 11), (34, 20))
        self.add_line('e3', (34, 20), (40, 29))
        self.add_line('e4', (40, 29), (11, 29))
        self.add_line('e5', (11, 11), (11, 29))
        self.add_arc('e6-top', (8, 7), (14, 7), radius_x=3)
        self.add_arc('e6-bottom', (14, 7), (8, 7), radius_x=3)
        self.add_bezier('e7', (11, 11), ((11, 10.745), (10.796, 10.409), (10.728, 10.127)), ((10.661, 9.9), (11.067, 9.227), (11, 9)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e7')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'e6')
