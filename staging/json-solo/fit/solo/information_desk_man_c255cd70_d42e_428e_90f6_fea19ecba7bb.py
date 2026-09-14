"""Information desk man (wayfinding), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
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
        self.add_line('sym-e4', (41, 27), (42, 28))
        self.add_line('sym-e6', (42, 28), (42, 35))
        self.add_arc('sym-e8', (42, 35), (39, 36), radius_x=2)
        self.add_line('sym-e10', (39, 36), (9, 36))
        self.add_line('sym-e11', (9, 36), (9, 42))
        self.add_line('sym-e12', (13, 27), (7, 27))
        self.add_line('sym-e13', (7, 27), (6, 28))
        self.add_line('sym-e15', (6, 28), (6, 35))
        self.add_arc('sym-e17', (6, 35), (9, 36), radius_x=2, sweep=False)
        self.add_line('sym-e19', (13, 27), (17, 20))
        self.add_line('sym-e20', (17, 20), (19, 20))
        self.add_line('sym-e21', (19, 20), (24, 20))
        self.add_line('sym-e22', (24, 20), (29, 20))
        self.add_line('sym-e23', (29, 20), (31, 20))
        self.add_line('sym-e24', (31, 20), (35, 27))
        self.add_line('sym-e25', (39, 42), (39, 36))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e8', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c2', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e17')
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
