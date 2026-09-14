"""Paper (content), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6deffd1-6733-4f23-8bdd-560adfa61866'
SOURCE_PATH = 'icons-json/content/paper_b6deffd1-6733-4f23-8bdd-560adfa61866.json'
AUTHOR = 'json_to_solo'

class PaperB6deffd1(Solo48):
    icon_id = 'paper-b6deffd1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('paper', 'content')

    def build(self):
        self.add_line('e0', (15, 35), (33, 35))
        self.add_line('e1', (15, 26), (28, 26))
        self.add_line('e2', (15, 15), (24, 15))
        self.add_line('e3', (40, 16), (40, 42))
        self.add_line('e4', (38, 44), (10, 44))
        self.add_line('e5', (8, 42), (8, 6))
        self.add_line('e6', (11, 4), (28, 4))
        self.add_line('e7', (29, 5), (40, 16))
        self.add_bezier('e8', (40, 42), ((40, 42.027), (39.992, 42.245), (39.992, 42.273)), ((39.992, 42.864), (38.905, 43.982), (38.4, 43.982)), ((38.375, 43.991), (38.025, 43.991), (38, 44)))
        self.add_bezier('e9', (10, 44), ((9.436, 43.691), (8.362, 43.382), (8.101, 42.655)), ((8.051, 42.5), (8.059, 42.145), (8, 42)))
        self.add_bezier('e10', (8, 6), ((8.749, 4.655), (9.577, 4.345), (11, 4)))
        self.add_bezier('e11', (28, 4), ((28.278, 4.3), (28.705, 4.709), (29, 5)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e8', 'e4', 'e9', 'e5', 'e10', 'e6', 'e11', 'e7', closed=True)
