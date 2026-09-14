"""Picker take (design), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4f371c6-c5e7-45dd-8d80-8cefea43094a'
SOURCE_PATH = 'icons-json/design/picker take_b4f371c6-c5e7-45dd-8d80-8cefea43094a.json'
AUTHOR = 'json_to_solo'

class PickerTakeDesign(Solo48):
    icon_id = 'picker-take-design'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('picker', 'take', 'design')

    def build(self):
        self.add_line('e0', (8, 16), (15, 16))
        self.add_line('e1', (40, 16), (33, 16))
        self.add_line('e2', (15, 16), (33, 16))
        self.add_line('e3', (15, 16), (15, 28))
        self.add_line('e4', (20, 31), (20, 33))
        self.add_line('e5', (28, 33), (28, 31))
        self.add_line('e6', (33, 28), (33, 16))
        self.add_line('e7', (15, 16), (15, 8))
        self.add_line('e8', (33, 9), (33, 16))
        self.add_bezier('e9', (15, 28), ((15, 29.373), (17.867, 29.773), (19.52, 30.573)), ((19.964, 30.791), (19.644, 30.764), (20, 31)))
        self.add_bezier('e10', (20, 33), ((20.356, 33.236), (20.907, 33.591), (21.369, 33.8)), ((22.756, 34.427), (25.138, 34.427), (26.542, 33.827)), ((27.076, 33.6), (27.644, 33.264), (28, 33)))
        self.add_bezier('e11', (28, 31), ((28.32, 30.764), (27.964, 30.791), (28.391, 30.573)), ((30.044, 29.736), (33, 29.436), (33, 28)))
        self.add_bezier('e12', (15, 8), ((15, 6.318), (19.164, 4.009), (22.364, 4.009)), ((22.434, 4.009), (22.487, 4), (22.557, 4)), ((22.558, 4), (22.559, 4), (22.56, 4)), ((22.898, 4), (23.236, 4.009), (23.591, 4.009)), ((27.716, 4.009), (33, 6.845), (33, 9)))
        self.add_bezier('e13', (22, 39), ((20.364, 40.436), (17.831, 41.845), (20.711, 43.355)), ((21.333, 43.673), (22.276, 43.991), (23.2, 43.991)), ((23.323, 43.991), (23.428, 44), (23.55, 44)), ((23.552, 44), (23.554, 44), (23.556, 44)), ((23.68, 44), (23.804, 43.991), (23.929, 43.991)), ((24.729, 43.991), (25.564, 43.709), (26.116, 43.436)), ((28.836, 42.127), (26.916, 40.464), (25.404, 39.118)), ((25.049, 38.8), (23.609, 37.527), (23.484, 37.527)), ((23.058, 37.864), (22.427, 38.664), (22, 39)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11', 'e6')
        self.add_contour('c4', 'e7', 'e12', 'e8')
        self.add_contour('c5', 'e13', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
