"""Reality vr (technology), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0284d3a8-c0bf-450e-8702-f6e30af3b263'
SOURCE_PATH = 'icons-json/technology/reality vr_0284d3a8-c0bf-450e-8702-f6e30af3b263.json'
AUTHOR = 'json_to_solo'

class RealityVrTechnology(Solo48):
    icon_id = 'reality-vr-technology'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('reality', 'vr', 'technology')

    def build(self):
        self.add_line('e0', (9, 29), (18, 29))
        self.add_line('e1', (30, 29), (38, 29))
        self.add_line('e2', (6, 26), (6, 17))
        self.add_line('e3', (8, 13), (10, 13))
        self.add_line('e4', (40, 29), (41, 28))
        self.add_line('e5', (42, 26), (42, 17))
        self.add_line('e6', (38, 13), (10, 13))
        self.add_line('e7', (28, 6), (20, 6))
        self.add_bezier('e8', (18, 29), ((19.301, 29), (20.277, 27.862), (21.292, 27.256)), ((22.077, 26.79), (22.985, 26.561), (23.902, 26.561)), ((24.867, 26.553), (25.874, 26.806), (26.684, 27.338)), ((27.625, 27.952), (28.773, 29), (30, 29)))
        self.add_bezier('e9', (38, 29), ((38.548, 29), (39.452, 28.992), (40, 29)))
        self.add_bezier('e10', (9, 29), ((9.663, 36.118), (16.252, 41.992), (23.509, 41.992)), ((23.598, 41.992), (23.686, 42), (23.775, 42)), ((23.776, 42), (23.778, 42), (23.779, 42)), ((24.106, 42), (24.442, 41.992), (24.769, 41.992)), ((30.529, 41.992), (35.708, 38.105), (38.179, 33.057)), ((38.834, 31.724), (39.566, 30.399), (40, 29)))
        self.add_bezier('e11', (9, 29), ((7.781, 28.427), (6, 27.395), (6, 25.743)), ((6, 25.71), (6, 26.033), (6, 26)))
        self.add_bezier('e12', (6, 17), ((6.475, 15.421), (6.503, 13.826), (8, 13)))
        self.add_bezier('e13', (41, 28), ((41.417, 27.337), (42, 26.823), (42, 26.005)), ((42, 25.882), (42, 26.123), (42, 26)))
        self.add_bezier('e14', (42, 17), ((42, 14.865), (39.857, 13), (38, 13)))
        self.add_bezier('e15', (38, 13), ((37.501, 11.92), (36.935, 11.22), (36.248, 10.246)), ((34.546, 7.816), (31.47, 6.008), (28.443, 6.008)), ((28.385, 6.008), (28.328, 6), (28.271, 6)), ((28.214, 6), (28.057, 6), (28, 6)))
        self.add_bezier('e16', (20, 6), ((16.768, 6), (13.421, 7.8), (11.588, 10.418)), ((10.958, 11.326), (10.458, 12.002), (10, 13)))
        self.add_contour('c0', 'e0', 'e8', 'e1', 'e9')
        self.add_contour('c1', 'e10')
        self.add_contour('c2', 'e11', 'e2', 'e12', 'e3')
        self.add_contour('c3', 'e4', 'e13', 'e5', 'e14')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e15', 'e7', 'e16')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
