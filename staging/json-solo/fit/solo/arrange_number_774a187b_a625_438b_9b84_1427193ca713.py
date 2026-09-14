"""Arrange number (_uncategorized_04), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '774a187b-a625-438b-9b84-1427193ca713'
SOURCE_PATH = 'icons-json/_uncategorized_04/arrange number_774a187b-a625-438b-9b84-1427193ca713.json'
AUTHOR = 'json_to_solo'

class ArrangeNumberUncategorized04(Solo48):
    icon_id = 'arrange-number-uncategorized-04'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_04'
    aliases = ()
    keywords = ('arrange', 'number', '_uncategorized_04')

    def build(self):
        self.add_line('e0', (32, 7), (36, 4))
        self.add_line('e1', (36, 4), (36, 19))
        self.add_line('e2', (32, 19), (36, 19))
        self.add_line('e3', (39, 19), (36, 19))
        self.add_line('e4', (13, 9), (13, 34))
        self.add_line('e5', (8, 29), (13, 34))
        self.add_line('e6', (19, 29), (13, 34))
        self.add_line('e7', (40, 35), (38, 37))
        self.add_line('e8-1', (32, 43), (34, 44))
        self.add_arc('e8-2', (34, 44), (40, 38), radius_x=6, sweep=False)
        self.add_arc('e8-3', (40, 38), (40, 35), radius_x=50)
        self.add_arc('e9-1', (38, 37), (31, 33), radius_x=5)
        self.add_arc('e9-2', (31, 33), (35, 28), radius_x=5)
        self.add_arc('e9-3', (35, 28), (40, 32), radius_x=5)
        self.add_arc('e9-4', (40, 32), (40, 35), radius_x=35, sweep=False)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6')
        self.add_contour('c6', 'e8-1', 'e8-2', 'e8-3')
        self.add_contour('c7', 'e7', 'e9-1', 'e9-2', 'e9-3', 'e9-4', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c6', 'c7')
