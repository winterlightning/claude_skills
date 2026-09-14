"""Square brackets (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'acfbd10d-de12-4626-bd35-5e7b02ef616f'
SOURCE_PATH = 'icons-json/symbol/square brackets_acfbd10d-de12-4626-bd35-5e7b02ef616f.json'
AUTHOR = 'json_to_solo'

class SquareBracketsSymbol(Solo48):
    icon_id = 'square-brackets-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('square', 'brackets', 'symbol')

    def build(self):
        self.add_line('sym-e0', (42, 24), (42, 40))
        self.add_bezier('sym-e1', (42, 40), ((42, 40.057), (42, 39.943), (42, 40)))
        self.add_bezier('sym-e2', (42, 40), ((42, 40.769), (41.589, 41.542), (41, 42)))
        self.add_bezier('sym-e3', (41, 42), ((40.853, 42), (40.155, 41.902), (40, 42)))
        self.add_line('sym-e4', (40, 42), (36, 42))
        self.add_line('sym-e5', (6, 24), (6, 40))
        self.add_bezier('sym-e6', (6, 40), ((6.54, 41.432), (6.544, 41.501), (8, 42)))
        self.add_line('sym-e7', (8, 42), (11, 42))
        self.add_line('sym-e8', (42, 24), (42, 8))
        self.add_bezier('sym-e9', (42, 8), ((42, 7.943), (42, 8.057), (42, 8)))
        self.add_bezier('sym-e10', (42, 8), ((42, 7.231), (41.589, 6.458), (41, 6)))
        self.add_bezier('sym-e11', (41, 6), ((40.853, 6), (40.155, 6.098), (40, 6)))
        self.add_line('sym-e12', (40, 6), (36, 6))
        self.add_line('sym-e13', (6, 24), (6, 8))
        self.add_bezier('sym-e14', (6, 8), ((6.54, 6.568), (6.544, 6.499), (8, 6)))
        self.add_line('sym-e15', (8, 6), (11, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c1', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c2', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c3', 'sym-e13', 'sym-e14', 'sym-e15')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
