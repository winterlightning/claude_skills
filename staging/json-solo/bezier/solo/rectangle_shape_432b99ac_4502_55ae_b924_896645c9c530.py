"""Rectangle shape (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '432b99ac-4502-55ae-b924-896645c9c530'
SOURCE_PATH = 'icons-json/design/rectangle shape_432b99ac-4502-55ae-b924-896645c9c530.json'
AUTHOR = 'json_to_solo'

class RectangleShapeDesign(Solo48):
    icon_id = 'rectangle-shape-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('rectangle', 'shape', 'design')

    def build(self):
        self.add_line('e0', (40, 40), (7, 40))
        self.add_line('e1', (4, 36), (4, 12))
        self.add_line('e2', (7, 8), (42, 8))
        self.add_line('e3', (44, 12), (44, 39))
        self.add_bezier('e4', (7, 40), ((6.855, 40), (6.445, 39.988), (6.3, 39.988)), ((5.191, 39.988), (4, 38.363), (4, 36.886)), ((4, 36.689), (4, 36.197), (4, 36)))
        self.add_bezier('e5', (4, 12), ((4, 11.754), (4.009, 11.188), (4.009, 10.942)), ((4.009, 9.305), (4.909, 8.025), (6.127, 8.025)), ((6.327, 8.025), (6.8, 8), (7, 8)))
        self.add_bezier('e6', (42, 8), ((42.073, 8), (42.318, 8), (42.391, 8)), ((42.8, 8), (43.991, 8.751), (43.991, 9.428)), ((43.991, 9.514), (44, 9.6), (44, 9.698)), ((44, 9.982), (43.991, 10.265), (43.991, 10.548)), ((44, 10.732), (44, 10.929), (44, 11.126)), ((44, 11.311), (44, 11.815), (44, 12)))
        self.add_bezier('e7', (44, 39), ((43.1, 39.837), (42.536, 39.975), (41.427, 39.975)), ((41.073, 39.975), (40.355, 40), (40, 40)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5', 'e2', 'e6', 'e3', 'e7', closed=True)
