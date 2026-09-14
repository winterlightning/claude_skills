"""Security officer scanner (travel), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ffcd86b-ac47-42cd-b42f-ac704fe62ab1'
SOURCE_PATH = 'icons-json/travel/security officer scanner_6ffcd86b-ac47-42cd-b42f-ac704fe62ab1.json'
AUTHOR = 'json_to_solo'

class SecurityOfficerScanner(Solo48):
    icon_id = 'security-officer-scanner'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('security', 'officer', 'scanner', 'travel')

    def build(self):
        self.add_line('sym-e0', (8, 11), (40, 11))
        self.add_line('sym-e1', (40, 11), (40, 44))
        self.add_line('sym-e2', (8, 44), (8, 11))
        self.add_line('sym-e3', (8, 11), (8, 6))
        self.add_line('sym-e4', (8, 6), (10, 4))
        self.add_line('sym-e5', (10, 4), (24, 4))
        self.add_line('sym-e6', (24, 4), (38, 4))
        self.add_line('sym-e7', (38, 4), (40, 6))
        self.add_line('sym-e8', (40, 6), (40, 11))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
