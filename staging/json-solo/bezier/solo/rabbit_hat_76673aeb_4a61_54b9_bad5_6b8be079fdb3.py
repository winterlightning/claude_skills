"""Rabbit hat (products), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '76673aeb-4a61-54b9-bad5-6b8be079fdb3'
SOURCE_PATH = 'icons-json/products/rabbit hat_76673aeb-4a61-54b9-bad5-6b8be079fdb3.json'
AUTHOR = 'json_to_solo'

class RabbitHatProducts(Solo48):
    icon_id = 'rabbit-hat-products'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'products'
    aliases = ()
    keywords = ('rabbit', 'hat', 'products')

    def build(self):
        self.add_line('e0', (23, 18), (23, 8))
        self.add_line('e1', (16, 7), (16, 28))
        self.add_line('e2', (16, 28), (40, 28))
        self.add_line('e3', (31, 22), (31, 28))
        self.add_line('e4', (31, 28), (33, 41))
        self.add_line('e5', (31, 44), (15, 44))
        self.add_line('e6', (13, 41), (15, 28))
        self.add_line('e7', (15, 28), (8, 28))
        self.add_line('e8', (23, 28), (23, 18))
        self.add_bezier('e9', (23, 14), ((26.47, 13.4), (29.42, 13.427), (32.23, 15.664)), ((33.57, 16.736), (36.48, 20.118), (34.55, 21.664)), ((33.62, 22.409), (32.11, 22.027), (31, 22)))
        self.add_bezier('e10', (31, 22), ((27.09, 20.964), (26.06, 20.691), (23, 18)))
        self.add_bezier('e11', (23, 8), ((23, 6.264), (21.97, 4), (19.75, 4)), ((19.749, 4), (19.748, 4), (19.746, 4)), ((19.668, 4), (19.599, 4.009), (19.52, 4.009)), ((17.5, 4.009), (16.68, 5.464), (16, 7)))
        self.add_bezier('e12', (33, 41), ((33.25, 42.727), (32.66, 43.491), (31, 44)))
        self.add_bezier('e13', (15, 44), ((14.91, 44), (14.81, 43.991), (14.72, 43.991)), ((13.35, 43.991), (12.86, 41.964), (13, 41)))
        self.add_contour('c0', 'e9')
        self.add_contour('c1', 'e10', 'e0', 'e11', 'e1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e12', 'e5', 'e13', 'e6', 'e7')
        self.add_contour('c4', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c1')
        self.relate('connect', 'c4', 'c1')
