"""Chilli jelapeno (food), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d1b6c4c-c3c7-57e5-867a-78bc05759ba4'
SOURCE_PATH = 'icons-json/food/chilli jelapeno_7d1b6c4c-c3c7-57e5-867a-78bc05759ba4.json'
AUTHOR = 'json_to_solo'

class ChilliJelapenoFood(Solo48):
    icon_id = 'chilli-jelapeno-food'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('chilli', 'jelapeno', 'food')

    def build(self):
        self.add_bezier('e0', (40, 18), ((39.209, 17.571), (38.736, 17.137), (37.827, 16.935)), ((33.636, 16.008), (31.027, 19.183), (28.382, 21.608)), ((26.082, 23.714), (23.536, 25.667), (20.5, 26.787)), ((16.336, 28.328), (11.909, 28.505), (7.482, 28.328)), ((6.309, 28.286), (4.018, 27.891), (4.018, 29.566)), ((4.009, 29.691), (4, 29.823), (4, 29.948)), ((4, 29.95), (4, 29.952), (4, 29.954)), ((4, 31.427), (5.782, 33.229), (6.809, 34.24)), ((10.255, 37.583), (15.136, 40), (20.227, 40)), ((20.23, 40), (20.232, 40), (20.234, 40)), ((20.377, 40), (20.521, 39.991), (20.673, 39.983)), ((27.973, 39.983), (34.864, 35.646), (39.127, 30.417)), ((41.473, 27.545), (43.536, 23.958), (41.936, 20.328)), ((41.582, 19.52), (40.536, 18.699), (40, 18)))
        self.add_bezier('e1', (40, 18), ((41.655, 16.611), (44, 14.552), (44, 12.337)), ((44, 12.336), (44, 12.335), (44, 12.334)), ((44, 12.276), (43.991, 12.21), (43.982, 12.152)), ((43.982, 10.905), (42.864, 9.389), (41.8, 8.691)), ((41.364, 8.404), (40.482, 8.219), (40, 8)))
        self.add_bezier('e2', (40, 8), ((40.3, 8), (40.7, 8), (41, 8)))
        self.add_contour('c0', 'e0', closed=True)
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
