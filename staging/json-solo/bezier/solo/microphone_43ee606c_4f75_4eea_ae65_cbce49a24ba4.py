"""Microphone (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '43ee606c-4f75-4eea-ae65-cbce49a24ba4'
SOURCE_PATH = 'icons-json/audio/microphone_43ee606c-4f75-4eea-ae65-cbce49a24ba4.json'
AUTHOR = 'json_to_solo'

class Microphone43ee606c(Solo48):
    icon_id = 'microphone-43ee606c'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('microphone', 'audio')

    def build(self):
        self.add_line('e0', (20, 20), (15, 20))
        self.add_line('e1', (15, 14), (21, 14))
        self.add_line('e2', (24, 37), (24, 44))
        self.add_line('e3', (15, 12), (15, 21))
        self.add_line('e4', (33, 22), (33, 12))
        self.add_bezier('e5', (8, 21), ((8, 21.455), (8.01, 22.182), (8.01, 22.636)), ((8.01, 24.373), (8.48, 26.136), (9.19, 27.736)), ((11.64, 33.318), (17.42, 36.736), (24, 36.727)), ((30.53, 36.718), (36.36, 33.445), (38.87, 27.891)), ((39.43, 26.673), (39.99, 25.191), (39.99, 23.845)), ((39.99, 23.782), (40, 23.709), (40, 23.636)), ((40, 22.845), (40, 21.791), (40, 21)))
        self.add_bezier('e6', (33, 12), ((33, 7.964), (29.28, 4.018), (24.66, 4.018)), ((24.434, 4.018), (24.207, 4), (23.971, 4)), ((23.967, 4), (23.964, 4), (23.96, 4)), ((23.81, 4.009), (23.65, 4.009), (23.5, 4.018)), ((18.86, 4.018), (15, 7.918), (15, 12)))
        self.add_bezier('e7', (15, 21), ((15, 24.1), (15.57, 27), (18.32, 29.127)), ((19.7, 30.2), (21.44, 30.818), (23.25, 30.964)), ((28.97, 31.4), (33, 27.009), (33, 22)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e6', 'e3', 'e7', 'e4', closed=True)
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c2')
