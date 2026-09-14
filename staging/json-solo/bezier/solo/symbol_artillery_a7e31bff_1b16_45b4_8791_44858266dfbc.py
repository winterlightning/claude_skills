"""Symbol artillery (war), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7e31bff-1b16-45b4-8791-44858266dfbc'
SOURCE_PATH = 'icons-json/war/symbol artillery_a7e31bff-1b16-45b4-8791-44858266dfbc.json'
AUTHOR = 'json_to_solo'

class SymbolArtilleryWar(Solo48):
    icon_id = 'symbol-artillery-war'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('symbol', 'artillery', 'war')

    def build(self):
        self.add_line('e0', (24, 4), (24, 14))
        self.add_line('e1', (9, 25), (9, 36))
        self.add_line('e2', (39, 36), (39, 25))
        self.add_line('e3', (8, 12), (8, 4))
        self.add_line('e4', (8, 4), (24, 14))
        self.add_line('e5', (24, 17), (24, 14))
        self.add_line('e6', (24, 14), (30, 10))
        self.add_line('e7', (30, 10), (40, 4))
        self.add_line('e8', (40, 4), (40, 13))
        self.add_bezier('e9', (15, 19), ((12.6, 20.573), (9, 22.627), (9, 25)))
        self.add_bezier('e10', (9, 36), ((9, 40.336), (16.785, 44), (23.52, 44)), ((23.526, 44), (23.531, 44), (23.537, 44)), ((23.895, 44), (24.238, 43.991), (24.596, 43.991)), ((30.458, 43.991), (35.84, 41), (37.775, 37.7)), ((38.109, 37.136), (39, 36.609), (39, 36)))
        self.add_bezier('e11', (39, 25), ((39, 22.327), (35.895, 20.718), (33, 19)))
        self.add_bezier('e12', (15, 19), ((17.953, 18.073), (20.655, 17.082), (24, 17)))
        self.add_bezier('e13', (15, 19), ((12.135, 17.482), (9.847, 15.591), (8.509, 13.345)), ((8.276, 12.964), (8, 12.409), (8, 12)))
        self.add_bezier('e14', (24, 17), ((27.302, 17.073), (30.105, 18.082), (33, 19)))
        self.add_bezier('e15', (40, 13), ((38.589, 15.673), (36.549, 17.345), (33, 19)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e9', 'e1', 'e10', 'e2', 'e11')
        self.add_contour('c2', 'e12')
        self.add_contour('c3', 'e13', 'e3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e14')
        self.add_contour('c6', 'e6', 'e7', 'e8', 'e15')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
