"""Flip (content), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3a329c3-d291-512e-bc93-90a8d0c4c1fc'
SOURCE_PATH = 'icons-json/content/flip_d3a329c3-d291-512e-bc93-90a8d0c4c1fc.json'
AUTHOR = 'json_to_solo'

class FlipContent(Solo48):
    icon_id = 'flip-content'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('flip', 'content')

    def build(self):
        self.add_line('e0', (42, 30), (31, 30))
        self.add_line('e1', (29, 33), (29, 42))
        self.add_line('e2', (29, 42), (8, 42))
        self.add_line('e3', (6, 40), (6, 12))
        self.add_line('e4', (9, 9), (40, 9))
        self.add_line('e5', (42, 12), (42, 30))
        self.add_line('e6', (42, 30), (29, 42))
        self.add_line('e7', (14, 6), (14, 13))
        self.add_line('e8', (24, 13), (24, 6))
        self.add_line('e9', (34, 13), (34, 6))
        self.add_bezier('e10', (31, 30), ((29.642, 30), (29.015, 30.644), (28.852, 32.01)), ((28.811, 32.354), (29, 32.665), (29, 33)))
        self.add_bezier('e11', (8, 42), ((7.918, 42), (8.291, 42), (8.201, 42)), ((6.875, 42), (6, 41.276), (6, 40)))
        self.add_bezier('e12', (6, 12), ((6, 10.216), (7.503, 9), (9, 9)))
        self.add_bezier('e13', (40, 9), ((41.129, 9), (41.984, 10.132), (41.984, 11.359)), ((41.992, 11.416), (41.992, 11.482), (42, 11.539)), ((42, 11.605), (42, 11.935), (42, 12)))
        self.add_contour('c0', 'e0', 'e10', 'e1', 'e2', 'e11', 'e3', 'e12', 'e4', 'e13', 'e5', closed=True)
        self.add_contour('c1', 'e6')
        self.add_contour('c2', 'e7')
        self.add_contour('c3', 'e8')
        self.add_contour('c4', 'e9')
        self.relate('connect', 'c0', 'c1')
