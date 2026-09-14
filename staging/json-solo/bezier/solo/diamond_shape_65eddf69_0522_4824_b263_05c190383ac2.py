"""Diamond shape (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65eddf69-0522-4824-b263-05c190383ac2'
SOURCE_PATH = 'icons-json/design/diamond shape_65eddf69-0522-4824-b263-05c190383ac2.json'
AUTHOR = 'json_to_solo'

class DiamondShape65eddf69(Solo48):
    icon_id = 'diamond-shape-65eddf69'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('diamond', 'shape', 'design')

    def build(self):
        self.add_bezier('sym-e0', (24, 6), ((23.984, 6), (24.016, 6.015), (24, 6)))
        self.add_bezier('sym-e1', (24, 6), ((23.746, 6.27), (23.254, 6.73), (23, 7)))
        self.add_line('sym-e2', (23, 7), (7, 23))
        self.add_bezier('sym-e3', (7, 23), ((6.73, 23.221), (6.27, 23.779), (6, 24)))
        self.add_bezier('sym-e4', (6, 24), ((6.047, 24.052), (6, 23.948), (6, 24)))
        self.add_bezier('sym-e5', (6, 24), ((6, 24.052), (6.047, 23.948), (6, 24)))
        self.add_bezier('sym-e6', (6, 24), ((6.27, 24.221), (6.73, 24.779), (7, 25)))
        self.add_line('sym-e7', (7, 25), (23, 41))
        self.add_bezier('sym-e8', (23, 41), ((23.254, 41.27), (23.746, 41.73), (24, 42)))
        self.add_bezier('sym-e9', (24, 42), ((24.016, 41.985), (23.984, 42), (24, 42)))
        self.add_bezier('sym-e10', (24, 42), ((24.016, 42), (23.984, 41.985), (24, 42)))
        self.add_bezier('sym-e11', (24, 42), ((24.254, 41.73), (24.746, 41.27), (25, 41)))
        self.add_line('sym-e12', (25, 41), (41, 25))
        self.add_bezier('sym-e13', (41, 25), ((41.27, 24.779), (41.73, 24.221), (42, 24)))
        self.add_bezier('sym-e14', (42, 24), ((41.953, 23.948), (42, 24.052), (42, 24)))
        self.add_bezier('sym-e15', (42, 24), ((42, 23.948), (41.953, 24.052), (42, 24)))
        self.add_bezier('sym-e16', (42, 24), ((41.73, 23.779), (41.27, 23.221), (41, 23)))
        self.add_line('sym-e17', (41, 23), (25, 7))
        self.add_bezier('sym-e18', (25, 7), ((24.746, 6.73), (24.254, 6.27), (24, 6)))
        self.add_bezier('sym-e19', (24, 6), ((23.984, 6.015), (24.016, 6), (24, 6)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
