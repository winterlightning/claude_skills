"""Sauna heat stone (spas), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2e71463-3949-5bb1-825f-2b5f7009fede'
SOURCE_PATH = 'icons-json/spas/sauna heat stone_e2e71463-3949-5bb1-825f-2b5f7009fede.json'
AUTHOR = 'json_to_solo'

class SaunaHeatStoneSpas(Solo48):
    icon_id = 'sauna-heat-stone-spas'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'spas'
    aliases = ()
    keywords = ('sauna', 'heat', 'stone', 'spas')

    def build(self):
        self.add_line('e0', (15, 22), (13, 16))
        self.add_bezier('e1', (22, 29), ((23.645, 26.693), (25.276, 24.123), (24.949, 21.21)), ((24.663, 18.649), (23.067, 16.555), (22.396, 14.108)), ((21.595, 11.187), (23.11, 8.185), (25, 6)))
        self.add_bezier('e2', (6, 31), ((6, 31.491), (6.008, 31.527), (6.008, 32.018)), ((6.008, 34.219), (7.718, 36.15), (9.289, 37.467)), ((12.873, 40.478), (18.404, 41.992), (23.051, 41.992)), ((23.115, 41.992), (23.188, 42), (23.252, 42)), ((23.253, 42), (23.254, 42), (23.255, 42)), ((23.615, 42), (23.984, 41.984), (24.344, 41.984)), ((29.408, 41.984), (34.628, 40.805), (38.613, 37.549)), ((40.126, 36.314), (41.992, 34.088), (41.992, 31.994)), ((41.992, 31.936), (42, 31.879), (42, 31.822)), ((42, 31.396), (42, 31.425), (42, 31)))
        self.add_bezier('e3', (33, 27), ((33.507, 26.329), (33.974, 25.964), (34.268, 25.17)), ((35.864, 20.915), (32.722, 18.526), (32.1, 14.714)), ((31.666, 12.055), (33.298, 9.931), (35, 8)))
        self.add_bezier('e4', (13, 27), ((14.317, 25.249), (15.049, 24.168), (15, 22)))
        self.add_bezier('e5', (13, 16), ((12.861, 15.501), (13.233, 14.722), (13.192, 14.198)), ((12.979, 11.752), (13.462, 9.939), (15, 8)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e0', 'e5')
