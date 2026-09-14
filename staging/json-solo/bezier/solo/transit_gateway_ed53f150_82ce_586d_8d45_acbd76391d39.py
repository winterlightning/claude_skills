"""Transit gateway (programing), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed53f150-82ce-586d-8d45-acbd76391d39'
SOURCE_PATH = 'icons-json/programing/transit gateway_ed53f150-82ce-586d-8d45-acbd76391d39.json'
AUTHOR = 'json_to_solo'

class TransitGatewayPrograming(Solo48):
    icon_id = 'transit-gateway-programing'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('transit', 'gateway', 'programing')

    def build(self):
        self.add_line('sym-e0', (20, 24), (10, 24))
        self.add_line('sym-e1', (10, 24), (4, 24))
        self.add_line('sym-e2', (44, 24), (30, 24))
        self.add_line('sym-e3', (30, 24), (30, 11))
        self.add_bezier('sym-e4', (30, 11), ((29.436, 9.669), (28.736, 8), (27, 8)))
        self.add_bezier('sym-e5', (27, 8), ((26.845, 8), (27.155, 8), (27, 8)))
        self.add_line('sym-e6', (27, 8), (15, 8))
        self.add_bezier('sym-e7', (15, 8), ((14.855, 8), (14.145, 8), (14, 8)))
        self.add_bezier('sym-e8', (14, 8), ((13.927, 8), (14.073, 8), (14, 8)))
        self.add_bezier('sym-e9', (14, 8), ((13.855, 8), (14.145, 8), (14, 8)))
        self.add_bezier('sym-e10', (14, 8), ((13.927, 8), (14.064, 8.008), (14, 8)))
        self.add_bezier('sym-e11', (14, 8), ((13.927, 8.008), (13.064, 8), (13, 8)))
        self.add_bezier('sym-e12', (13, 8), ((11.473, 8), (10.264, 9.754), (10, 11)))
        self.add_bezier('sym-e13', (10, 11), ((9.9, 11.488), (10, 11.528), (10, 12)))
        self.add_line('sym-e14', (10, 12), (10, 24))
        self.add_line('sym-e15', (10, 24), (10, 36))
        self.add_bezier('sym-e16', (10, 36), ((10, 36.472), (9.9, 36.512), (10, 37)))
        self.add_bezier('sym-e17', (10, 37), ((10.264, 38.246), (11.473, 40), (13, 40)))
        self.add_bezier('sym-e18', (13, 40), ((13.064, 40), (13.927, 39.992), (14, 40)))
        self.add_bezier('sym-e19', (14, 40), ((14.064, 39.992), (13.927, 40), (14, 40)))
        self.add_bezier('sym-e20', (14, 40), ((14.145, 40), (13.855, 40), (14, 40)))
        self.add_bezier('sym-e21', (14, 40), ((14.073, 40), (13.927, 40), (14, 40)))
        self.add_bezier('sym-e22', (14, 40), ((14.145, 40), (14.855, 40), (15, 40)))
        self.add_line('sym-e23', (15, 40), (27, 40))
        self.add_bezier('sym-e24', (27, 40), ((27.155, 40), (26.845, 40), (27, 40)))
        self.add_bezier('sym-e25', (27, 40), ((28.736, 40), (29.436, 38.331), (30, 37)))
        self.add_line('sym-e26', (30, 37), (30, 24))
        self.add_line('sym-e27', (44, 24), (39, 19))
        self.add_line('sym-e28', (44, 24), (39, 29))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26')
        self.add_contour('sym-c2', 'sym-e27')
        self.add_contour('sym-c3', 'sym-e28')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
