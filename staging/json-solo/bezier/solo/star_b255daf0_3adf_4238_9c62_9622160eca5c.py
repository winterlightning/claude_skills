"""Star (holidays), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b255daf0-3adf-4238-9c62-9622160eca5c'
SOURCE_PATH = 'icons-json/holidays/star_b255daf0-3adf-4238-9c62-9622160eca5c.json'
AUTHOR = 'json_to_solo'

class Star(Solo48):
    icon_id = 'star'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('star', 'holidays')

    def build(self):
        self.add_line('e0', (33, 33), (35, 42))
        self.add_line('e1', (35, 42), (24, 35))
        self.add_line('e2', (24, 35), (13, 42))
        self.add_line('e3', (13, 42), (16, 29))
        self.add_line('e4', (16, 29), (6, 19))
        self.add_line('e5', (6, 19), (19, 19))
        self.add_line('e6', (19, 19), (24, 6))
        self.add_line('e7', (24, 6), (29, 19))
        self.add_line('e8', (29, 19), (42, 19))
        self.add_line('e9', (42, 19), (33, 28))
        self.add_bezier('e10', (33, 28), ((32.894, 28.213), (32.722, 28.443), (32.656, 28.688)), ((32.452, 29.408), (32.836, 32.395), (33, 33)))
        self.add_contour('c0', 'e10', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', closed=True)
