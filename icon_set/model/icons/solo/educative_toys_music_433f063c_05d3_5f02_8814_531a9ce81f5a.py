"""Educative toys music (music), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '433f063c-05d3-5f02-8814-531a9ce81f5a'
SOURCE_PATH = 'icons-json/music/educative toys music_433f063c-05d3-5f02-8814-531a9ce81f5a.json'
AUTHOR = 'json_to_solo'

class EducativeToysMusic(Solo48):
    icon_id = 'educative-toys-music'
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
        self.add_bezier('e5', (40, 6), ((39.747, 5.373), (39.328, 4.609), (39, 4)))
        self.add_bezier('e6', (21, 9), ((19.072, 9.591), (20, 11.255), (20, 13)))
        self.add_bezier('e7', (20, 37), ((20, 37.873), (19.781, 38.6), (19.503, 39.436)), ((18.585, 42.209), (15.739, 43.991), (13.061, 43.991)), ((13.003, 43.991), (12.945, 44), (12.887, 44)), ((12.886, 44), (12.885, 44), (12.884, 44)), ((10.712, 44), (8.017, 42.182), (8.017, 39.573)), ((8.008, 39.427), (8.008, 39.282), (8, 39.145)), ((8, 39.142), (8, 39.138), (8, 39.134)), ((8, 38.902), (8.017, 38.678), (8.017, 38.455)), ((8.017, 37.8), (8.345, 37), (8.632, 36.436)), ((9.844, 34.064), (12.404, 32.527), (14.939, 32.964)), ((16.867, 33.291), (18.484, 34.782), (20, 36)))
        self.add_bezier('e8', (38, 29), ((36.442, 28.055), (35.225, 27.973), (33.423, 28.464)), ((29.996, 29.391), (26.855, 34.009), (29.263, 37.627)), ((31.554, 41.073), (36.564, 39.809), (38.703, 36.918)), ((39.225, 36.209), (39.983, 35.155), (39.983, 34.191)), ((39.992, 34.109), (39.992, 34.027), (40, 33.945)), ((40, 33.627), (40, 33.3), (40, 32.973)), ((40, 32.573), (40, 32.173), (40, 31.773)), ((40, 31.3), (40, 30.473), (40, 30)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e8', 'e4', closed=True)
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
