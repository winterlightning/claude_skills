"""Diamond shape (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65eddf69-0522-4824-b263-05c190383ac2'
SOURCE_PATH = 'icons-json/design/diamond shape_65eddf69-0522-4824-b263-05c190383ac2.json'
AUTHOR = 'json_to_solo'

class DiamondShapeDesign(Solo48):
    icon_id = 'diamond-shape-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('diamond', 'shape', 'design')

    def build(self):
        self.add_line('sym-e1', (24, 6), (23, 7))
        self.add_line('sym-e2', (23, 7), (7, 23))
        self.add_line('sym-e3', (7, 23), (6, 24))
        self.add_line('sym-e6', (6, 24), (7, 25))
        self.add_line('sym-e7', (7, 25), (23, 41))
        self.add_line('sym-e8', (23, 41), (24, 42))
        self.add_line('sym-e11', (24, 42), (25, 41))
        self.add_line('sym-e12', (25, 41), (41, 25))
        self.add_line('sym-e13', (41, 25), (42, 24))
        self.add_line('sym-e16', (42, 24), (41, 23))
        self.add_line('sym-e17', (41, 23), (25, 7))
        self.add_line('sym-e18', (25, 7), (24, 6))
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e16', 'sym-e17', 'sym-e18', closed=True)
