"""Skull 2 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b30b6f33-77c4-460d-b4be-c506ddae4ff2'
SOURCE_PATH = 'icons-json/interface-essential/skull 2_b30b6f33-77c4-460d-b4be-c506ddae4ff2.json'
AUTHOR = 'json_to_solo'

class Skull2InterfaceEssential(Solo48):
    icon_id = 'skull-2-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('skull', 'interface-essential')

    def build(self):
        self.add_line('e0', (31, 24), (35, 22))
        self.add_line('e1', (18, 24), (14, 22))
        self.add_line('e2', (15, 42), (15, 38))
        self.add_line('e3', (38, 33), (35, 35))
        self.add_line('e4', (34, 38), (34, 42))
        self.add_line('e5', (24, 42), (24, 40))
        self.add_bezier('e6', (15, 38), ((15, 34.899), (11.277, 34.006), (9.297, 32.37)), ((7.006, 30.48), (6.016, 27.805), (6.016, 24.875)), ((6.016, 24.54), (6, 24.205), (6, 23.869)), ((6, 23.866), (6, 23.863), (6, 23.86)), ((6, 23.658), (6.008, 23.457), (6.008, 23.255)), ((6.008, 13.724), (13.936, 6.008), (23.395, 6.008)), ((23.596, 6.008), (23.797, 6), (24.006, 6)), ((24.01, 6), (24.013, 6), (24.016, 6)), ((24.327, 6), (24.646, 6.008), (24.965, 6.008)), ((26.782, 6.008), (28.68, 6.434), (30.382, 7.031)), ((36.355, 9.117), (40.216, 13.699), (41.517, 19.819)), ((41.763, 20.981), (41.992, 22.192), (41.992, 23.378)), ((41.992, 23.571), (42, 23.757), (42, 23.95)), ((42, 23.953), (42, 23.956), (42, 23.959)), ((42, 24.155), (41.992, 24.352), (41.992, 24.548)), ((41.992, 27.412), (40.765, 31.617), (38, 33)))
        self.add_bezier('e7', (35, 35), ((34.665, 35.548), (33.843, 35.79), (33.736, 36.445)), ((33.663, 36.935), (34, 37.517), (34, 38)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e6', 'e3', 'e7', 'e4')
        self.add_contour('c3', 'e5')
