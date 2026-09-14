"""Plane 1 (travel), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18f96efa-93ca-4c4e-9556-e131c14f8073'
SOURCE_PATH = 'icons-json/travel/plane 1_18f96efa-93ca-4c4e-9556-e131c14f8073.json'
AUTHOR = 'json_to_solo'

class Plane118f96efa(Solo48):
    icon_id = 'plane-1-18f96efa'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('plane', 'travel')

    def build(self):
        self.add_line('e0', (4, 29), (16, 40))
        self.add_line('e1', (16, 40), (41, 19))
        self.add_line('e2', (39, 8), (29, 15))
        self.add_line('e3', (29, 15), (16, 12))
        self.add_line('e4', (16, 12), (9, 17))
        self.add_line('e5', (9, 17), (22, 23))
        self.add_line('e6', (22, 23), (17, 28))
        self.add_line('e7', (17, 28), (9, 25))
        self.add_line('e8', (9, 25), (4, 29))
        self.add_bezier('e9', (41, 19), ((42.555, 17.72), (43.991, 16.23), (43.991, 13.98)), ((43.991, 13.793), (44, 13.616), (44, 13.429)), ((44, 13.426), (44, 13.423), (44, 13.42)), ((44, 13.18), (43.991, 12.93), (43.991, 12.69)), ((43.991, 11.02), (43.445, 9.49), (42.227, 8.46)), ((42.064, 8.31), (41.755, 8), (41.527, 8)), ((40.973, 8), (40.418, 8.02), (39.864, 8.02)), ((39.682, 8.02), (39.509, 8.01), (39.327, 8.01)), ((39.291, 8.01), (39.245, 8), (39.2, 8)), ((38.982, 8), (39.218, 8), (39, 8)))
        self.add_contour('c0', 'e0', 'e1', 'e9', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8')
