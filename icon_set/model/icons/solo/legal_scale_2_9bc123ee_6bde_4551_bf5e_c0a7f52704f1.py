"""Legal scale 2 (office), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9bc123ee-6bde-4551-bf5e-c0a7f52704f1'
SOURCE_PATH = 'icons-json/office/legal scale 2_9bc123ee-6bde-4551-bf5e-c0a7f52704f1.json'
AUTHOR = 'json_to_solo'

class LegalScale2(Solo48):
    icon_id = 'legal-scale-2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('legal', 'scale', 'office')

    def build(self):
        self.add_line('sym-e0', (24, 8), (24, 12))
        self.add_line('sym-e1', (24, 12), (24, 17))
        self.add_line('sym-e2', (7, 12), (11, 12))
        self.add_line('sym-e3', (11, 12), (24, 12))
        self.add_line('sym-e4', (24, 12), (37, 12))
        self.add_line('sym-e5', (37, 12), (41, 12))
        self.add_line('sym-e6', (18, 32), (11, 12))
        self.add_line('sym-e7', (11, 12), (5, 32))
        self.add_line('sym-e8', (5, 32), (18, 32))
        self.add_line('sym-e9', (18, 32), (19, 32))
        self.add_line('sym-e10', (19, 32), (19, 34))
        self.add_arc('sym-e11', (19, 34), (12, 40), radius_x=9)
        self.add_arc('sym-e12', (12, 40), (11, 40), radius_x=1, sweep=False)
        self.add_arc('sym-e14', (11, 40), (4, 34), radius_x=8)
        self.add_line('sym-e15', (4, 34), (4, 33))
        self.add_line('sym-e17', (4, 33), (4, 32))
        self.add_arc('sym-e18', (4, 32), (5, 32), radius_x=13, sweep=False)
        self.add_line('sym-e19', (30, 32), (37, 12))
        self.add_line('sym-e20', (37, 12), (43, 32))
        self.add_line('sym-e21', (43, 32), (30, 32))
        self.add_line('sym-e22', (30, 32), (29, 32))
        self.add_line('sym-e23', (29, 32), (29, 34))
        self.add_arc('sym-e24', (29, 34), (36, 40), radius_x=9, sweep=False)
        self.add_line('sym-e25', (36, 40), (37, 40))
        self.add_arc('sym-e27', (37, 40), (44, 34), radius_x=8, sweep=False)
        self.add_arc('sym-e28', (44, 34), (44, 33), radius_x=34)
        self.add_arc('sym-e30', (44, 33), (44, 32), radius_x=34)
        self.add_arc('sym-e31', (44, 32), (43, 32), radius_x=13)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c2', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e15', 'sym-e17', 'sym-e18')
        self.add_contour('sym-c3', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e27', 'sym-e28', 'sym-e30', 'sym-e31')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
