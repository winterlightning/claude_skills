"""Batch-03/indoor plant (decoration), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f271830-3c9b-5ad9-a96a-8ceb96df6b84'
SOURCE_PATH = 'icons-json/decoration/batch-03/indoor plant_0f271830-3c9b-5ad9-a96a-8ceb96df6b84.json'
AUTHOR = 'json_to_solo'

class Batch03IndoorPlant(Solo48):
    icon_id = 'batch-03-indoor-plant'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    aliases = ()
    keywords = ('batch', 'indoor', 'plant', 'decoration')

    def build(self):
        self.add_line('e0', (34, 23), (28, 29))
        self.add_line('e1', (31, 44), (19, 44))
        self.add_line('e2', (13, 40), (12, 29))
        self.add_line('e3', (12, 29), (36, 29))
        self.add_line('e4', (36, 29), (35, 40))
        self.add_bezier('e5', (22, 29), ((16.511, 24.818), (10.585, 21.391), (8.689, 15.536)), ((8.345, 14.455), (8.025, 13.291), (8.025, 12.173)), ((8.025, 11.718), (8, 11.264), (8, 10.818)), ((8, 10.664), (8, 10.155), (8, 10)))
        self.add_bezier('e6', (26, 19), ((27.477, 14.309), (28.751, 12.091), (26.548, 7.382)), ((26.099, 6.424), (24.184, 4), (24.078, 4)), ((24.076, 4), (24.075, 4), (24.074, 4)), ((23.803, 4), (21.735, 6.955), (21.502, 7.445)), ((19.262, 12.155), (20.548, 14.318), (22, 19)))
        self.add_bezier('e7', (26, 19), ((27.932, 15.991), (31.298, 14), (35.249, 12.355)), ((36.209, 11.955), (37.218, 11.6), (38.252, 11.3)), ((38.634, 11.191), (39.028, 11.091), (39.409, 10.991)), ((39.603, 10.937), (40, 10.699), (40, 10.839)), ((40, 10.841), (40, 10.843), (40, 10.845)), ((39.988, 10.936), (39.988, 11.036), (39.975, 11.127)), ((39.975, 14.3), (38.978, 17.573), (36.677, 20.273)), ((35.84, 21.255), (34.911, 22.055), (34, 23)))
        self.add_bezier('e8', (22, 19), ((18.714, 14.991), (13.92, 11.791), (8, 10)))
        self.add_bezier('e9', (35, 40), ((34.865, 41.191), (33.748, 43.491), (32.086, 43.9)), ((31.311, 44), (31.862, 43.736), (31, 44)))
        self.add_bezier('e10', (19, 44), ((18.865, 44), (18.794, 44), (18.658, 44)), ((16.025, 44), (13.222, 42.018), (13, 40)))
        self.add_contour('c0', 'e5')
        self.add_contour('c1', 'e6')
        self.add_contour('c2', 'e7', 'e0')
        self.add_contour('c3', 'e8')
        self.add_contour('c4', 'e9', 'e1', 'e10', 'e2', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c4')
