"""Educative toys music (music), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '433f063c-05d3-5f02-8814-531a9ce81f5a'
SOURCE_PATH = 'icons-json/music/educative toys music_433f063c-05d3-5f02-8814-531a9ce81f5a.json'
AUTHOR = 'json_to_solo'

class EducativeToysMusicMusic(Solo48):
    icon_id = 'educative-toys-music-music'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'music'
    aliases = ()
    keywords = ('educative', 'toys', 'music')

    def build(self):
        self.add_line('e0', (40, 31), (40, 6))
        self.add_line('e1', (39, 4), (21, 9))
        self.add_line('e2', (20, 13), (20, 37))
        self.add_line('e3', (40, 14), (20, 20))
        self.add_line('e4', (40, 30), (38, 29))
        self.add_arc('e5', (40, 6), (39, 4), radius_x=18, sweep=False)
        self.add_line('e6', (21, 9), (20, 13))
        self.add_arc('e7-1', (20, 37), (13, 44), radius_x=7)
        self.add_arc('e7-2', (13, 44), (8, 39), radius_x=5)
        self.add_arc('e7-3', (8, 39), (13, 33), radius_x=7)
        self.add_arc('e7-4', (13, 33), (20, 36), radius_x=8)
        self.add_arc('e8-1', (38, 29), (29, 37), radius_x=7, sweep=False)
        self.add_arc('e8-2', (29, 37), (40, 34), radius_x=6, sweep=False)
        self.add_arc('e8-3', (40, 34), (40, 30), radius_x=33)
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7-1', 'e7-2', 'e7-3', 'e7-4')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e8-1', 'e8-2', 'e8-3', 'e4', closed=True)
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
