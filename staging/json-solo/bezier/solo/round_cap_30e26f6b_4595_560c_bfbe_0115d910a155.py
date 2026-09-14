"""Round cap (construction), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e3', (4, 24), ((4, 24.057), (4, 23.944), (4, 24)))
        self.add_bezier('sym-e4', (4, 24), ((4, 30.92), (7.882, 37.19), (14, 39)))
        self.add_bezier('sym-e5', (14, 39), ((15.545, 39.46), (17.418, 40), (19, 40)))
        self.add_bezier('sym-e6', (19, 40), ((19.318, 40), (19.682, 40), (20, 40)))
        self.add_line('sym-e7', (20, 40), (44, 40))
        self.add_bezier('sym-e8', (4, 24), ((4, 23.943), (4, 24.056), (4, 24)))
        self.add_bezier('sym-e9', (4, 24), ((4, 17.08), (7.882, 10.81), (14, 9)))
        self.add_bezier('sym-e10', (14, 9), ((15.545, 8.54), (17.418, 8), (19, 8)))
        self.add_bezier('sym-e11', (19, 8), ((19.318, 8), (19.682, 8), (20, 8)))
        self.add_line('sym-e12', (20, 8), (44, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c3', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
