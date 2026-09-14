"""Arrow thick down 3 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4c495be8-9a08-470b-bacc-5efd7480755f'
SOURCE_PATH = 'icons-json/arrows/arrow thick down 3_4c495be8-9a08-470b-bacc-5efd7480755f.json'
AUTHOR = 'json_to_solo'

class ArrowThickDown3Arrows(Solo48):
    icon_id = 'arrow-thick-down-3-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'down', 'arrows')

    def build(self):
        self.add_line('e0', (28, 27), (36, 19))
        self.add_line('e1', (37, 18), (42, 23))
        self.add_line('e2', (42, 25), (25, 41))
        self.add_line('e3', (23, 42), (6, 24))
        self.add_line('e4', (6, 23), (10, 19))
        self.add_line('e5', (12, 19), (18, 26))
        self.add_line('e6', (19, 26), (19, 6))
        self.add_line('e7', (19, 6), (28, 6))
        self.add_line('e8', (28, 6), (28, 27))
        self.add_bezier('e9', (36, 19), ((36.278, 18.722), (36.705, 18.278), (37, 18)))
        self.add_bezier('e10', (42, 23), ((42, 23.213), (42, 23.607), (42, 23.812)), ((42, 23.959), (42, 24.131), (42, 24.27)), ((42, 24.458), (42, 24.82), (42, 25)))
        self.add_bezier('e11', (25, 41), ((24.599, 41.376), (24.344, 41.984), (23.648, 41.984)), ((23.607, 41.992), (23.566, 41.992), (23.525, 42)), ((23.411, 42), (23.115, 42), (23, 42)))
        self.add_bezier('e12', (6, 24), ((6, 23.73), (6, 23.27), (6, 23)))
        self.add_bezier('e13', (10, 19), ((10.9, 18.681), (11.116, 18.714), (12, 19)))
        self.add_bezier('e14', (18, 26), ((18.27, 26.27), (18.73, 25.73), (19, 26)))
        self.add_contour('c0', 'e0', 'e9', 'e1', 'e10', 'e2', 'e11', 'e3', 'e12', 'e4', 'e13', 'e5', 'e14', 'e6', 'e7', 'e8', closed=True)
