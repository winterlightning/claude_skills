"""Network (networks), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1e9f2473-7774-5d81-917a-5de0d098f445'
SOURCE_PATH = 'icons-json/networks/network_1e9f2473-7774-5d81-917a-5de0d098f445.json'
AUTHOR = 'json_to_solo'

class NetworkNetworks(Solo48):
    icon_id = 'network-networks'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('network', 'networks')

    def build(self):
        self.add_arc('sym-e0', (19, 36), (24, 32), radius_x=5, radius_y=4)
        self.add_arc('sym-e1', (24, 32), (29, 36), radius_x=5, radius_y=4)
        self.add_arc('sym-e2', (29, 36), (19, 36), radius_x=5, radius_y=4)
        self.add_arc('sym-e3', (19, 12), (29, 12), radius_x=5, radius_y=4)
        self.add_arc('sym-e4', (29, 12), (24, 16), radius_x=5, radius_y=4)
        self.add_arc('sym-e5', (24, 16), (19, 12), radius_x=5, radius_y=4)
        self.add_arc('sym-e6', (35, 36), (39, 32), radius_x=5, radius_y=4)
        self.add_arc('sym-e7', (39, 32), (44, 36), radius_x=5, radius_y=4)
        self.add_arc('sym-e8', (44, 36), (35, 36), radius_x=5, radius_y=4)
        self.add_arc('sym-e9', (13, 36), (9, 32), radius_x=5, radius_y=4, sweep=False)
        self.add_arc('sym-e10', (9, 32), (4, 36), radius_x=5, radius_y=4, sweep=False)
        self.add_arc('sym-e11', (4, 36), (13, 36), radius_x=5, radius_y=4, sweep=False)
        self.add_line('sym-e12', (24, 16), (24, 24))
        self.add_line('sym-e13', (24, 24), (24, 32))
        self.add_line('sym-e14', (39, 32), (39, 27))
        self.add_bezier('sym-e15', (39, 27), ((39, 25.383), (38.673, 24), (37, 24)))
        self.add_line('sym-e16', (37, 24), (24, 24))
        self.add_line('sym-e17', (24, 24), (11, 24))
        self.add_bezier('sym-e18', (11, 24), ((9.327, 24), (9, 25.383), (9, 27)))
        self.add_line('sym-e19', (9, 27), (9, 32))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', closed=True)
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', closed=True)
        self.add_contour('sym-c2', 'sym-e6', 'sym-e7', 'sym-e8', closed=True)
        self.add_contour('sym-c3', 'sym-e9', 'sym-e10', 'sym-e11', closed=True)
        self.add_contour('sym-c4', 'sym-e12', 'sym-e13')
        self.add_contour('sym-c5', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c2', 'sym-c5')
        self.relate('connect', 'sym-c3', 'sym-c5')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c3', 'sym-c5')
        self.relate('connect', 'sym-c2', 'sym-c5')
