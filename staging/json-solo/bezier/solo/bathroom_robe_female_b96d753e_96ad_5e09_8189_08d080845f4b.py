"""Bathroom robe female (spas), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b96d753e-96ad-5e09-8189-08d080845f4b'
SOURCE_PATH = 'icons-json/spas/bathroom robe female_b96d753e-96ad-5e09-8189-08d080845f4b.json'
AUTHOR = 'json_to_solo'

class BathroomRobeFemaleSpas(Solo48):
    icon_id = 'bathroom-robe-female-spas'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'spas'
    aliases = ()
    keywords = ('bathroom', 'robe', 'female', 'spas')

    def build(self):
        self.add_line('e0', (34, 34), (34, 39))
        self.add_line('e1', (27, 44), (16, 44))
        self.add_line('e2', (15, 32), (16, 25))
        self.add_line('e3', (32, 25), (27, 25))
        self.add_line('e4', (27, 25), (27, 44))
        self.add_line('e5', (32, 25), (32, 16))
        self.add_line('e6', (27, 25), (16, 25))
        self.add_line('e7', (8, 30), (12, 9))
        self.add_line('e8', (19, 4), (28, 4))
        self.add_line('e9', (36, 10), (40, 31))
        self.add_line('e10', (40, 31), (34, 34))
        self.add_line('e11', (16, 25), (16, 16))
        self.add_line('e12', (30, 4), (24, 17))
        self.add_bezier('e13', (32, 25), ((32.918, 28.036), (33.659, 30.818), (34.105, 34)), ((34.105, 34), (34, 34), (34, 34)))
        self.add_bezier('e14', (34, 39), ((34, 39.609), (34.063, 39.764), (34.072, 40.382)), ((34.097, 41.618), (34.316, 42.855), (33.331, 43.755)), ((33.171, 43.9), (29.28, 43.982), (28.935, 43.982)), ((28.413, 43.982), (27.891, 44), (27.368, 44)), ((27.091, 44), (27.278, 44), (27, 44)))
        self.add_bezier('e15', (16, 44), ((15.722, 43.9), (15.048, 43.982), (14.796, 43.782)), ((14.552, 43.6), (14.341, 43.3), (14.189, 43.027)), ((13.794, 42.373), (13.785, 38), (13.785, 36.936)), ((13.785, 36.409), (13.709, 34.427), (13.895, 34)), ((14.173, 33.391), (14.722, 32.609), (15, 32)))
        self.add_bezier('e16', (18, 4), ((19.524, 8.409), (21.726, 12.718), (24, 16.727)), ((25.726, 19.773), (26.377, 21.427), (27, 25)))
        self.add_bezier('e17', (14, 34), ((12.257, 33.218), (9.406, 31.491), (8, 30)))
        self.add_bezier('e18', (12, 9), ((12.472, 6.573), (15.899, 4), (18.105, 4)), ((18.383, 4), (18.722, 4), (19, 4)))
        self.add_bezier('e19', (28, 4), ((28.564, 4), (29.331, 4), (29.895, 4)), ((30.375, 4), (30.914, 4.218), (31.352, 4.4)), ((33.709, 5.409), (35.469, 7.382), (36, 10)))
        self.add_contour('c0', 'e13', 'e0', 'e14', 'e1', 'e15', 'e2')
        self.add_contour('c1', 'e3', 'e4')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e16', 'e6')
        self.add_contour('c4', 'e17', 'e7', 'e18', 'e8', 'e19', 'e9', 'e10')
        self.add_contour('c5', 'e11')
        self.add_contour('c6', 'e12')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c4', 'c0')
        self.relate('connect', 'c4', 'c0')
        self.relate('connect', 'c6', 'c4')
        self.relate('connect', 'c6', 'c3')
