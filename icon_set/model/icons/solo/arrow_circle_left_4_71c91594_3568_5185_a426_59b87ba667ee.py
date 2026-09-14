"""Arrow circle left 4 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '71c91594-3568-5185-a426-59b87ba667ee'
SOURCE_PATH = 'icons-json/arrows/arrow circle left 4_71c91594-3568-5185-a426-59b87ba667ee.json'
AUTHOR = 'json_to_solo'

class ArrowCircleLeft4(Solo48):
    icon_id = 'arrow-circle-left-4'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'circle', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (13, 24), (41, 24))
        self.add_line('e1', (13, 24), (22, 14))
        self.add_line('e2', (13, 24), (22, 34))
        self.add_bezier('e3', (41, 24), ((41.491, 23.779), (41.992, 23.943), (41.992, 23.206)), ((42, 23.067), (42, 22.936), (42, 22.797)), ((42, 22.794), (42, 22.791), (42, 22.788)), ((42, 22.586), (42, 22.385), (42, 22.184)), ((42, 14.493), (33.164, 6.016), (25.546, 6.016)), ((25.297, 6.016), (25.039, 6), (24.781, 6)), ((24.777, 6), (24.773, 6), (24.769, 6)), ((24.499, 6), (24.229, 6.016), (23.959, 6.016)), ((22.429, 6.016), (20.875, 6.319), (19.41, 6.728)), ((11.85, 8.847), (6.008, 15.597), (6.008, 23.648)), ((6.008, 23.841), (6, 24.043), (6, 24.244)), ((6, 24.247), (6, 24.25), (6, 24.254)), ((6, 24.45), (6.008, 24.646), (6.008, 24.851)), ((6.008, 26.569), (6.401, 28.32), (6.949, 29.948)), ((9.477, 37.377), (16.808, 41.984), (24.54, 41.984)), ((24.745, 41.984), (24.957, 42), (25.162, 42)), ((25.163, 42), (25.164, 42), (25.165, 42)), ((25.23, 42), (25.302, 41.992), (25.366, 41.992)), ((30.513, 41.992), (35.954, 39.095), (38.662, 34.694)), ((39.905, 32.665), (40.419, 30.291), (41, 28)))
        self.add_contour('c0', 'e0', 'e3')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
