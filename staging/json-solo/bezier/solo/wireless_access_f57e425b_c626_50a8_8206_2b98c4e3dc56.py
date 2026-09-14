"""Wireless access (networks), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f57e425b-c626-50a8-8206-2b98c4e3dc56'
SOURCE_PATH = 'icons-json/networks/wireless access_f57e425b-c626-50a8-8206-2b98c4e3dc56.json'
AUTHOR = 'json_to_solo'

class WirelessAccessNetworks(Solo48):
    icon_id = 'wireless-access-networks'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('wireless', 'access', 'networks')

    def build(self):
        self.add_arc('sym-e0', (8, 24), (20, 24), radius_x=6)
        self.add_arc('sym-e1', (20, 24), (8, 24), radius_x=6)
        self.add_bezier('sym-e2', (32, 4), ((32.943, 4.918), (33.158, 5.936), (34, 7)))
        self.add_bezier('sym-e3', (34, 7), ((37.276, 11.127), (40, 17.527), (40, 23)))
        self.add_bezier('sym-e4', (40, 23), ((40, 23.145), (39.992, 22.855), (40, 23)))
        self.add_bezier('sym-e5', (40, 23), ((40, 23.254), (40, 23.743), (40, 24)))
        self.add_bezier('sym-e6', (40, 24), ((40, 24.257), (40, 24.746), (40, 25)))
        self.add_bezier('sym-e7', (40, 25), ((39.992, 25.145), (40, 24.855), (40, 25)))
        self.add_bezier('sym-e8', (40, 25), ((40, 30.473), (37.276, 36.873), (34, 41)))
        self.add_bezier('sym-e9', (34, 41), ((33.158, 42.064), (32.943, 43.082), (32, 44)))
        self.add_bezier('sym-e10', (25, 11), ((26.246, 12.264), (27.116, 13.409), (28, 15)))
        self.add_bezier('sym-e11', (28, 15), ((29.454, 17.593), (30, 21.025), (30, 24)))
        self.add_bezier('sym-e12', (30, 24), ((30, 26.975), (29.454, 30.407), (28, 33)))
        self.add_bezier('sym-e13', (28, 33), ((27.116, 34.591), (26.246, 35.736), (25, 37)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c2', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13')
