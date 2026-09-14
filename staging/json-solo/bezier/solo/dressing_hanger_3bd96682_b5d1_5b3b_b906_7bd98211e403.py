"""Dressing hanger (furnitures), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3bd96682-b5d1-5b3b-b906-7bd98211e403'
SOURCE_PATH = 'icons-json/furnitures/dressing hanger_3bd96682-b5d1-5b3b-b906-7bd98211e403.json'
AUTHOR = 'json_to_solo'

class DressingHangerFurnitures(Solo48):
    icon_id = 'dressing-hanger-furnitures'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('dressing', 'hanger', 'furnitures')

    def build(self):
        self.add_line('e0', (24, 18), (24, 22))
        self.add_line('e1', (24, 22), (6, 34))
        self.add_line('e2', (7, 40), (40, 40))
        self.add_line('e3', (42, 34), (24, 22))
        self.add_bezier('e4', (19, 13), ((19.082, 12.29), (19.564, 11.57), (19.845, 10.91)), ((20.418, 9.53), (21.982, 8.01), (23.418, 8.01)), ((23.481, 8), (23.552, 8), (23.624, 8)), ((23.625, 8), (23.626, 8), (23.627, 8)), ((23.7, 8), (23.773, 8), (23.845, 8.01)), ((24.518, 8.01), (25.118, 8.33), (25.682, 8.7)), ((27.527, 9.91), (28.573, 12.35), (27.736, 14.66)), ((27.064, 16.49), (25.555, 17.28), (24, 18)))
        self.add_bezier('e5', (6, 34), ((5.209, 34.52), (4, 35.42), (4, 36.56)), ((4, 36.561), (4, 36.562), (4, 36.564)), ((4, 36.642), (4, 36.721), (4, 36.8)), ((4, 36.88), (4.009, 36.96), (4.009, 37.04)), ((4.009, 38.63), (5.555, 40), (7, 40)))
        self.add_bezier('e6', (40, 40), ((40.082, 40), (40.536, 40), (40.618, 39.99)), ((42.091, 39.99), (44, 38.7), (44, 36.9)), ((44, 36.882), (44, 36.865), (44, 36.847)), ((44, 35.732), (42.823, 34.541), (42, 34)))
        self.add_contour('c0', 'e4', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6', 'e3')
