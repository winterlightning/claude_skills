"""Batch-02/necklace jewel (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8209a5c1-aa96-5a1d-afb2-da4dda62e9ab'
SOURCE_PATH = 'icons-json/accessories/batch-02/necklace jewel_8209a5c1-aa96-5a1d-afb2-da4dda62e9ab.json'
AUTHOR = 'json_to_solo'

class Batch02NecklaceJewel(Solo48):
    icon_id = 'batch-02-necklace-jewel'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'necklace', 'jewel', 'accessories')

    def build(self):
        self.add_line('e0', (6, 6), (6, 10))
        self.add_line('e1', (24, 27), (21, 31))
        self.add_bezier('e2', (6, 10), ((6, 12.029), (7.399, 15.425), (8.471, 17.135)), ((9.101, 18.134), (9.764, 19.197), (10.582, 20.065)), ((18.649, 28.647), (33.573, 27.109), (39.595, 16.972)), ((40.593, 15.286), (41.992, 11.997), (41.992, 10.042)), ((41.992, 9.976), (42, 9.911), (42, 9.845)), ((42, 8.569), (42, 7.285), (42, 6)))
        self.add_bezier('e3', (21, 31), ((20.64, 31.458), (20.105, 32.435), (19.852, 32.959)), ((18.453, 35.872), (18.199, 39.701), (21.603, 41.362)), ((22.282, 41.689), (23.043, 41.992), (23.812, 41.992)), ((23.86, 41.992), (23.916, 42), (23.973, 42)), ((23.974, 42), (23.975, 42), (23.975, 42)), ((24.025, 42), (24.074, 41.992), (24.131, 41.992)), ((24.72, 41.992), (25.366, 41.771), (25.898, 41.542)), ((28.091, 40.593), (29.302, 38.465), (29.105, 36.085)), ((28.827, 32.746), (26.135, 29.373), (24, 27)))
        self.add_contour('c0', 'e0', 'e2')
        self.add_contour('c1', 'e3', 'e1', closed=True)
