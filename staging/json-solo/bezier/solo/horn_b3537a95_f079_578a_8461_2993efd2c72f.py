"""Horn (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3537a95-f079-578a-8461-2993efd2c72f'
SOURCE_PATH = 'icons-json/transportation/horn_b3537a95-f079-578a-8461-2993efd2c72f.json'
AUTHOR = 'json_to_solo'

class HornB3537a95(Solo48):
    icon_id = 'horn-b3537a95'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('horn', 'transportation')

    def build(self):
        self.add_line('sym-e0', (4, 10), (4, 38))
        self.add_bezier('sym-e1', (4, 38), ((5.327, 36.105), (6.173, 34.533), (8, 33)))
        self.add_bezier('sym-e2', (8, 33), ((12.4, 29.328), (18.382, 28.095), (24, 27)))
        self.add_bezier('sym-e3', (24, 27), ((27.055, 26.402), (29.873, 26.101), (33, 26)))
        self.add_bezier('sym-e4', (33, 26), ((32.88, 25.458), (33, 24.48), (33, 24)))
        self.add_bezier('sym-e5', (33, 24), ((33, 23.94), (33.005, 24.06), (33, 24)))
        self.add_bezier('sym-e6', (33, 24), ((33.005, 23.94), (33, 24.06), (33, 24)))
        self.add_bezier('sym-e7', (33, 24), ((33, 23.52), (32.88, 22.542), (33, 22)))
        self.add_bezier('sym-e8', (33, 22), ((29.873, 21.899), (27.055, 21.598), (24, 21)))
        self.add_bezier('sym-e9', (24, 21), ((18.382, 19.905), (12.4, 18.672), (8, 15)))
        self.add_bezier('sym-e10', (8, 15), ((6.173, 13.467), (5.327, 11.895), (4, 10)))
        self.add_line('sym-e11', (4, 10), (4, 8))
        self.add_bezier('sym-e12', (33, 22), ((33.927, 20.358), (34.991, 19.488), (37, 19)))
        self.add_bezier('sym-e13', (37, 19), ((40.282, 18.217), (44, 20.834), (44, 24)))
        self.add_bezier('sym-e14', (44, 24), ((44, 24.087), (43.997, 23.913), (44, 24)))
        self.add_bezier('sym-e15', (44, 24), ((43.997, 24.087), (44, 23.913), (44, 24)))
        self.add_bezier('sym-e16', (44, 24), ((44, 27.166), (40.282, 29.783), (37, 29)))
        self.add_bezier('sym-e17', (37, 29), ((34.991, 28.512), (33.927, 27.642), (33, 26)))
        self.add_line('sym-e18', (4, 38), (4, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17')
        self.add_contour('sym-c2', 'sym-e18')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
