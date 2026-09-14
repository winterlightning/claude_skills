"""Elastic load balance circle (programing), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b5811619-4d2e-4d0e-bd82-0ceb97f8b687'
SOURCE_PATH = 'icons-json/programing/elastic load balance circle_b5811619-4d2e-4d0e-bd82-0ceb97f8b687.json'
AUTHOR = 'json_to_solo'

class ElasticLoadBalanceCirclePrograming(Solo48):
    icon_id = 'elastic-load-balance-circle-programing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('elastic', 'load', 'balance', 'circle', 'programing')

    def build(self):
        self.add_arc('sym-e0', (35, 24), (41, 24), radius_x=3)
        self.add_arc('sym-e1', (41, 24), (35, 24), radius_x=3)
        self.add_arc('sym-e2', (6, 24), (21, 24), radius_x=7)
        self.add_arc('sym-e3', (21, 24), (6, 24), radius_x=7)
        self.add_arc('sym-e4', (34, 10), (42, 10), radius_x=4)
        self.add_arc('sym-e5', (42, 10), (35, 13), radius_x=4)
        self.add_arc('sym-e6', (35, 13), (34, 10), radius_x=4)
        self.add_arc('sym-e7', (34, 38), (42, 38), radius_x=4, sweep=False)
        self.add_arc('sym-e8', (42, 38), (35, 35), radius_x=4, sweep=False)
        self.add_arc('sym-e9', (35, 35), (34, 38), radius_x=4, sweep=False)
        self.add_line('sym-e10', (35, 24), (34, 24))
        self.add_line('sym-e11', (34, 24), (23, 24))
        self.add_line('sym-e12', (23, 24), (21, 24))
        self.add_line('sym-e13', (21, 24), (22, 22))
        self.add_line('sym-e14', (22, 22), (34, 13))
        self.add_line('sym-e15', (34, 13), (35, 13))
        self.add_line('sym-e16', (21, 24), (22, 26))
        self.add_line('sym-e17', (22, 26), (34, 35))
        self.add_line('sym-e18', (34, 35), (35, 35))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6', closed=True)
        self.add_contour('sym-c3', 'sym-e7', 'sym-e8', 'sym-e9', closed=True)
        self.add_contour('sym-c4', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.add_contour('sym-c5', 'sym-e16', 'sym-e17', 'sym-e18')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c2', 'sym-c4')
        self.relate('connect', 'sym-c3', 'sym-c5')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c3', 'sym-c5')
        self.relate('connect', 'sym-c2', 'sym-c4')
