"""Oil change (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a50c664f-fe0c-48dc-bf92-8b6a021045a3'
SOURCE_PATH = 'pictographic-primitives/transportation/oil change_a50c664f-fe0c-48dc-bf92-8b6a021045a3.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class OilChange(Solo48):
    icon_id = 'oil-change'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('oil', 'change', 'transportation')

    def build(self):
        self.add_line('sym-e0', (24, 42), (35, 42))
        self.add_line('sym-e1', (35, 42), (39, 40))
        self.add_line('sym-e2', (39, 40), (42, 28))
        self.add_arc('sym-e3', (24, 31), (32, 26), radius_x=10, sweep=False)
        self.add_line('sym-e4', (32, 26), (33, 21))
        self.add_line('sym-e5', (33, 21), (29, 14))
        self.add_line('sym-e6', (29, 14), (24, 6))
        self.add_line('sym-e7', (24, 6), (19, 14))
        self.add_arc('sym-e8', (19, 14), (15, 21), radius_x=21, sweep=False)
        self.add_line('sym-e9', (15, 21), (16, 26))
        self.add_arc('sym-e10', (16, 26), (24, 31), radius_x=10, sweep=False)
        self.add_line('sym-e11', (24, 42), (13, 42))
        self.add_line('sym-e12', (13, 42), (9, 40))
        self.add_line('sym-e13', (9, 40), (6, 28))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', closed=True)
        self.add_contour('sym-c2', 'sym-e11', 'sym-e12', 'sym-e13')
        self.relate('connect', 'sym-c0', 'sym-c2')
