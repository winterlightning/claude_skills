"""Up (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa2173f6-e147-4572-8d82-eb4f6eb22c5a'
SOURCE_PATH = 'icons-json/arrows/up_fa2173f6-e147-4572-8d82-eb4f6eb22c5a.json'
AUTHOR = 'json_to_solo'

class UpArrows(Solo48):
    icon_id = 'up-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('up', 'arrows')

    def build(self):
        self.add_line('e0', (33, 10), (38, 6))
        self.add_line('e1', (37, 12), (38, 6))
        self.add_line('e2', (42, 11), (38, 6))
        self.add_bezier('e3', (32, 11), ((32.27, 10.73), (32.705, 10.245), (33, 10)))
        self.add_bezier('e4', (6, 42), ((6.016, 42), (6.033, 41.992), (6.049, 41.992)), ((6.843, 41.992), (7.718, 41.787), (8.495, 41.607)), ((10.475, 41.157), (12.439, 40.732), (14.345, 40.028)), ((27.044, 35.373), (35.094, 25.369), (37, 12)))
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e4', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
