"""A (text) (other), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '37012d29-357d-4e7a-9788-4fe102b86097'
SOURCE_PATH = 'icons-json/other/a (text)_37012d29-357d-4e7a-9788-4fe102b86097.json'
AUTHOR = 'json_to_solo'

class ATextOther(Solo48):
    icon_id = 'a-text-other'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('a', 'text', 'other')

    def build(self):
        self.add_line('sym-e0', (13, 30), (35, 30))
        self.add_bezier('sym-e1', (24, 4), ((23.99, 4), (24.01, 4), (24, 4)))
        self.add_bezier('sym-e2', (24, 4), ((23.98, 4), (24.02, 4), (24, 4)))
        self.add_bezier('sym-e3', (24, 4), ((23.8, 4), (23.21, 4), (23, 4)))
        self.add_bezier('sym-e4', (23, 4), ((21.93, 4), (21.29, 5.136), (21, 6)))
        self.add_line('sym-e5', (21, 6), (8, 44))
        self.add_bezier('sym-e6', (24, 4), ((24.01, 4), (23.99, 4), (24, 4)))
        self.add_bezier('sym-e7', (24, 4), ((24.02, 4), (23.98, 4), (24, 4)))
        self.add_bezier('sym-e8', (24, 4), ((24.2, 4), (24.79, 4), (25, 4)))
        self.add_bezier('sym-e9', (25, 4), ((26.07, 4), (26.71, 5.136), (27, 6)))
        self.add_line('sym-e10', (27, 6), (40, 44))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c2', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
