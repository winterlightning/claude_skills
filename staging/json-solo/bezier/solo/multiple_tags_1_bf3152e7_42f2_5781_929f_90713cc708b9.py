"""Multiple tags 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf3152e7-42f2-5781-929f-90713cc708b9'
SOURCE_PATH = 'icons-json/interface-essential/multiple tags 1_bf3152e7-42f2-5781-929f-90713cc708b9.json'
AUTHOR = 'json_to_solo'

class MultipleTags1InterfaceEssential(Solo48):
    icon_id = 'multiple-tags-1-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('multiple', 'tags', 'interface-essential')

    def build(self):
        self.add_line('e0', (42, 18), (38, 40))
        self.add_line('e1', (34, 42), (22, 40))
        self.add_line('e2', (35, 6), (26, 6))
        self.add_line('e3', (22, 8), (8, 24))
        self.add_line('e4', (8, 29), (17, 40))
        self.add_line('e5', (22, 40), (37, 23))
        self.add_line('e6', (39, 18), (39, 8))
        self.add_arc('e7-top', (27, 16), (31, 16), radius_x=2)
        self.add_arc('e7-bottom', (31, 16), (27, 16), radius_x=2)
        self.add_bezier('e8', (39, 13), ((39.851, 14.047), (41.992, 15.712), (41.992, 17.193)), ((41.992, 17.422), (42, 17.651), (42, 17.88)), ((42, 18.011), (42, 17.869), (42, 18)))
        self.add_bezier('e9', (38, 40), ((37.804, 41.031), (36.78, 42), (35.577, 42)), ((34.988, 42), (34.589, 42), (34, 42)))
        self.add_bezier('e10', (39, 8), ((39, 7.035), (38.007, 6), (36.862, 6)), ((36.813, 6), (36.764, 6), (36.715, 6)), ((36.289, 6), (35.417, 6), (35, 6)))
        self.add_bezier('e11', (26, 6), ((24.355, 6), (22.974, 6.969), (22, 8)))
        self.add_bezier('e12', (8, 24), ((7.427, 24.605), (6.008, 25.44), (6.008, 26.373)), ((6.008, 26.421), (6, 26.469), (6, 26.526)), ((6, 26.526), (6, 26.527), (6, 26.528)), ((6, 26.577), (6.008, 26.626), (6.008, 26.675)), ((6.008, 27.584), (7.46, 28.411), (8, 29)))
        self.add_bezier('e13', (17, 40), ((18.113, 41.203), (20.863, 41.195), (22, 40)))
        self.add_bezier('e14', (37, 23), ((38.661, 21.257), (39, 20.25), (39, 18)))
        self.add_contour('c0', 'e8', 'e0', 'e9', 'e1')
        self.add_contour('c1', 'e10', 'e2', 'e11', 'e3', 'e12', 'e4', 'e13', 'e5', 'e14', 'e6', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
