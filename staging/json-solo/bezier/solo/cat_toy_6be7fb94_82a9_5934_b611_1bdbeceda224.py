"""Cat toy (pets), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6be7fb94-82a9-5934-b611-1bdbeceda224'
SOURCE_PATH = 'icons-json/pets/cat toy_6be7fb94-82a9-5934-b611-1bdbeceda224.json'
AUTHOR = 'json_to_solo'

class CatToyPets(Solo48):
    icon_id = 'cat-toy-pets'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('cat', 'toy', 'pets')

    def build(self):
        self.add_line('e0', (34, 35), (25, 35))
        self.add_line('e1', (25, 44), (28, 44))
        self.add_arc('e2-top', (8, 14), (26, 14), radius_x=9, radius_y=10)
        self.add_arc('e2-bottom', (26, 14), (8, 14), radius_x=9, radius_y=10)
        self.add_bezier('e3', (26, 19), ((27.229, 21.473), (28.126, 23.027), (30.728, 23.955)), ((33.617, 24.991), (37.154, 23.9), (39.158, 27.018)), ((39.638, 27.755), (39.983, 28.718), (39.983, 29.636)), ((39.991, 29.699), (40, 29.762), (40, 29.824)), ((40, 29.825), (40, 29.826), (40, 29.827)), ((40, 32.991), (36.577, 35), (34, 35)))
        self.add_bezier('e4', (25, 35), ((23.392, 35), (21.314, 35.6), (20.497, 37.209)), ((19.175, 39.836), (20.817, 42.518), (23.124, 43.536)), ((23.377, 43.655), (23.773, 44), (24.042, 44)), ((24.312, 44), (24.731, 44), (25, 44)))
        self.add_contour('c0', 'e3', 'e0', 'e4', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.relate('connect', 'c0', 'e2')
