"""Music clef (music), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b729f41-589f-5522-afeb-95562d668db3'
SOURCE_PATH = 'icons-json/music/music clef_7b729f41-589f-5522-afeb-95562d668db3.json'
AUTHOR = 'json_to_solo'

class MusicClef(Solo48):
    icon_id = 'music-clef'
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
        self.add_bezier('e5', (30, 35), ((35.58, 33.664), (39.96, 32.264), (39.96, 29.055)), ((39.98, 28.991), (39.98, 28.927), (40, 28.864)), ((40, 28.86), (40, 28.857), (40, 28.853)), ((40, 28.629), (39.96, 28.406), (39.96, 28.182)), ((39.96, 25.873), (36.32, 23.927), (31.48, 23.345)), ((29.62, 23.127), (28.02, 23.036), (26, 23)))
        self.add_bezier('e6', (30, 35), ((27.78, 35.009), (25.48, 34.991), (23.26, 34.845)), ((15.28, 34.336), (8.02, 31.573), (8.02, 27.7)), ((8.02, 27.566), (8, 27.432), (8, 27.297)), ((8, 27.295), (8, 27.293), (8, 27.291)), ((8.02, 27.227), (8.02, 27.164), (8.04, 27.091)), ((8.04, 23.645), (14.64, 21.055), (20, 19)))
        self.add_bezier('e7', (26, 23), ((20.98, 24.964), (19.22, 25.964), (20, 29)))
        self.add_bezier('e8', (30, 39), ((30, 39.373), (29.72, 40.236), (29.6, 40.6)), ((29.14, 41.918), (28.8, 42.927), (26.06, 43.655)), ((25.52, 43.791), (24.82, 43.991), (24.16, 43.991)), ((24.022, 43.991), (23.884, 44), (23.727, 44)), ((23.725, 44), (23.723, 44), (23.72, 44)), ((23.4, 43.991), (23.08, 43.991), (22.76, 43.982)), ((18.98, 43.982), (18.02, 41.255), (18, 40)))
        self.add_bezier('e9', (24, 18), ((30.56, 15.336), (36.46, 12.482), (35.92, 8.127)), ((35.74, 6.755), (34.76, 5.055), (32.04, 4.273)), ((31.8, 4.2), (31.2, 4), (30.92, 4)), ((30.918, 4), (30.916, 4), (30.913, 4)), ((30.775, 4), (30.617, 4), (30.46, 4)), ((24.88, 4), (21.46, 6.755), (22, 9)))
        self.add_contour('c0', 'e5', 'e0')
        self.add_contour('c1', 'e6', 'e1', 'e2', 'e7')
        self.add_contour('c2', 'e3', 'e8')
        self.add_contour('c3', 'e4', 'e9', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
