"""Periodic table (science), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8f197bd-aa39-572d-9e90-2dd8a2290991'
SOURCE_PATH = 'icons-json/science/periodic table_b8f197bd-aa39-572d-9e90-2dd8a2290991.json'
AUTHOR = 'json_to_solo'

class PeriodicTableScience(Solo48):
    icon_id = 'periodic-table-science'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('periodic', 'table', 'science')

    def build(self):
        self.add_line('e0', (44, 29), (4, 29))
        self.add_line('e1', (15, 40), (15, 19))
        self.add_line('e2', (15, 19), (4, 19))
        self.add_line('e3', (44, 19), (31, 19))
        self.add_line('e4', (31, 40), (31, 12))
        self.add_line('e5', (33, 10), (43, 10))
        self.add_line('e6', (44, 11), (44, 37))
        self.add_line('e7', (40, 40), (7, 40))
        self.add_line('e8', (4, 36), (4, 12))
        self.add_line('e9', (12, 12), (12, 19))
        self.add_bezier('e10', (31, 12), ((31.482, 10.52), (31.673, 10.54), (33, 10)))
        self.add_bezier('e11', (43, 10), ((43.2, 10.16), (43.518, 10.29), (43.709, 10.46)), ((43.882, 10.6), (43.855, 10.83), (44, 11)))
        self.add_bezier('e12', (44, 37), ((44, 37.15), (44, 37.31), (44, 37.46)), ((44, 38.73), (42.736, 39.99), (41.6, 39.99)), ((41.527, 39.99), (41.464, 39.99), (41.391, 39.99)), ((41.255, 39.99), (41.118, 39.99), (40.973, 40)), ((40.909, 40), (40.836, 40), (40.773, 40)), ((40.636, 40), (40.136, 40), (40, 40)))
        self.add_bezier('e13', (7, 40), ((6.909, 40), (6.545, 39.99), (6.455, 39.99)), ((5.009, 39.99), (4.009, 38.08), (4.009, 36.68)), ((4.009, 36.45), (4, 36.23), (4, 36)))
        self.add_bezier('e14', (4, 12), ((4, 11.79), (4.018, 11.58), (4.018, 11.37)), ((4.018, 9.85), (5.609, 8.02), (7.018, 8.02)), ((7.136, 8.01), (7.255, 8.01), (7.373, 8)), ((7.375, 8), (7.377, 8), (7.38, 8)), ((7.522, 8), (7.657, 8.01), (7.791, 8.01)), ((9.764, 8.01), (12, 9.6), (12, 12)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e10', 'e5', 'e11', 'e6', 'e12', 'e7', 'e13', 'e8', 'e14', 'e9')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c1')
