"""Music clef (music), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b729f41-589f-5522-afeb-95562d668db3'
SOURCE_PATH = 'icons-json/music/music clef_7b729f41-589f-5522-afeb-95562d668db3.json'
AUTHOR = 'json_to_solo'

class MusicClefMusic(Solo48):
    icon_id = 'music-clef-music'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'music'
    aliases = ()
    keywords = ('music', 'clef')

    def build(self):
        self.add_line('e0', (26, 23), (30, 35))
        self.add_line('e1', (20, 19), (24, 18))
        self.add_line('e2', (24, 18), (26, 23))
        self.add_line('e3', (30, 35), (30, 39))
        self.add_line('e4', (22, 9), (24, 18))
        self.add_arc('e5-1', (30, 35), (38, 32), radius_x=27, sweep=False)
        self.add_arc('e5-2', (38, 32), (40, 29), radius_x=4, sweep=False)
        self.add_line('e5-3', (40, 29), (39, 26))
        self.add_arc('e5-4', (39, 26), (37, 25), radius_x=7, sweep=False)
        self.add_arc('e5-5', (37, 25), (26, 23), radius_x=25, sweep=False)
        self.add_arc('e6-1', (30, 35), (14, 33), radius_x=44)
        self.add_arc('e6-2', (14, 33), (8, 27), radius_x=7)
        self.add_arc('e6-3', (8, 27), (20, 19), radius_x=14)
        self.add_arc('e7', (26, 23), (20, 29), radius_x=6, sweep=False)
        self.add_line('e8-1', (30, 39), (29, 42))
        self.add_arc('e8-2', (29, 42), (24, 44), radius_x=8)
        self.add_line('e8-3', (24, 44), (19, 43))
        self.add_line('e8-4', (19, 43), (18, 40))
        self.add_arc('e9-1', (24, 18), (36, 9), radius_x=17, sweep=False)
        self.add_arc('e9-2', (36, 9), (31, 4), radius_x=5, sweep=False)
        self.add_line('e9-3', (31, 4), (24, 6))
        self.add_arc('e9-4', (24, 6), (22, 9), radius_x=3, sweep=False)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e0')
        self.add_contour('c1', 'e6-1', 'e6-2', 'e6-3', 'e1', 'e2', 'e7')
        self.add_contour('c2', 'e3', 'e8-1', 'e8-2', 'e8-3', 'e8-4')
        self.add_contour('c3', 'e4', 'e9-1', 'e9-2', 'e9-3', 'e9-4', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
