"""Play first playlist (music), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f1883242-d820-40f5-bdc6-92fbacecb89f'
SOURCE_PATH = 'icons-json/music/play first playlist_f1883242-d820-40f5-bdc6-92fbacecb89f.json'
AUTHOR = 'json_to_solo'

class PlayFirstPlaylistMusic(Solo48):
    icon_id = 'play-first-playlist-music'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'music'
    aliases = ()
    keywords = ('play', 'first', 'playlist', 'music')

    def build(self):
        self.add_line('e0', (15, 8), (19, 13))
        self.add_line('e1', (4, 28), (4, 22))
        self.add_line('e2', (11, 13), (19, 13))
        self.add_line('e3', (15, 18), (19, 13))
        self.add_line('e4', (27, 10), (44, 10))
        self.add_line('e5', (27, 20), (44, 20))
        self.add_line('e6', (27, 30), (44, 30))
        self.add_line('e7', (4, 40), (44, 40))
        self.add_bezier('e8', (4, 22), ((4, 18.39), (6.364, 14.97), (9.336, 13.63)), ((9.882, 13.39), (10.4, 13), (11, 13)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e8', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6')
        self.add_contour('c6', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
