"""Oil change (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a50c664f-fe0c-48dc-bf92-8b6a021045a3'
SOURCE_PATH = 'icons-json/transportation/oil change_a50c664f-fe0c-48dc-bf92-8b6a021045a3.json'
AUTHOR = 'json_to_solo'

class OilChangeTransportation(Solo48):
    icon_id = 'oil-change-transportation'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('oil', 'change', 'transportation')

    def build(self):
        self.add_line('sym-e0', (24, 42), (35, 42))
        self.add_bezier('sym-e1', (35, 42), ((36.235, 42), (38.656, 41.186), (39, 40)))
        self.add_line('sym-e2', (39, 40), (42, 28))
        self.add_bezier('sym-e3', (24, 31), ((27.104, 30.969), (30.392, 28.932), (32, 26)))
        self.add_bezier('sym-e4', (32, 26), ((32.769, 24.601), (33.311, 22.571), (33, 21)))
        self.add_bezier('sym-e5', (33, 21), ((32.501, 18.464), (30.301, 16.176), (29, 14)))
        self.add_line('sym-e6', (29, 14), (24, 6))
        self.add_line('sym-e7', (24, 6), (19, 14))
        self.add_bezier('sym-e8', (19, 14), ((17.699, 16.176), (15.499, 18.464), (15, 21)))
        self.add_bezier('sym-e9', (15, 21), ((14.689, 22.571), (15.231, 24.601), (16, 26)))
        self.add_bezier('sym-e10', (16, 26), ((17.608, 28.932), (20.896, 30.969), (24, 31)))
        self.add_line('sym-e11', (24, 42), (13, 42))
        self.add_bezier('sym-e12', (13, 42), ((11.765, 42), (9.344, 41.186), (9, 40)))
        self.add_line('sym-e13', (9, 40), (6, 28))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', closed=True)
        self.add_contour('sym-c2', 'sym-e11', 'sym-e12', 'sym-e13')
        self.relate('connect', 'sym-c0', 'sym-c2')
