"""Phone merge (phones), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1171bcf4-d88f-401f-86a0-fd93af09bc27'
SOURCE_PATH = 'icons-json/phones/phone merge_1171bcf4-d88f-401f-86a0-fd93af09bc27.json'
AUTHOR = 'json_to_solo'

class PhoneMergePhones(Solo48):
    icon_id = 'phone-merge-phones'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    aliases = ()
    keywords = ('phone', 'merge', 'phones')

    def build(self):
        self.add_line('sym-e0', (24, 4), (24, 29))
        self.add_bezier('sym-e1', (24, 29), ((24.564, 31.045), (25.006, 33.127), (26, 35)))
        self.add_bezier('sym-e2', (26, 35), ((28.333, 39.409), (32.52, 41.591), (37, 43)))
        self.add_bezier('sym-e3', (37, 43), ((38.002, 43.318), (38.947, 44), (40, 44)))
        self.add_bezier('sym-e4', (40, 44), ((40, 44), (39.958, 44), (40, 44)))
        self.add_line('sym-e5', (33, 14), (24, 4))
        self.add_line('sym-e6', (24, 4), (15, 14))
        self.add_bezier('sym-e7', (8, 44), ((8.042, 44), (8, 44), (8, 44)))
        self.add_bezier('sym-e8', (8, 44), ((9.053, 44), (9.998, 43.318), (11, 43)))
        self.add_bezier('sym-e9', (11, 43), ((15.48, 41.591), (19.667, 39.409), (22, 35)))
        self.add_bezier('sym-e10', (22, 35), ((22.994, 33.127), (23.436, 31.045), (24, 29)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c1', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
