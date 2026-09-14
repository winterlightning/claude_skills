"""Symbol mountain infantry (war), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '56fac8f8-8d3d-40b1-a35c-415b751a3a8b'
SOURCE_PATH = 'icons-json/war/symbol mountain infantry_56fac8f8-8d3d-40b1-a35c-415b751a3a8b.json'
AUTHOR = 'json_to_solo'

class SymbolMountainInfantryWar(Solo48):
    icon_id = 'symbol-mountain-infantry-war'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('symbol', 'mountain', 'infantry', 'war')

    def build(self):
        self.add_line('e0', (19, 21), (17, 18))
        self.add_line('e1', (17, 18), (4, 39))
        self.add_line('e2', (5, 40), (30, 40))
        self.add_line('e3', (19, 21), (30, 40))
        self.add_line('e4', (19, 21), (27, 9))
        self.add_line('e5', (28, 9), (43, 35))
        self.add_line('e6', (42, 40), (30, 40))
        self.add_bezier('e7', (4, 39), ((4.2, 39.26), (4.3, 39.58), (4.536, 39.8)), ((4.664, 39.87), (4.873, 39.93), (5, 40)))
        self.add_bezier('e8', (27, 9), ((27.17, 8.675), (27.067, 8), (27.228, 8)), ((27.231, 8), (27.234, 8.005), (27.236, 8)), ((27.373, 8.33), (27.864, 8.67), (28, 9)))
        self.add_bezier('e9', (43, 35), ((43.364, 35.61), (44, 36.69), (44, 37.42)), ((44, 37.421), (44, 37.423), (44, 37.424)), ((44, 37.513), (43.991, 37.601), (43.982, 37.69)), ((43.982, 38.47), (43.3, 39.37), (42.745, 39.79)), ((42.564, 39.93), (42.173, 39.89), (42, 40)))
        self.add_contour('c0', 'e0', 'e1', 'e7', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e8', 'e5', 'e9', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
