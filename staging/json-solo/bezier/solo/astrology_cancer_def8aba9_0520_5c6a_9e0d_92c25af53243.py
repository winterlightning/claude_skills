"""Batch-05/astrology cancer (culture), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'def8aba9-0520-5c6a-9e0d-92c25af53243'
SOURCE_PATH = 'icons-json/culture/batch-05/astrology cancer_def8aba9-0520-5c6a-9e0d-92c25af53243.json'
AUTHOR = 'json_to_solo'

class Batch05AstrologyCancer(Solo48):
    icon_id = 'batch-05-astrology-cancer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('batch', 'astrology', 'cancer', 'culture')

    def build(self):
        self.add_line('e0', (32, 17), (31, 21))
        self.add_line('e1', (8, 22), (40, 22))
        self.add_bezier('e2', (6, 6), ((6.916, 6.229), (7.857, 6.45), (8.7, 6.892)), ((10.23, 7.685), (11.465, 8.921), (12.521, 10.255)), ((17.422, 16.456), (17.855, 25.833), (15.164, 33.041)), ((13.658, 37.058), (11.214, 40.691), (7, 42)))
        self.add_bezier('e3', (42, 6), ((41.697, 6), (41.386, 6), (41.084, 6)), ((41.043, 6), (38.523, 7.415), (38.318, 7.563)), ((35.725, 9.387), (33.974, 12.03), (32.812, 14.943)), ((32.591, 15.483), (32.115, 16.435), (32, 17)))
        self.add_bezier('e4', (31, 21), ((30.648, 22.767), (31.241, 24.507), (31.413, 26.275)), ((31.904, 31.274), (33.843, 37.361), (38.048, 40.445)), ((39.022, 41.157), (39.887, 41.607), (41, 42)))
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e3', 'e0', 'e4')
        self.add_contour('c2', 'e1')
