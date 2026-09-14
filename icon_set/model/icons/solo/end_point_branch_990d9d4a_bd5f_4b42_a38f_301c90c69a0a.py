"""End point branch (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '990d9d4a-bd5f-4b42-a38f-301c90c69a0a'
SOURCE_PATH = 'icons-json/arrows/end point branch_990d9d4a-bd5f-4b42-a38f-301c90c69a0a.json'
AUTHOR = 'json_to_solo'

class EndPointBranch(Solo48):
    icon_id = 'end-point-branch'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('end', 'point', 'branch', 'arrows')

    def build(self):
        self.add_line('sym-e0', (4, 24), (15, 24))
        self.add_line('sym-e1', (15, 24), (25, 24))
        self.add_line('sym-e2', (25, 24), (36, 24))
        self.add_line('sym-e3', (36, 24), (44, 40))
        self.add_line('sym-e4', (23, 40), (15, 24))
        self.add_line('sym-e5', (15, 24), (23, 8))
        self.add_line('sym-e6', (33, 40), (25, 24))
        self.add_line('sym-e7', (25, 24), (33, 8))
        self.add_line('sym-e8', (44, 8), (36, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c2', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c3', 'sym-e8')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
