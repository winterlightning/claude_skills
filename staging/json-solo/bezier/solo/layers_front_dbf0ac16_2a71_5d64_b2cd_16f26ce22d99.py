"""Layers front (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dbf0ac16-2a71-5d64-b2cd-16f26ce22d99'
SOURCE_PATH = 'icons-json/design/layers front_dbf0ac16-2a71-5d64-b2cd-16f26ce22d99.json'
AUTHOR = 'json_to_solo'

class LayersFrontDesign(Solo48):
    icon_id = 'layers-front-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('layers', 'front', 'design')

    def build(self):
        self.add_line('e0', (32, 16), (32, 7))
        self.add_line('e1', (26, 6), (8, 6))
        self.add_line('e2', (6, 8), (6, 31))
        self.add_line('e3', (7, 32), (16, 32))
        self.add_line('e4', (20, 16), (36, 16))
        self.add_line('e5', (42, 17), (42, 40))
        self.add_line('e6', (40, 42), (17, 42))
        self.add_line('e7', (16, 41), (16, 17))
        self.add_bezier('e8', (32, 7), ((31.73, 6.763), (31.642, 6.262), (31.315, 6.106)), ((30.946, 6), (29.146, 6.025), (28.713, 6.016)), ((28.083, 6.016), (27.453, 6), (26.823, 6)), ((26.7, 6), (26.123, 6), (26, 6)))
        self.add_bezier('e9', (8, 6), ((7.157, 6.262), (6, 6.912), (6, 8)))
        self.add_bezier('e10', (6, 31), ((6, 31.155), (6.016, 30.856), (6.016, 31.012)), ((6.016, 31.568), (6.656, 31.656), (7, 32)))
        self.add_bezier('e11', (36, 16), ((36.736, 16), (37.737, 15.769), (38.465, 15.695)), ((39.341, 15.605), (40.83, 15.098), (41.591, 15.81)), ((41.861, 16.064), (41.853, 16.705), (42, 17)))
        self.add_bezier('e12', (42, 40), ((42, 40.638), (41.501, 41.689), (40.895, 41.91)), ((40.724, 41.967), (40.172, 41.943), (40, 42)))
        self.add_bezier('e13', (17, 42), ((16.935, 42), (17.332, 42), (17.266, 42)), ((16.62, 42), (16.442, 41.401), (16, 41)))
        self.add_bezier('e14', (16, 17), ((16, 16.427), (16.088, 16.154), (16.612, 15.843)), ((16.865, 15.695), (19.607, 16), (20, 16)))
        self.add_contour('c0', 'e0', 'e8', 'e1', 'e9', 'e2', 'e10', 'e3')
        self.add_contour('c1', 'e4', 'e11', 'e5', 'e12', 'e6', 'e13', 'e7', 'e14', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
