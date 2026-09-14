"""Planting (outdoors), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9455f205-a8f4-5254-8cd0-5d2ae9ba19ea'
SOURCE_PATH = 'icons-json/outdoors/planting_9455f205-a8f4-5254-8cd0-5d2ae9ba19ea.json'
AUTHOR = 'json_to_solo'

class PlantingOutdoors(Solo48):
    icon_id = 'planting-outdoors'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('planting', 'outdoors')

    def build(self):
        self.add_line('e0', (25, 26), (25, 32))
        self.add_line('e1', (25, 18), (27, 14))
        self.add_line('e2', (30, 20), (25, 20))
        self.add_line('e3', (25, 18), (25, 26))
        self.add_line('e4', (10, 44), (40, 44))
        self.add_bezier('e5', (25, 18), ((24.343, 16.036), (23.579, 13.536), (22.602, 11.727)), ((20.227, 7.336), (16.253, 4.018), (11.394, 4.018)), ((10.947, 4.018), (10.493, 4), (10.046, 4)), ((10.037, 4), (10.029, 4), (10.02, 4)), ((9.464, 4), (8.909, 4.009), (8.354, 4.009)), ((8.253, 4.018), (8.143, 4.018), (8.042, 4.018)), ((8.025, 4.718), (8.017, 5.418), (8, 6.118)), ((8, 6.12), (8, 6.122), (8, 6.123)), ((8, 6.23), (8.009, 6.329), (8.017, 6.436)), ((8.017, 11.055), (10.501, 15.9), (14.021, 18.482)), ((14.703, 18.991), (15.419, 19.482), (16.16, 19.873)), ((17.76, 20.718), (19.52, 21.127), (21.069, 22.1)), ((22.535, 23.018), (23.821, 24.718), (25, 26)))
        self.add_bezier('e6', (27, 14), ((27.219, 13.536), (27.057, 13.109), (27.284, 12.645)), ((27.579, 12.045), (27.815, 11.418), (28.152, 10.836)), ((29.684, 8.145), (32.109, 6.191), (34.863, 5.209)), ((35.613, 4.936), (39.478, 4.391), (39.924, 4.709)), ((40, 4.764), (39.992, 5.509), (39.992, 5.636)), ((39.992, 5.782), (40, 5.918), (40, 6.064)), ((40, 6.273), (39.992, 6.482), (39.992, 6.691)), ((39.992, 11.427), (37.086, 15.882), (33.566, 18.427)), ((32.547, 19.164), (31.305, 20), (30, 20)))
        self.add_bezier('e7', (40, 44), ((38.728, 36.682), (31.267, 32.355), (24.842, 32.182)), ((19.183, 32.027), (13.491, 35.409), (10.754, 40.8)), ((10.257, 41.8), (10.286, 42.918), (10, 44)))
        self.add_contour('c0', 'e5', 'e0')
        self.add_contour('c1', 'e1', 'e6', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e7', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
