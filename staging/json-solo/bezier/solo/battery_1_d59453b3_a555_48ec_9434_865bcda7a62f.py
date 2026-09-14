"""Battery 1 (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd59453b3-a555-48ec-9434-865bcda7a62f'
SOURCE_PATH = 'icons-json/state/battery 1_d59453b3-a555-48ec-9434-865bcda7a62f.json'
AUTHOR = 'json_to_solo'

class Battery1State(Solo48):
    icon_id = 'battery-1-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('battery', 'state')

    def build(self):
        self.add_line('e0', (44, 19), (44, 29))
        self.add_line('e1', (42, 31), (37, 31))
        self.add_line('e2', (36, 17), (36, 31))
        self.add_line('e3', (36, 17), (36, 10))
        self.add_line('e4', (33, 8), (29, 8))
        self.add_line('e5', (29, 8), (31, 8))
        self.add_line('e6', (31, 8), (6, 8))
        self.add_line('e7', (4, 10), (4, 38))
        self.add_line('e8', (6, 40), (31, 40))
        self.add_line('e9', (31, 40), (29, 40))
        self.add_line('e10', (29, 40), (33, 40))
        self.add_line('e11', (36, 38), (36, 31))
        self.add_bezier('e12', (37, 17), ((38.882, 17.012), (42.573, 16.074), (43.809, 18.326)), ((43.936, 18.56), (43.9, 18.778), (44, 19)))
        self.add_bezier('e13', (44, 29), ((44, 29.086), (43.991, 29.095), (43.991, 29.182)), ((43.991, 29.969), (42.536, 31), (42, 31)))
        self.add_bezier('e14', (36, 10), ((35.527, 8.72), (34.682, 8.025), (33.482, 8.025)), ((33.409, 8.012), (33.336, 8.012), (33.264, 8)), ((32.891, 8), (31.491, 8), (33, 8)))
        self.add_bezier('e15', (6, 8), ((4.791, 8.825), (4.609, 8.338), (4, 10)))
        self.add_bezier('e16', (4, 38), ((4.518, 39.465), (4.936, 39.262), (6, 40)))
        self.add_bezier('e17', (33, 40), ((31.427, 40), (33.236, 39.988), (33.655, 39.988)), ((34.555, 39.988), (36, 39.366), (36, 38)))
        self.add_bezier('e18', (36, 17), ((36.3, 17), (36.7, 17), (37, 17)))
        self.add_bezier('e19', (36, 31), ((36.3, 31), (36.7, 31), (37, 31)))
        self.add_contour('c0', 'e12', 'e0', 'e13', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e14', 'e4', 'e5', 'e6', 'e15', 'e7', 'e16', 'e8', 'e9', 'e10', 'e17', 'e11')
        self.add_contour('c3', 'e18')
        self.add_contour('c4', 'e19')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
