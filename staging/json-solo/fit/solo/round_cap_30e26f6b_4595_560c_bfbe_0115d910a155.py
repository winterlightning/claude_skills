"""Round cap (construction), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30e26f6b-4595-560c-bfbe-0115d910a155'
SOURCE_PATH = 'icons-json/construction/round cap_30e26f6b-4595-560c-bfbe-0115d910a155.json'
AUTHOR = 'json_to_solo'

class RoundCapConstruction(Solo48):
    icon_id = 'round-cap-construction'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('round', 'cap', 'construction')

    def build(self):
        self.add_arc('sym-e0', (13, 24), (22, 24), radius_x=5)
        self.add_arc('sym-e1', (22, 24), (13, 24), radius_x=5)
        self.add_line('sym-e2', (44, 24), (22, 24))
        self.add_arc('sym-e4-1', (4, 24), (6, 32), radius_x=17, sweep=False)
        self.add_arc('sym-e4-2', (6, 32), (14, 39), radius_x=14, sweep=False)
        self.add_arc('sym-e5', (14, 39), (19, 40), radius_x=18, sweep=False)
        self.add_line('sym-e6', (19, 40), (20, 40))
        self.add_line('sym-e7', (20, 40), (44, 40))
        self.add_arc('sym-e9-1', (4, 24), (6, 16), radius_x=17)
        self.add_arc('sym-e9-2', (6, 16), (14, 9), radius_x=14)
        self.add_arc('sym-e10', (14, 9), (19, 8), radius_x=18)
        self.add_line('sym-e11', (19, 8), (20, 8))
        self.add_line('sym-e12', (20, 8), (44, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e4-1', 'sym-e4-2', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c3', 'sym-e9-1', 'sym-e9-2', 'sym-e10', 'sym-e11', 'sym-e12')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
