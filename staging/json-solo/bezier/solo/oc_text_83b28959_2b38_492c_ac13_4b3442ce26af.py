"""Oc (text) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '83b28959-2b38-492c-ac13-4b3442ce26af'
SOURCE_PATH = 'icons-json/symbol/OC (text)_83b28959-2b38-492c-ac13-4b3442ce26af.json'
AUTHOR = 'json_to_solo'

class OcTextSymbol(Solo48):
    icon_id = 'oc-text-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('oc', 'text', 'symbol')

    def build(self):
        self.add_bezier('sym-e0', (44, 13), ((43.909, 12.78), (44, 12.21), (44, 12)))
        self.add_bezier('sym-e1', (44, 12), ((42.8, 9.7), (40.545, 8), (38, 8)))
        self.add_bezier('sym-e2', (38, 8), ((37.855, 8), (38.145, 8), (38, 8)))
        self.add_bezier('sym-e3', (38, 8), ((37.855, 8.01), (37.145, 8), (37, 8)))
        self.add_bezier('sym-e4', (37, 8), ((33.336, 8), (30, 12.15), (30, 16)))
        self.add_line('sym-e5', (30, 16), (30, 24))
        self.add_line('sym-e6', (30, 24), (30, 32))
        self.add_bezier('sym-e7', (30, 32), ((30, 35.85), (33.336, 40), (37, 40)))
        self.add_bezier('sym-e8', (37, 40), ((37.145, 40), (37.855, 39.99), (38, 40)))
        self.add_bezier('sym-e9', (38, 40), ((38.145, 40), (37.855, 40), (38, 40)))
        self.add_bezier('sym-e10', (38, 40), ((40.545, 40), (42.8, 38.3), (44, 36)))
        self.add_bezier('sym-e11', (44, 36), ((44, 35.79), (43.909, 35.22), (44, 35)))
        self.add_line('sym-e12', (19, 24), (19, 16))
        self.add_bezier('sym-e13', (19, 16), ((19, 11.83), (15.764, 8), (12, 8)))
        self.add_bezier('sym-e14', (12, 8), ((11.855, 8), (12.145, 8), (12, 8)))
        self.add_bezier('sym-e15', (12, 8), ((11.855, 8.01), (11.145, 8), (11, 8)))
        self.add_bezier('sym-e16', (11, 8), ((7.091, 8), (4, 12.86), (4, 17)))
        self.add_bezier('sym-e17', (4, 17), ((4, 17.08), (4, 16.93), (4, 17)))
        self.add_bezier('sym-e18', (4, 17), ((4, 17.08), (4, 16.92), (4, 17)))
        self.add_line('sym-e19', (4, 17), (4, 24))
        self.add_line('sym-e20', (4, 24), (4, 31))
        self.add_bezier('sym-e21', (4, 31), ((4, 31.08), (4, 30.92), (4, 31)))
        self.add_bezier('sym-e22', (4, 31), ((4, 31.07), (4, 30.92), (4, 31)))
        self.add_bezier('sym-e23', (4, 31), ((4, 35.14), (7.091, 40), (11, 40)))
        self.add_bezier('sym-e24', (11, 40), ((11.145, 40), (11.855, 39.99), (12, 40)))
        self.add_bezier('sym-e25', (12, 40), ((12.145, 40), (11.855, 40), (12, 40)))
        self.add_bezier('sym-e26', (12, 40), ((15.764, 40), (19, 36.17), (19, 32)))
        self.add_line('sym-e27', (19, 32), (19, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', closed=True)
