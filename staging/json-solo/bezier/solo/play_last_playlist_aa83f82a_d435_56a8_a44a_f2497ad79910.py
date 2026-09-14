"""Play last playlist (music), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa83f82a-d435-56a8-a44a-f2497ad79910'
SOURCE_PATH = 'icons-json/music/play last playlist_aa83f82a-d435-56a8-a44a-f2497ad79910.json'
AUTHOR = 'json_to_solo'

class PlayLastPlaylistMusic(Solo48):
    icon_id = 'play-last-playlist-music'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'music'
    aliases = ()
    keywords = ('play', 'last', 'playlist', 'music')

    def build(self):
        self.add_line('e0', (25, 13), (44, 13))
        self.add_line('e1', (26, 26), (41, 26))
        self.add_line('e2', (25, 38), (44, 38))
        self.add_line('e3', (9, 11), (17, 21))
        self.add_line('e4', (18, 27), (8, 38))
        self.add_line('e5', (4, 38), (4, 13))
        self.add_bezier('e6', (4, 13), ((4, 12.856), (4, 12.496), (4, 12.352)), ((4, 10.816), (4.664, 8), (5.727, 8)), ((5.741, 8), (5.754, 8), (5.768, 8)), ((6.644, 8), (8.293, 10.165), (9, 11)))
        self.add_bezier('e7', (17, 21), ((18.073, 22.248), (19.627, 25.176), (18, 27)))
        self.add_bezier('e8', (8, 38), ((7.391, 38.688), (6.427, 40), (5.645, 40)), ((5.644, 40), (5.643, 40), (5.642, 40)), ((5.58, 40), (5.508, 40), (5.436, 40)), ((5.364, 39.984), (5.3, 39.984), (5.227, 39.968)), ((4.364, 39.968), (4.355, 38.672), (4, 38)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e6', 'e3', 'e7', 'e4', 'e8', 'e5', closed=True)
