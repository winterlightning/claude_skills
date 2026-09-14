"""Fall down large head (diagrams), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab7112f8-4c6c-4ed5-83c2-c31699018e31'
SOURCE_PATH = 'icons-json/diagrams/fall down large head_ab7112f8-4c6c-4ed5-83c2-c31699018e31.json'
AUTHOR = 'json_to_solo'

class FallDownLargeHead(Solo48):
    icon_id = 'fall-down-large-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('fall', 'down', 'large', 'head', 'diagrams')

    def build(self):
        self.add_line('sym-e0', (24, 20), (24, 40))
        self.add_line('sym-e1', (24, 40), (32, 33))
        self.add_line('sym-e2', (44, 8), (44, 17))
        self.add_arc('sym-e3', (44, 17), (41, 20), radius_x=3)
        self.add_line('sym-e4', (41, 20), (24, 20))
        self.add_line('sym-e5', (24, 20), (7, 20))
        self.add_arc('sym-e6', (7, 20), (4, 17), radius_x=3)
        self.add_line('sym-e7', (4, 17), (4, 8))
        self.add_line('sym-e8', (16, 33), (24, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c2', 'sym-e8')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
