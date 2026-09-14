"""Filter (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6d2a0d3-a38b-5d2d-bf20-5a42fdc874a0'
SOURCE_PATH = 'icons-json/interface-essential/filter_a6d2a0d3-a38b-5d2d-bf20-5a42fdc874a0.json'
AUTHOR = 'json_to_solo'

class FilterInterfaceEssential(Solo48):
    icon_id = 'filter-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('filter', 'interface-essential')

    def build(self):
        self.add_line('e0', (20, 42), (28, 34))
        self.add_line('e1', (28, 34), (28, 25))
        self.add_line('e2', (28, 25), (41, 9))
        self.add_line('e3', (39, 6), (8, 6))
        self.add_line('e4', (6, 8), (20, 25))
        self.add_line('e5', (20, 25), (20, 42))
        self.add_bezier('e6', (41, 9), ((41.344, 8.591), (41.992, 8.315), (41.992, 7.743)), ((41.992, 7.694), (42, 7.638), (42, 7.582)), ((42, 7.581), (42, 7.58), (42, 7.579)), ((41.992, 7.481), (41.992, 7.375), (41.984, 7.276)), ((41.984, 6.556), (40.985, 6.016), (40.372, 6.016)), ((40.2, 6.016), (40.036, 6), (39.865, 6)), ((39.488, 6), (39.376, 6), (39, 6)))
        self.add_bezier('e7', (8, 6), ((6.601, 6), (6, 6.573), (6, 8.054)), ((6, 8.185), (6, 7.869), (6, 8)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e6', 'e3', 'e7', 'e4', 'e5', closed=True)
