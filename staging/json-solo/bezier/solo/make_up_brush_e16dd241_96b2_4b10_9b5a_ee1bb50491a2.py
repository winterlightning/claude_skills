"""Make up brush (beauty), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e16dd241-96b2-4b10-9b5a-ee1bb50491a2'
SOURCE_PATH = 'icons-json/beauty/make up brush_e16dd241-96b2-4b10-9b5a-ee1bb50491a2.json'
AUTHOR = 'json_to_solo'

class MakeUpBrushBeauty(Solo48):
    icon_id = 'make-up-brush-beauty'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    aliases = ()
    keywords = ('make', 'up', 'brush', 'beauty')

    def build(self):
        self.add_line('e0', (16, 20), (8, 12))
        self.add_line('e1', (40, 12), (32, 20))
        self.add_line('e2', (32, 20), (16, 20))
        self.add_line('e3', (19, 28), (19, 41))
        self.add_line('e4', (29, 41), (29, 28))
        self.add_line('e5', (21, 12), (22, 20))
        self.add_bezier('e6', (8, 12), ((8, 10.973), (8.016, 10.136), (8.016, 9.109)), ((8.016, 8.564), (10.048, 7.291), (10.672, 6.936)), ((13.76, 5.173), (18.56, 4.009), (22.96, 4.009)), ((23.086, 4.009), (23.228, 4), (23.354, 4)), ((23.356, 4), (23.358, 4), (23.36, 4)), ((23.808, 4), (24.24, 4.009), (24.688, 4.009)), ((29.168, 4.009), (33.776, 5.082), (37.072, 6.782)), ((38.016, 7.273), (40, 8.418), (40, 9.191)), ((40, 9.691), (39.984, 10.2), (39.984, 10.709)), ((39.984, 10.936), (39.984, 11.164), (39.984, 11.391)), ((40, 11.427), (40, 11.464), (40, 11.5)), ((40, 11.727), (40, 11.773), (40, 12)))
        self.add_bezier('e7', (16, 20), ((16.032, 23.309), (14.84, 25.182), (19, 28)))
        self.add_bezier('e8', (19, 41), ((19.704, 42.064), (21.28, 43.991), (23.744, 43.991)), ((23.886, 43.991), (24.027, 44), (24.169, 44)), ((24.171, 44), (24.174, 44), (24.176, 44)), ((24.256, 43.991), (24.352, 43.991), (24.432, 43.982)), ((26.304, 43.982), (29, 41.991), (29, 41)))
        self.add_bezier('e9', (29, 28), ((29.016, 27.927), (28.832, 27.482), (28.848, 27.409)), ((28.928, 27.3), (29.008, 27.191), (29.088, 27.082)), ((29.488, 26.6), (30.256, 26.182), (30.672, 25.682)), ((32.112, 24), (32.064, 21.818), (32, 20)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e2', 'e7', 'e3', 'e8', 'e4')
        self.add_contour('c1', 'e9')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c2', 'c0')
