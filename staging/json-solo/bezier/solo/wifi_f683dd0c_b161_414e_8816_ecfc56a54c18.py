"""Wifi (networks), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f683dd0c-b161-414e-8816-ecfc56a54c18'
SOURCE_PATH = 'icons-json/networks/wifi_f683dd0c-b161-414e-8816-ecfc56a54c18.json'
AUTHOR = 'json_to_solo'

class Wifi(Solo48):
    icon_id = 'wifi'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('wifi', 'networks')

    def build(self):
        self.add_line('sym-e0', (24, 40), (24, 40))
        self.add_bezier('sym-e1', (4, 17), ((4.082, 16.87), (4, 17.13), (4, 17)))
        self.add_bezier('sym-e2', (4, 17), ((4.236, 16.78), (4.755, 16.21), (5, 16)))
        self.add_bezier('sym-e3', (5, 16), ((6.609, 14.59), (8.227, 13.16), (10, 12)))
        self.add_bezier('sym-e4', (10, 12), ((13.718, 9.58), (18.645, 8), (23, 8)))
        self.add_bezier('sym-e5', (23, 8), ((23.209, 8), (22.791, 8), (23, 8)))
        self.add_bezier('sym-e6', (23, 8), ((23.144, 8), (23.854, 8), (24, 8)))
        self.add_bezier('sym-e7', (24, 8), ((24.073, 8), (23.927, 8), (24, 8)))
        self.add_bezier('sym-e8', (24, 8), ((24.073, 8), (23.927, 8), (24, 8)))
        self.add_bezier('sym-e9', (24, 8), ((24.146, 8), (24.856, 8), (25, 8)))
        self.add_bezier('sym-e10', (25, 8), ((25.209, 8), (24.791, 8), (25, 8)))
        self.add_bezier('sym-e11', (25, 8), ((29.355, 8), (34.282, 9.58), (38, 12)))
        self.add_bezier('sym-e12', (38, 12), ((39.773, 13.16), (41.391, 14.59), (43, 16)))
        self.add_bezier('sym-e13', (43, 16), ((43.245, 16.21), (43.764, 16.78), (44, 17)))
        self.add_bezier('sym-e14', (44, 17), ((44, 17.13), (43.918, 16.87), (44, 17)))
        self.add_bezier('sym-e15', (14, 27), ((15.518, 25.68), (17.145, 24.67), (19, 24)))
        self.add_bezier('sym-e16', (19, 24), ((20.601, 23.423), (22.27, 23.014), (24, 23)))
        self.add_bezier('sym-e17', (24, 23), ((25.73, 23.014), (27.399, 23.423), (29, 24)))
        self.add_bezier('sym-e18', (29, 24), ((30.855, 24.67), (32.482, 25.68), (34, 27)))
        self.add_contour('sym-c0', 'sym-e0', closed=True)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
        self.add_contour('sym-c2', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
