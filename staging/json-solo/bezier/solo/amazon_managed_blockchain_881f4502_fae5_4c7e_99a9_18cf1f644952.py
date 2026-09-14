"""Amazon managed blockchain (programing), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '881f4502-fae5-4c7e-99a9-18cf1f644952'
SOURCE_PATH = 'icons-json/programing/amazon managed blockchain_881f4502-fae5-4c7e-99a9-18cf1f644952.json'
AUTHOR = 'json_to_solo'

class AmazonManagedBlockchainPrograming(Solo48):
    icon_id = 'amazon-managed-blockchain-programing'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('amazon', 'managed', 'blockchain', 'programing')

    def build(self):
        self.add_line('sym-e0', (19, 24), (29, 24))
        self.add_line('sym-e1', (29, 24), (29, 10))
        self.add_bezier('sym-e2', (29, 10), ((29.164, 9.591), (28.8, 8.356), (29, 8)))
        self.add_bezier('sym-e3', (29, 8), ((29.118, 8), (28.882, 8.196), (29, 8)))
        self.add_line('sym-e4', (29, 8), (42, 8))
        self.add_bezier('sym-e5', (42, 8), ((42.073, 8), (41.927, 8), (42, 8)))
        self.add_bezier('sym-e6', (42, 8), ((42.618, 8), (43.545, 9.342), (44, 10)))
        self.add_line('sym-e7', (44, 10), (44, 24))
        self.add_line('sym-e8', (44, 24), (44, 38))
        self.add_bezier('sym-e9', (44, 38), ((43.545, 38.658), (42.618, 40), (42, 40)))
        self.add_bezier('sym-e10', (42, 40), ((41.927, 40), (42.073, 40), (42, 40)))
        self.add_line('sym-e11', (42, 40), (29, 40))
        self.add_bezier('sym-e12', (29, 40), ((28.882, 39.804), (29.118, 40), (29, 40)))
        self.add_bezier('sym-e13', (29, 40), ((28.8, 39.644), (29.164, 38.409), (29, 38)))
        self.add_line('sym-e14', (29, 38), (29, 24))
        self.add_line('sym-e15', (19, 24), (19, 12))
        self.add_bezier('sym-e16', (19, 12), ((18.909, 10.898), (19.4, 9.907), (19, 9)))
        self.add_bezier('sym-e17', (19, 9), ((18.891, 8.751), (19.091, 8.196), (19, 8)))
        self.add_line('sym-e18', (19, 8), (5, 8))
        self.add_bezier('sym-e19', (5, 8), ((4.627, 8.924), (4, 9.72), (4, 11)))
        self.add_bezier('sym-e20', (4, 11), ((4, 11.124), (4, 11.876), (4, 12)))
        self.add_line('sym-e21', (4, 12), (4, 24))
        self.add_line('sym-e22', (4, 24), (4, 36))
        self.add_bezier('sym-e23', (4, 36), ((4, 36.124), (4, 36.876), (4, 37)))
        self.add_bezier('sym-e24', (4, 37), ((4, 38.28), (4.627, 39.076), (5, 40)))
        self.add_line('sym-e25', (5, 40), (19, 40))
        self.add_bezier('sym-e26', (19, 40), ((19.091, 39.804), (18.891, 39.249), (19, 39)))
        self.add_bezier('sym-e27', (19, 39), ((19.4, 38.093), (18.909, 37.102), (19, 36)))
        self.add_line('sym-e28', (19, 36), (19, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
        self.add_contour('sym-c1', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
