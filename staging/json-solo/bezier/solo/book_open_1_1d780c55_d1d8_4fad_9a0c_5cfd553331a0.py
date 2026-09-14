"""Book open 1 (content), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d780c55-d1d8-4fad-9a0c-5cfd553331a0'
SOURCE_PATH = 'icons-json/content/book open 1_1d780c55-d1d8-4fad-9a0c-5cfd553331a0.json'
AUTHOR = 'json_to_solo'

class BookOpen11d780c55(Solo48):
    icon_id = 'book-open-1-1d780c55'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'content')

    def build(self):
        self.add_line('e0', (6, 8), (6, 35))
        self.add_line('e1', (8, 38), (17, 39))
        self.add_line('e2', (42, 8), (42, 35))
        self.add_line('e3', (40, 38), (31, 39))
        self.add_bezier('e4', (24, 10), ((23.525, 9.272), (23.059, 8.643), (22.405, 8.054)), ((20.097, 6), (16.505, 6.008), (13.593, 6.008)), ((13.271, 6.008), (12.948, 6), (12.626, 6)), ((12.621, 6), (12.616, 6), (12.611, 6)), ((12.226, 6), (11.85, 6.016), (11.474, 6.016)), ((10.533, 6.016), (7.604, 6), (6.925, 6.442)), ((6.393, 6.785), (6, 7.563), (6, 8.185)), ((6, 8.275), (6, 7.91), (6, 8)))
        self.add_bezier('e5', (6, 35), ((6, 36.604), (6.282, 37.828), (8, 38)))
        self.add_bezier('e6', (17, 39), ((19.7, 39.27), (21.979, 40.282), (24, 42)))
        self.add_bezier('e7', (24, 10), ((24.475, 9.272), (24.941, 8.643), (25.595, 8.054)), ((27.903, 6), (31.495, 6.008), (34.407, 6.008)), ((34.735, 6.008), (35.062, 6), (35.389, 6)), ((35.774, 6), (36.15, 6.016), (36.526, 6.016)), ((37.467, 6.016), (40.396, 6), (41.075, 6.442)), ((41.607, 6.785), (42, 7.563), (42, 8.185)), ((42, 8.275), (42, 7.91), (42, 8)))
        self.add_bezier('e8', (42, 35), ((42, 36.604), (41.718, 37.828), (40, 38)))
        self.add_bezier('e9', (31, 39), ((28.3, 39.27), (26.021, 40.282), (24, 42)))
        self.add_contour('c0', 'e4', 'e0', 'e5', 'e1', 'e6')
        self.add_contour('c1', 'e7', 'e2', 'e8', 'e3', 'e9')
