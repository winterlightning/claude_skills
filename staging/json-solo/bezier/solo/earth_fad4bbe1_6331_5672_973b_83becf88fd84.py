"""Earth (maps), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fad4bbe1-6331-5672-973b-83becf88fd84'
SOURCE_PATH = 'icons-json/maps/earth_fad4bbe1-6331-5672-973b-83becf88fd84.json'
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
        self.add_line('e0', (16, 34), (15, 30))
        self.add_line('e1', (9, 24), (4, 24))
        self.add_line('e2', (37, 27), (34, 30))
        self.add_line('e3', (27, 27), (27, 23))
        self.add_line('e4', (22, 9), (24, 4))
        self.add_arc('e5-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e5-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e6', (24, 44), ((20, 41.245), (17.245, 38.991), (16, 34)))
        self.add_bezier('e7', (15, 30), ((14.773, 29.1), (14.555, 28.6), (14.145, 27.755)), ((13.236, 25.9), (11.127, 24), (9, 24)))
        self.add_bezier('e8', (44, 24), ((41.582, 24.018), (39.5, 24.418), (37.6, 25.991)), ((37.327, 26.209), (37.209, 26.727), (37, 27)))
        self.add_bezier('e9', (34, 30), ((32.7, 31.727), (29.791, 33.273), (28.045, 31.491)), ((26.891, 30.309), (27, 28.573), (27, 27)))
        self.add_bezier('e10', (27, 23), ((27, 21.373), (25.673, 19.764), (24.273, 18.991)), ((23.109, 18.355), (21.455, 18.164), (20.718, 16.918)), ((19.627, 15.091), (21.264, 10.855), (22, 9)))
        self.add_contour('c0', 'e6', 'e0', 'e7', 'e1')
        self.add_contour('c1', 'e8', 'e2', 'e9', 'e3', 'e10', 'e4')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'e5')
        self.relate('connect', 'c0', 'e5')
        self.relate('connect', 'c1', 'e5')
        self.relate('connect', 'c1', 'e5')
