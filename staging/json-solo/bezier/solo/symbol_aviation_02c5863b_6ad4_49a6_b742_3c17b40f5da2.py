"""Symbol aviation (war), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02c5863b-6ad4-49a6-b742-3c17b40f5da2'
SOURCE_PATH = 'icons-json/war/symbol aviation_02c5863b-6ad4-49a6-b742-3c17b40f5da2.json'
AUTHOR = 'json_to_solo'

class SymbolAviationWar(Solo48):
    icon_id = 'symbol-aviation-war'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('symbol', 'aviation', 'war')

    def build(self):
        self.add_bezier('sym-e0', (24, 22), ((21.118, 28.098), (16.7, 40), (12, 40)))
        self.add_bezier('sym-e1', (12, 40), ((11.936, 40), (12.064, 40), (12, 40)))
        self.add_bezier('sym-e2', (12, 40), ((11.8, 40), (11.2, 40), (11, 40)))
        self.add_bezier('sym-e3', (11, 40), ((7.109, 40), (4, 32.342), (4, 25)))
        self.add_bezier('sym-e4', (4, 25), ((4, 24.858), (4, 25.142), (4, 25)))
        self.add_bezier('sym-e5', (4, 25), ((4, 24.733), (4, 24.267), (4, 24)))
        self.add_bezier('sym-e6', (4, 24), ((4, 21.031), (4.2, 17.489), (5, 15)))
        self.add_bezier('sym-e7', (5, 15), ((5.818, 12.458), (7.6, 11.244), (9, 10)))
        self.add_bezier('sym-e8', (9, 10), ((10.042, 9.073), (10.983, 8), (12, 8)))
        self.add_bezier('sym-e9', (12, 8), ((15.039, 8), (17.657, 12.044), (20, 16)))
        self.add_bezier('sym-e10', (20, 16), ((21.018, 17.724), (22.036, 19.151), (23, 21)))
        self.add_bezier('sym-e11', (23, 21), ((23.297, 21.581), (23.703, 21.419), (24, 22)))
        self.add_bezier('sym-e12', (24, 22), ((26.882, 28.098), (31.3, 40), (36, 40)))
        self.add_bezier('sym-e13', (36, 40), ((36.064, 40), (35.936, 40), (36, 40)))
        self.add_bezier('sym-e14', (36, 40), ((36.2, 40), (36.8, 40), (37, 40)))
        self.add_bezier('sym-e15', (37, 40), ((40.891, 40), (44, 32.342), (44, 25)))
        self.add_bezier('sym-e16', (44, 25), ((44, 24.858), (44, 25.142), (44, 25)))
        self.add_bezier('sym-e17', (44, 25), ((44, 24.733), (44, 24.267), (44, 24)))
        self.add_bezier('sym-e18', (44, 24), ((44, 21.031), (43.8, 17.489), (43, 15)))
        self.add_bezier('sym-e19', (43, 15), ((42.182, 12.458), (40.4, 11.244), (39, 10)))
        self.add_bezier('sym-e20', (39, 10), ((37.958, 9.073), (37.017, 8), (36, 8)))
        self.add_bezier('sym-e21', (36, 8), ((32.961, 8), (30.343, 12.044), (28, 16)))
        self.add_bezier('sym-e22', (28, 16), ((26.982, 17.724), (25.964, 19.151), (25, 21)))
        self.add_bezier('sym-e23', (25, 21), ((24.703, 21.581), (24.297, 21.419), (24, 22)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
