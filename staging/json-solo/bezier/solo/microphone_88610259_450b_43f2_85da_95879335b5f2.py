"""Microphone (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '88610259-450b-43f2-85da-95879335b5f2'
SOURCE_PATH = 'icons-json/audio/microphone_88610259-450b-43f2-85da-95879335b5f2.json'
AUTHOR = 'json_to_solo'

class Microphone(Solo48):
    icon_id = 'microphone'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('microphone', 'audio')

    def build(self):
        self.add_line('e0', (24, 44), (24, 39))
        self.add_line('e1', (15, 20), (15, 11))
        self.add_line('e2', (32, 12), (32, 22))
        self.add_bezier('e3', (8, 25), ((8.22, 26.364), (8.48, 27.736), (9.1, 29.009)), ((11.35, 33.627), (17.35, 37.591), (23, 37.636)), ((23.67, 37.636), (24.33, 38), (25, 38)))
        self.add_bezier('e4', (23, 38), ((23.1, 38.109), (23.92, 38.564), (24, 38.545)), ((24.47, 38.455), (24.56, 37.809), (25, 37.636)), ((25.43, 37.464), (26.74, 37.545), (27.3, 37.473)), ((28.43, 37.327), (29.55, 36.982), (30.62, 36.618)), ((35.47, 34.964), (39.98, 30.182), (39.98, 25.291)), ((39.99, 25.164), (39.99, 25.127), (40, 25)))
        self.add_bezier('e5', (15, 11), ((15, 10.636), (15.28, 10.327), (15.41, 9.964)), ((16.52, 6.891), (19.96, 4.009), (23.68, 4.009)), ((23.759, 4), (23.838, 4), (23.916, 4)), ((23.918, 4), (23.919, 4), (23.92, 4)), ((24.08, 4), (24.24, 4.009), (24.4, 4.009)), ((28.18, 4.009), (31.29, 6.764), (31.95, 10.027)), ((32.1, 10.773), (32, 11.273), (32, 12)))
        self.add_bezier('e6', (32, 22), ((32, 22.264), (31.43, 23.755), (31.29, 24.073)), ((29.82, 27.355), (26.35, 29.418), (22.4, 28.709)), ((17.93, 27.909), (15, 24.027), (15, 20)))
        self.add_contour('c0', 'e3')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e0')
        self.add_contour('c3', 'e1', 'e5', 'e2', 'e6', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c2', 'c1')
