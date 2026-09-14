"""Microphone (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b72da6ab-adc1-4364-be21-8572894c8a90'
SOURCE_PATH = 'icons-json/audio/microphone_b72da6ab-adc1-4364-be21-8572894c8a90.json'
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
        self.add_line('e0', (16, 13), (21, 13))
        self.add_line('e1', (24, 39), (24, 44))
        self.add_line('e2', (16, 11), (16, 20))
        self.add_line('e3', (32, 21), (32, 11))
        self.add_bezier('e4', (8, 19), ((8, 19.591), (8.008, 20.636), (8.008, 21.227)), ((8.008, 30.745), (15.251, 38.491), (24, 38.545)), ((30.4, 38.591), (36.101, 34.436), (38.728, 28.182)), ((39.36, 26.691), (39.992, 24.845), (39.992, 23.173)), ((40, 23.109), (40, 23.036), (40, 22.964)), ((40, 22.1), (40, 20.864), (40, 20)))
        self.add_bezier('e5', (32, 11), ((32, 7.109), (27.848, 4.009), (24.371, 4.009)), ((24.238, 4.009), (24.105, 4), (23.965, 4)), ((23.962, 4), (23.96, 4), (23.958, 4)), ((23.823, 4), (23.688, 4.009), (23.545, 4.018)), ((20.051, 4.018), (16, 7.127), (16, 11)))
        self.add_bezier('e6', (16, 20), ((16, 24.082), (18.509, 27.564), (22.274, 28.545)), ((26.56, 29.655), (32, 26), (32, 21)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5', 'e2', 'e6', 'e3', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
