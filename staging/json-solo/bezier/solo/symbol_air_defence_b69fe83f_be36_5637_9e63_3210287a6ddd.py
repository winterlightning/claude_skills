"""Symbol air defence (war), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b69fe83f-be36-5637-9e63-3210287a6ddd'
SOURCE_PATH = 'icons-json/war/symbol air defence_b69fe83f-be36-5637-9e63-3210287a6ddd.json'
AUTHOR = 'json_to_solo'

class SymbolAirDefenceWar(Solo48):
    icon_id = 'symbol-air-defence-war'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('symbol', 'air', 'defence', 'war')

    def build(self):
        self.add_line('sym-e0', (24, 40), (6, 40))
        self.add_bezier('sym-e1', (6, 40), ((5.373, 39.631), (4.609, 39.455), (4, 39)))
        self.add_bezier('sym-e2', (4, 39), ((4.918, 36.711), (6.473, 34.662), (8, 33)))
        self.add_bezier('sym-e3', (8, 33), ((12.13, 28.493), (18.133, 26), (24, 26)))
        self.add_bezier('sym-e4', (24, 26), ((24.041, 26), (23.959, 26), (24, 26)))
        self.add_bezier('sym-e5', (24, 26), ((24.041, 26), (23.959, 26), (24, 26)))
        self.add_bezier('sym-e6', (24, 26), ((29.867, 26), (35.87, 28.493), (40, 33)))
        self.add_bezier('sym-e7', (40, 33), ((41.527, 34.662), (43.082, 36.711), (44, 39)))
        self.add_bezier('sym-e8', (44, 39), ((43.391, 39.455), (42.627, 39.631), (42, 40)))
        self.add_line('sym-e9', (42, 40), (24, 40))
        self.add_line('sym-e10', (24, 8), (6, 8))
        self.add_bezier('sym-e11', (6, 8), ((5.173, 8.418), (4.527, 8.757), (4, 10)))
        self.add_bezier('sym-e12', (4, 10), ((4, 10.271), (4.082, 9.717), (4, 10)))
        self.add_line('sym-e13', (4, 10), (4, 39))
        self.add_line('sym-e14', (24, 8), (42, 8))
        self.add_bezier('sym-e15', (42, 8), ((42.827, 8.418), (43.473, 8.757), (44, 10)))
        self.add_bezier('sym-e16', (44, 10), ((44, 10.271), (43.918, 9.717), (44, 10)))
        self.add_line('sym-e17', (44, 10), (44, 39))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', closed=True)
        self.add_contour('sym-c1', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13')
        self.add_contour('sym-c2', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
