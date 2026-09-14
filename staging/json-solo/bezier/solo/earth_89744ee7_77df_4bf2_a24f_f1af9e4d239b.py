"""Earth (maps), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89744ee7-77df-4bf2-a24f-f1af9e4d239b'
SOURCE_PATH = 'icons-json/maps/earth_89744ee7-77df-4bf2-a24f-f1af9e4d239b.json'
AUTHOR = 'json_to_solo'

class Earth(Solo48):
    icon_id = 'earth'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('earth', 'maps')

    def build(self):
        self.add_line('e0', (15, 34), (14, 29))
        self.add_line('e1', (27, 23), (27, 27))
        self.add_line('e2', (34, 30), (36, 27))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e4', (24, 44), ((20.291, 41.373), (15.973, 38.864), (15, 34)))
        self.add_bezier('e5', (14, 29), ((12.955, 23.791), (8.482, 23.5), (4, 24)))
        self.add_bezier('e6', (24, 4), ((22.4, 6.891), (21.173, 9.836), (20.445, 13.073)), ((20.182, 14.264), (19.736, 15.727), (20.445, 16.845)), ((21.2, 18.027), (22.764, 18.164), (23.945, 18.709)), ((25.664, 19.518), (27, 21.109), (27, 23)))
        self.add_bezier('e7', (27, 27), ((27, 28.618), (26.991, 30.1), (28.191, 31.291)), ((29.782, 32.864), (32.991, 32.009), (34, 30)))
        self.add_bezier('e8', (36, 27), ((37.264, 24.473), (41.555, 23.909), (44, 24)))
        self.add_contour('c0', 'e4', 'e0', 'e5')
        self.add_contour('c1', 'e6', 'e1', 'e7', 'e2', 'e8')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c1', 'e3')
        self.relate('connect', 'c1', 'e3')
