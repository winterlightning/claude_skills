"""Legal scale 1 (office), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fdd3c820-b393-4768-9d70-ae254dcf010e'
SOURCE_PATH = 'icons-json/office/legal scale 1_fdd3c820-b393-4768-9d70-ae254dcf010e.json'
AUTHOR = 'json_to_solo'

class LegalScale1Office(Solo48):
    icon_id = 'legal-scale-1-office'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('legal', 'scale', 'office')

    def build(self):
        self.add_arc('sym-e0', (21, 11), (27, 11), radius_x=3)
        self.add_arc('sym-e1', (27, 11), (24, 13), radius_x=3)
        self.add_arc('sym-e2', (24, 13), (21, 11), radius_x=3)
        self.add_line('sym-e3', (24, 40), (24, 13))
        self.add_line('sym-e4', (7, 10), (21, 10))
        self.add_line('sym-e5', (18, 40), (24, 40))
        self.add_line('sym-e6', (24, 40), (30, 40))
        self.add_line('sym-e7', (4, 24), (17, 24))
        self.add_line('sym-e8', (17, 24), (17, 25))
        self.add_arc('sym-e9', (17, 25), (12, 30), radius_x=6)
        self.add_arc('sym-e10', (12, 30), (4, 27), radius_x=7)
        self.add_line('sym-e11', (4, 27), (4, 25))
        self.add_line('sym-e12', (4, 25), (4, 24))
        self.add_line('sym-e13', (4, 24), (10, 11))
        self.add_line('sym-e14', (10, 11), (17, 24))
        self.add_line('sym-e15', (41, 10), (27, 10))
        self.add_line('sym-e16', (44, 24), (31, 24))
        self.add_line('sym-e17', (31, 24), (31, 25))
        self.add_arc('sym-e18', (31, 25), (36, 30), radius_x=6, sweep=False)
        self.add_arc('sym-e19', (36, 30), (43, 27), radius_x=6, sweep=False)
        self.add_line('sym-e20', (43, 27), (44, 25))
        self.add_line('sym-e21', (44, 25), (44, 24))
        self.add_line('sym-e22', (44, 24), (38, 11))
        self.add_line('sym-e23', (38, 11), (31, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', closed=True)
        self.add_contour('sym-c1', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c4', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
        self.add_contour('sym-c5', 'sym-e15')
        self.add_contour('sym-c6', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
