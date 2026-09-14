"""Fortress (protection), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '662fb562-2043-4728-8a10-72a8034ebd9b'
SOURCE_PATH = 'icons-json/protection/fortress_662fb562-2043-4728-8a10-72a8034ebd9b.json'
AUTHOR = 'json_to_solo'

class FortressProtection(Solo48):
    icon_id = 'fortress-protection'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('fortress', 'protection')

    def build(self):
        self.add_line('e0', (28, 12), (34, 12))
        self.add_line('e1', (34, 12), (35, 6))
        self.add_line('e2', (35, 6), (42, 6))
        self.add_line('e3', (42, 6), (42, 16))
        self.add_line('e4', (37, 19), (37, 40))
        self.add_line('e5', (35, 42), (13, 42))
        self.add_line('e6', (11, 40), (11, 19))
        self.add_line('e7', (6, 15), (6, 6))
        self.add_line('e8', (7, 6), (14, 6))
        self.add_line('e9', (14, 6), (14, 12))
        self.add_line('e10', (14, 12), (20, 12))
        self.add_line('e11', (20, 12), (20, 6))
        self.add_line('e12', (20, 6), (28, 6))
        self.add_line('e13', (28, 6), (28, 12))
        self.add_bezier('e14', (42, 16), ((42, 16.082), (41.992, 15.982), (41.992, 16.064)), ((41.992, 16.293), (41.82, 16.579), (41.714, 16.775)), ((40.765, 18.485), (38.71, 18.591), (37, 19)))
        self.add_bezier('e15', (37, 40), ((37, 40.753), (35.728, 42), (35, 42)))
        self.add_bezier('e16', (13, 42), ((11.985, 42), (11, 40.835), (11, 40)))
        self.add_bezier('e17', (11, 19), ((9.192, 18.485), (7.358, 18.027), (6.425, 16.244)), ((6.221, 15.851), (6, 15.458), (6, 15)))
        self.add_bezier('e18', (6, 6), ((6.27, 6), (6.73, 6), (7, 6)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e14', 'e4', 'e15', 'e5', 'e16', 'e6', 'e17', 'e7', 'e18', 'e8', 'e9', 'e10', 'e11', 'e12', 'e13', closed=True)
