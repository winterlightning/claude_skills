"""Focus cross (photography), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3523a4ef-eb15-4b00-a241-c59dc2e09efa'
SOURCE_PATH = 'icons-json/photography/focus cross_3523a4ef-eb15-4b00-a241-c59dc2e09efa.json'
AUTHOR = 'json_to_solo'

class FocusCross(Solo48):
    icon_id = 'focus-cross'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('focus', 'cross', 'photography')

    def build(self):
        self.add_line('sym-e0', (33, 24), (24, 24))
        self.add_line('sym-e1', (24, 24), (15, 24))
        self.add_line('sym-e2', (24, 34), (24, 24))
        self.add_line('sym-e3', (24, 24), (24, 14))
        self.add_line('sym-e4', (35, 42), (40, 42))
        self.add_arc('sym-e5', (40, 42), (42, 40), radius_x=2, sweep=False)
        self.add_line('sym-e6', (42, 40), (42, 35))
        self.add_line('sym-e7', (13, 42), (8, 42))
        self.add_arc('sym-e8', (8, 42), (6, 40), radius_x=2)
        self.add_line('sym-e9', (6, 40), (6, 35))
        self.add_line('sym-e10', (35, 6), (40, 6))
        self.add_arc('sym-e11', (40, 6), (42, 8), radius_x=2)
        self.add_line('sym-e12', (42, 8), (42, 13))
        self.add_line('sym-e13', (13, 6), (8, 6))
        self.add_arc('sym-e14', (8, 6), (6, 8), radius_x=2, sweep=False)
        self.add_line('sym-e15', (6, 8), (6, 13))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c4', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c5', 'sym-e13', 'sym-e14', 'sym-e15')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
