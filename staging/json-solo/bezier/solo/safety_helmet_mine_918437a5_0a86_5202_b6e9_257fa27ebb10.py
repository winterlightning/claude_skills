"""Safety helmet mine (construction), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '918437a5-0a86-5202-b6e9-257fa27ebb10'
SOURCE_PATH = 'icons-json/construction/safety helmet mine_918437a5-0a86-5202-b6e9-257fa27ebb10.json'
AUTHOR = 'json_to_solo'

class SafetyHelmetMineConstruction(Solo48):
    icon_id = 'safety-helmet-mine-construction'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('safety', 'helmet', 'mine', 'construction')

    def build(self):
        self.add_line('e0', (29, 17), (29, 11))
        self.add_line('e1', (27, 8), (21, 8))
        self.add_line('e2', (19, 12), (19, 17))
        self.add_arc('e3-top', (19, 24), (29, 24), radius_x=5, radius_y=6)
        self.add_arc('e3-bottom', (29, 24), (19, 24), radius_x=5, radius_y=6)
        self.add_bezier('e4', (29, 11), ((28.736, 9.82), (28.745, 8.01), (27.327, 8.01)), ((27.264, 8.01), (27.2, 8), (27.136, 8)), ((27, 8), (27.136, 8), (27, 8)))
        self.add_bezier('e5', (21, 8), ((20.864, 8), (21, 8.01), (20.855, 8.01)), ((19.5, 8.01), (18.582, 9.67), (18.545, 11)), ((18.536, 11.33), (19, 11.67), (19, 12)))
        self.add_bezier('e6', (29, 11), ((34.218, 13.14), (38.536, 16.69), (40.355, 22.62)), ((40.827, 24.17), (41.118, 25.78), (41.218, 27.41)), ((41.255, 27.96), (41.264, 28.52), (41.255, 29.07)), ((41.245, 29.23), (41.245, 29.39), (41.236, 29.55)), ((41.382, 29.73), (41.627, 29.73), (41.827, 29.83)), ((42.909, 30.38), (43.982, 31.13), (43.982, 32.62)), ((43.991, 32.78), (43.991, 32.94), (44, 33.11)), ((44, 33.111), (44, 33.112), (44, 33.113)), ((44, 33.182), (44, 33.261), (43.991, 33.33)), ((43.991, 35.3), (41.309, 36.57), (39.936, 37.17)), ((35.4, 39.17), (30.164, 39.98), (25.3, 39.98)), ((24.927, 39.98), (24.555, 40), (24.182, 40)), ((24.174, 40), (24.165, 40), (24.157, 40)), ((23.638, 40), (23.128, 39.98), (22.618, 39.98)), ((17.764, 39.98), (12.6, 39.13), (8.064, 37.23)), ((6.636, 36.64), (4.009, 35.47), (4.009, 33.42)), ((4.009, 33.341), (4, 33.272), (4, 33.194)), ((4, 33.192), (4, 33.191), (4, 33.19)), ((4, 33), (4.018, 32.81), (4.018, 32.61)), ((4.018, 31.3), (4.918, 30.45), (5.918, 29.95)), ((6.082, 29.87), (6.582, 29.74), (6.691, 29.6)), ((6.7, 29.59), (6.682, 27.88), (6.691, 27.69)), ((6.773, 26.06), (7.045, 24.45), (7.5, 22.89)), ((9.273, 16.82), (13.691, 13.17), (19, 11)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5', 'e2')
        self.add_contour('c1', 'e6')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c1', 'c0')
