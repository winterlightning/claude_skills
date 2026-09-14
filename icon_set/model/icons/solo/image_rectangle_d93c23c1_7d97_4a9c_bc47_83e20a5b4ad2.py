"""Image rectangle (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd93c23c1-7d97-4a9c-bc47-83e20a5b4ad2'
SOURCE_PATH = 'icons-json/symbol/image rectangle_d93c23c1-7d97-4a9c-bc47-83e20a5b4ad2.json'
AUTHOR = 'json_to_solo'

class ImageRectangle(Solo48):
    icon_id = 'image-rectangle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('image', 'rectangle', 'symbol')

    def build(self):
        self.add_line('e0', (6, 42), (42, 42))
        self.add_line('e1', (42, 42), (32, 24))
        self.add_line('e2', (32, 24), (24, 34))
        self.add_line('e3', (24, 34), (19, 29))
        self.add_line('e4', (19, 29), (6, 42))
        self.add_arc('e5-top', (6, 13), (20, 13), radius_x=7)
        self.add_arc('e5-bottom', (20, 13), (6, 13), radius_x=7)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
