"""Information desk man (wayfinding), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c255cd70-d42e-428e-90f6-fea19ecba7bb'
SOURCE_PATH = 'icons-json/wayfinding/information desk man_c255cd70-d42e-428e-90f6-fea19ecba7bb.json'
AUTHOR = 'json_to_solo'

class InformationDeskManWayfinding(Solo48):
    icon_id = 'information-desk-man-wayfinding'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('information', 'desk', 'man', 'wayfinding')

    def build(self):
        self.add_arc('sym-e0', (18, 12), (30, 12), radius_x=6)
        self.add_arc('sym-e1', (30, 12), (18, 12), radius_x=6)
        self.add_line('sym-e2', (13, 27), (35, 27))
        self.add_line('sym-e3', (35, 27), (41, 27))
        self.add_bezier('sym-e4', (41, 27), ((41.254, 27.164), (41.836, 27.714), (42, 28)))
        self.add_bezier('sym-e5', (42, 28), ((42, 28.123), (41.959, 27.885), (42, 28)))
        self.add_line('sym-e6', (42, 28), (42, 35))
        self.add_bezier('sym-e7', (42, 35), ((41.935, 35.155), (42, 34.845), (42, 35)))
        self.add_bezier('sym-e8', (42, 35), ((41.473, 36.074), (40.024, 36), (39, 36)))
        self.add_bezier('sym-e9', (39, 36), ((38.815, 36), (39.182, 36), (39, 36)))
        self.add_line('sym-e10', (39, 36), (9, 36))
        self.add_line('sym-e11', (9, 36), (9, 42))
        self.add_line('sym-e12', (13, 27), (7, 27))
        self.add_bezier('sym-e13', (7, 27), ((6.746, 27.164), (6.164, 27.714), (6, 28)))
        self.add_bezier('sym-e14', (6, 28), ((6, 28.123), (6.041, 27.885), (6, 28)))
        self.add_line('sym-e15', (6, 28), (6, 35))
        self.add_bezier('sym-e16', (6, 35), ((6.065, 35.155), (6, 34.845), (6, 35)))
        self.add_bezier('sym-e17', (6, 35), ((6.527, 36.074), (7.976, 36), (9, 36)))
        self.add_bezier('sym-e18', (9, 36), ((9.185, 36), (8.818, 36), (9, 36)))
        self.add_bezier('sym-e19', (13, 27), ((13.221, 24.185), (14.382, 21.366), (17, 20)))
        self.add_bezier('sym-e20', (17, 20), ((17.466, 19.755), (18.452, 20), (19, 20)))
        self.add_line('sym-e21', (19, 20), (24, 20))
        self.add_line('sym-e22', (24, 20), (29, 20))
        self.add_bezier('sym-e23', (29, 20), ((29.548, 20), (30.534, 19.755), (31, 20)))
        self.add_bezier('sym-e24', (31, 20), ((33.618, 21.366), (34.779, 24.185), (35, 27)))
        self.add_line('sym-e25', (39, 42), (39, 36))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c2', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
        self.add_contour('sym-c3', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24')
        self.add_contour('sym-c4', 'sym-e25')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
