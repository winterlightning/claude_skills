"""Skull (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '83b97801-31fc-4c2f-86e6-c8775e2ddea6'
SOURCE_PATH = 'icons-json/interface-essential/skull_83b97801-31fc-4c2f-86e6-c8775e2ddea6.json'
AUTHOR = 'json_to_solo'

class Skull83b97801(Solo48):
    icon_id = 'skull-83b97801'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('skull', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (24, 34), (24, 42))
        self.add_line('sym-e1', (24, 42), (19, 42))
        self.add_bezier('sym-e2', (19, 42), ((18.869, 42), (19.131, 42), (19, 42)))
        self.add_bezier('sym-e3', (19, 42), ((18.681, 42), (18.319, 42), (18, 42)))
        self.add_bezier('sym-e4', (18, 42), ((17.826, 42), (17.192, 42), (17, 42)))
        self.add_bezier('sym-e5', (17, 42), ((16.461, 42), (16.47, 42), (16, 42)))
        self.add_bezier('sym-e6', (16, 42), ((11.934, 40.527), (13.735, 35.921), (12, 33)))
        self.add_bezier('sym-e7', (12, 33), ((11.157, 31.585), (9.186, 31.064), (8, 30)))
        self.add_bezier('sym-e8', (8, 30), ((6.339, 28.511), (6, 26.119), (6, 24)))
        self.add_bezier('sym-e9', (6, 24), ((6, 23.673), (6, 23.327), (6, 23)))
        self.add_bezier('sym-e10', (6, 23), ((6, 22.738), (6, 22.262), (6, 22)))
        self.add_bezier('sym-e11', (6, 22), ((6, 20.879), (6.746, 20.088), (7, 19)))
        self.add_bezier('sym-e12', (7, 19), ((8.407, 12.986), (12.117, 8.702), (18, 7)))
        self.add_bezier('sym-e13', (18, 7), ((19.448, 6.583), (21.478, 6), (23, 6)))
        self.add_bezier('sym-e14', (23, 6), ((23.049, 6), (22.951, 6), (23, 6)))
        self.add_bezier('sym-e15', (23, 6), ((23.305, 6), (23.696, 6), (24, 6)))
        self.add_bezier('sym-e16', (24, 6), ((24.304, 6), (24.695, 6), (25, 6)))
        self.add_bezier('sym-e17', (25, 6), ((25.049, 6), (24.951, 6), (25, 6)))
        self.add_bezier('sym-e18', (25, 6), ((26.522, 6), (28.552, 6.583), (30, 7)))
        self.add_bezier('sym-e19', (30, 7), ((35.883, 8.702), (39.593, 12.986), (41, 19)))
        self.add_bezier('sym-e20', (41, 19), ((41.254, 20.088), (42, 20.879), (42, 22)))
        self.add_bezier('sym-e21', (42, 22), ((42, 22.262), (42, 22.738), (42, 23)))
        self.add_bezier('sym-e22', (42, 23), ((42, 23.327), (42, 23.673), (42, 24)))
        self.add_bezier('sym-e23', (42, 24), ((42, 26.119), (41.661, 28.511), (40, 30)))
        self.add_bezier('sym-e24', (40, 30), ((38.814, 31.064), (36.843, 31.585), (36, 33)))
        self.add_bezier('sym-e25', (36, 33), ((34.265, 35.921), (36.066, 40.527), (32, 42)))
        self.add_bezier('sym-e26', (32, 42), ((31.53, 42), (31.539, 42), (31, 42)))
        self.add_bezier('sym-e27', (31, 42), ((30.808, 42), (30.174, 42), (30, 42)))
        self.add_bezier('sym-e28', (30, 42), ((29.681, 42), (29.319, 42), (29, 42)))
        self.add_bezier('sym-e29', (29, 42), ((28.869, 42), (29.131, 42), (29, 42)))
        self.add_line('sym-e30', (29, 42), (24, 42))
        self.add_bezier('sym-e31', (16, 24), ((16, 23.73), (16, 23.27), (16, 23)))
        self.add_bezier('sym-e32', (32, 24), ((32, 23.73), (32, 23.27), (32, 23)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30')
        self.add_contour('sym-c1', 'sym-e31')
        self.add_contour('sym-c2', 'sym-e32')
