"""Soap (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ee9ecc8-c1c5-4fbd-86bf-4c3aaf9a18f4'
SOURCE_PATH = 'icons-json/symbol/soap_4ee9ecc8-c1c5-4fbd-86bf-4c3aaf9a18f4.json'
AUTHOR = 'json_to_solo'

class SoapSymbol(Solo48):
    icon_id = 'soap-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('soap', 'symbol')

    def build(self):
        self.add_bezier('sym-e0', (4, 22), ((5.709, 23.12), (7.236, 24.015), (9, 25)))
        self.add_bezier('sym-e1', (9, 25), ((12.8, 27.105), (16.936, 28), (21, 28)))
        self.add_line('sym-e2', (21, 28), (24, 28))
        self.add_line('sym-e3', (24, 28), (27, 28))
        self.add_bezier('sym-e4', (27, 28), ((31.064, 28), (35.2, 27.105), (39, 25)))
        self.add_bezier('sym-e5', (39, 25), ((40.764, 24.015), (42.291, 23.12), (44, 22)))
        self.add_line('sym-e6', (44, 22), (44, 29))
        self.add_bezier('sym-e7', (44, 29), ((44, 29.271), (44, 29.729), (44, 30)))
        self.add_bezier('sym-e8', (44, 30), ((44, 32.56), (42.482, 34.782), (41, 36)))
        self.add_bezier('sym-e9', (41, 36), ((37.509, 38.855), (33.036, 40), (29, 40)))
        self.add_bezier('sym-e10', (29, 40), ((28.8, 40), (28.2, 40), (28, 40)))
        self.add_bezier('sym-e11', (28, 40), ((27.582, 40), (27.418, 40), (27, 40)))
        self.add_line('sym-e12', (27, 40), (24, 40))
        self.add_line('sym-e13', (24, 40), (21, 40))
        self.add_bezier('sym-e14', (21, 40), ((20.582, 40), (20.418, 40), (20, 40)))
        self.add_bezier('sym-e15', (20, 40), ((19.8, 40), (19.2, 40), (19, 40)))
        self.add_bezier('sym-e16', (19, 40), ((14.964, 40), (10.491, 38.855), (7, 36)))
        self.add_bezier('sym-e17', (7, 36), ((5.518, 34.782), (4, 32.56), (4, 30)))
        self.add_bezier('sym-e18', (4, 30), ((4, 29.729), (4, 29.271), (4, 29)))
        self.add_line('sym-e19', (4, 29), (4, 22))
        self.add_line('sym-e20', (4, 22), (4, 17))
        self.add_bezier('sym-e21', (4, 17), ((4.064, 16.705), (4, 16.295), (4, 16)))
        self.add_bezier('sym-e22', (4, 16), ((4.218, 15.2), (4.582, 13.64), (5, 13)))
        self.add_bezier('sym-e23', (5, 13), ((7.3, 9.492), (11.745, 8.591), (15, 8)))
        self.add_bezier('sym-e24', (15, 8), ((15.527, 8), (16.455, 8), (17, 8)))
        self.add_line('sym-e25', (17, 8), (24, 8))
        self.add_line('sym-e26', (24, 8), (31, 8))
        self.add_bezier('sym-e27', (31, 8), ((31.545, 8), (32.473, 8), (33, 8)))
        self.add_bezier('sym-e28', (33, 8), ((36.255, 8.591), (40.7, 9.492), (43, 13)))
        self.add_bezier('sym-e29', (43, 13), ((43.418, 13.64), (43.782, 15.2), (44, 16)))
        self.add_bezier('sym-e30', (44, 16), ((44, 16.295), (43.936, 16.705), (44, 17)))
        self.add_line('sym-e31', (44, 17), (44, 22))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31')
