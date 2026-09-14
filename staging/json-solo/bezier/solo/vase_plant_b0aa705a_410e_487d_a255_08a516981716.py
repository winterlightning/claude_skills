"""Batch-05/vase plant (decoration), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0aa705a-410e-487d-a255-08a516981716'
SOURCE_PATH = 'icons-json/decoration/batch-05/vase plant_b0aa705a-410e-487d-a255-08a516981716.json'
AUTHOR = 'json_to_solo'

class Batch05VasePlant(Solo48):
    icon_id = 'batch-05-vase-plant'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    aliases = ()
    keywords = ('batch', 'vase', 'plant', 'decoration')

    def build(self):
        self.add_line('e0', (24, 29), (24, 31))
        self.add_line('e1', (24, 29), (22, 21))
        self.add_line('e2', (22, 21), (18, 17))
        self.add_line('e3', (24, 29), (28, 21))
        self.add_line('e4', (28, 21), (30, 17))
        self.add_line('e5', (30, 17), (29, 11))
        self.add_line('e6', (19, 12), (18, 17))
        self.add_line('e7', (24, 31), (10, 31))
        self.add_line('e8', (10, 31), (10, 40))
        self.add_line('e9', (15, 44), (33, 44))
        self.add_line('e10', (38, 40), (38, 31))
        self.add_line('e11', (38, 31), (24, 31))
        self.add_bezier('e12', (18, 17), ((16.203, 14.864), (14.203, 12.464), (11.742, 10.7)), ((11.225, 10.336), (10.695, 9.982), (10.129, 9.645)), ((9.428, 9.227), (8.714, 8.8), (8.012, 8.382)), ((8.012, 8.981), (8, 9.59), (8, 10.19)), ((8, 10.199), (8, 10.209), (8, 10.218)), ((8, 10.882), (8.025, 11.555), (8.025, 12.218)), ((8.025, 18.055), (10.603, 25.836), (14, 31)))
        self.add_bezier('e13', (34, 31), ((37.692, 24.982), (39.988, 18.409), (39.988, 11.764)), ((39.988, 11.665), (40, 11.576), (40, 11.477)), ((40, 11.476), (40, 11.474), (40, 11.473)), ((40, 11.073), (39.988, 10.664), (39.988, 10.264)), ((39.988, 10.1), (39.975, 9.936), (39.963, 9.773)), ((39.938, 9.291), (39.914, 8.809), (39.889, 8.327)), ((39.729, 8.309), (38.043, 9.518), (37.378, 9.955)), ((34.929, 11.573), (31.194, 14.791), (30, 17)))
        self.add_bezier('e14', (29, 11), ((28.557, 9.027), (27.003, 7.136), (25.489, 5.509)), ((25.114, 5.097), (24.321, 4), (24.167, 4)), ((24.164, 4), (24.162, 4), (24.16, 4)), ((24.086, 4), (22.978, 5.318), (22.585, 5.773)), ((20.935, 7.645), (19.591, 9.809), (19, 12)))
        self.add_bezier('e15', (10, 40), ((10, 41.418), (13.268, 43.991), (15.225, 43.991)), ((15.274, 43.991), (14.951, 44), (15, 44)))
        self.add_bezier('e16', (33, 44), ((34.908, 43.527), (36.111, 42.773), (37.034, 41.382)), ((37.218, 41.109), (38, 40.309), (38, 40)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3', 'e4')
        self.add_contour('c3', 'e12')
        self.add_contour('c4', 'e13')
        self.add_contour('c5', 'e5', 'e14', 'e6')
        self.add_contour('c6', 'e7', 'e8', 'e15', 'e9', 'e16', 'e10', 'e11', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
