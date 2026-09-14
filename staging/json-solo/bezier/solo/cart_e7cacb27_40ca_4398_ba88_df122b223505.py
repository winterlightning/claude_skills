"""Cart (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7cacb27-40ca-4398-ba88-df122b223505'
SOURCE_PATH = 'icons-json/shopping/cart_e7cacb27-40ca-4398-ba88-df122b223505.json'
AUTHOR = 'json_to_solo'

class Cart(Solo48):
    icon_id = 'cart'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('cart', 'shopping')

    def build(self):
        self.add_line('e0', (4, 8), (10, 8))
        self.add_line('e1', (10, 8), (17, 30))
        self.add_line('e2', (18, 31), (38, 31))
        self.add_line('e3', (39, 30), (44, 14))
        self.add_line('e4', (43, 12), (12, 12))
        self.add_bezier('e5', (17, 30), ((17.145, 30.16), (16.864, 30.282), (17.045, 30.451)), ((17.218, 30.602), (17.827, 30.874), (18, 31)))
        self.add_bezier('e6', (38, 31), ((38.1, 30.975), (37.836, 30.695), (37.936, 30.669)), ((38.355, 30.493), (38.791, 30.312), (39, 30)))
        self.add_bezier('e7', (44, 14), ((44, 13.714), (43.991, 13.322), (43.991, 13.036)), ((43.991, 12.531), (43.355, 12.219), (43, 12)))
        self.add_dot('e8', (20, 40))
        self.add_dot('e9', (36, 40))
        self.add_contour('c0', 'e0', 'e1', 'e5', 'e2', 'e6', 'e3', 'e7', 'e4')
