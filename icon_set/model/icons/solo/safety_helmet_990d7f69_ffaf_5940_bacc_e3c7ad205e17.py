"""Safety helmet (construction), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '990d7f69-ffaf-5940-bacc-e3c7ad205e17'
SOURCE_PATH = 'icons-json/construction/safety helmet_990d7f69-ffaf-5940-bacc-e3c7ad205e17.json'
AUTHOR = 'json_to_solo'

class SafetyHelmetConstruction(Solo48):
    icon_id = 'safety-helmet-construction'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('safety', 'helmet', 'construction')

    def build(self):
        self.add_line('e0', (30, 11), (29, 23))
        self.add_line('e1', (21, 8), (27, 8))
        self.add_line('e2', (18, 11), (19, 23))
        self.add_bezier('e3', (18, 11), ((13.145, 13.43), (9.536, 16.3), (7.455, 21.87)), ((6.836, 23.51), (6.473, 25.34), (6.4, 27.11)), ((6.373, 27.71), (6.364, 28.3), (6.345, 28.89)), ((6.345, 28.99), (6.345, 29.09), (6.345, 29.19)), ((6.109, 29.3), (5.882, 29.42), (5.645, 29.53)), ((4.682, 30.03), (4.018, 31.1), (4.018, 32.28)), ((4.018, 32.55), (4, 32.82), (4, 33.09)), ((4, 33.094), (4, 33.098), (4, 33.101)), ((4, 33.338), (4.009, 33.584), (4.009, 33.82)), ((4.009, 36), (7.2, 36.7), (8.445, 37.22)), ((12.391, 38.86), (17.755, 39.98), (21.973, 39.98)), ((22.455, 39.98), (22.936, 40), (23.409, 40)), ((23.419, 40), (23.43, 40), (23.44, 40)), ((24.094, 40), (24.756, 39.98), (25.409, 39.98)), ((30.355, 39.98), (35.209, 38.88), (39.864, 37.07)), ((41.473, 36.45), (43.982, 35.92), (43.982, 33.59)), ((43.991, 33.51), (43.991, 33.44), (44, 33.36)), ((44, 33.358), (44, 33.357), (44, 33.355)), ((44, 33.247), (43.991, 33.138), (43.991, 33.03)), ((43.991, 31.88), (43.809, 30.76), (42.973, 29.97)), ((42.673, 29.69), (41.727, 29.45), (41.582, 29.24)), ((41.518, 29.15), (41.509, 27.4), (41.491, 27.12)), ((41.373, 25.49), (41.1, 23.97), (40.627, 22.43)), ((38.864, 16.73), (34.873, 13.36), (30, 11)))
        self.add_bezier('e4', (18, 11), ((18.627, 9.27), (19.191, 8.02), (21.045, 8.02)), ((21.118, 8.01), (20.927, 8.01), (21, 8)))
        self.add_bezier('e5', (27, 8), ((27.145, 8), (27.018, 8.01), (27.155, 8.01)), ((28.864, 8.01), (29.518, 9.42), (30, 11)))
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e4', 'e1', 'e5')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
