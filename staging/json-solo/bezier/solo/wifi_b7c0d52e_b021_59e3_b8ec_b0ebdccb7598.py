"""Wifi (networks), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7c0d52e-b021-59e3-b8ec-b0ebdccb7598'
SOURCE_PATH = 'icons-json/networks/wifi_b7c0d52e-b021-59e3-b8ec-b0ebdccb7598.json'
AUTHOR = 'json_to_solo'

class WifiB7c0d52e(Solo48):
    icon_id = 'wifi-b7c0d52e'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('wifi', 'networks')

    def build(self):
        self.add_line('sym-e0', (24, 40), (24, 40))
        self.add_bezier('sym-e1', (4, 16), ((4.164, 15.85), (4, 16.14), (4, 16)))
        self.add_bezier('sym-e2', (4, 16), ((5.9, 14.57), (7.909, 13.11), (10, 12)))
        self.add_bezier('sym-e3', (10, 12), ((13.936, 9.91), (18.6, 8), (23, 8)))
        self.add_bezier('sym-e4', (23, 8), ((23.27, 8), (23.73, 8), (24, 8)))
        self.add_bezier('sym-e5', (24, 8), ((24.27, 8), (24.73, 8), (25, 8)))
        self.add_bezier('sym-e6', (25, 8), ((29.4, 8), (34.064, 9.91), (38, 12)))
        self.add_bezier('sym-e7', (38, 12), ((40.091, 13.11), (42.1, 14.57), (44, 16)))
        self.add_bezier('sym-e8', (44, 16), ((44, 16.14), (43.836, 15.85), (44, 16)))
        self.add_bezier('sym-e9', (10, 23), ((14.326, 19.132), (19.343, 17), (24, 17)))
        self.add_bezier('sym-e10', (24, 17), ((28.657, 17), (33.674, 19.132), (38, 23)))
        self.add_bezier('sym-e11', (17, 30), ((19.228, 28.208), (21.463, 27.232), (24, 27)))
        self.add_bezier('sym-e12', (24, 27), ((26.537, 27.232), (28.772, 28.208), (31, 30)))
        self.add_contour('sym-c0', 'sym-e0', closed=True)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8')
        self.add_contour('sym-c2', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c3', 'sym-e11', 'sym-e12')
