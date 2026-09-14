"""Bandaid (health), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d6f2522-2f4b-4001-af2d-ea58f858d927'
SOURCE_PATH = 'icons-json/health/bandaid_1d6f2522-2f4b-4001-af2d-ea58f858d927.json'
AUTHOR = 'json_to_solo'

class BandaidHealth(Solo48):
    icon_id = 'bandaid-health'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('bandaid', 'health')

    def build(self):
        self.add_line('e0', (13, 24), (24, 35))
        self.add_line('e1', (13, 24), (8, 30))
        self.add_line('e2', (18, 40), (24, 35))
        self.add_line('e3', (13, 24), (24, 13))
        self.add_line('e4', (13, 24), (8, 18))
        self.add_line('e5', (18, 8), (24, 13))
        self.add_line('e6', (24, 35), (30, 40))
        self.add_line('e7', (40, 30), (35, 24))
        self.add_line('e8', (24, 35), (35, 24))
        self.add_line('e9', (35, 24), (24, 13))
        self.add_line('e10', (35, 24), (40, 18))
        self.add_line('e11', (30, 8), (24, 13))
        self.add_bezier('e12', (8, 30), ((6.994, 31.006), (6.008, 32.632), (6.008, 34.023)), ((6.008, 34.184), (6, 34.337), (6, 34.498)), ((6, 34.5), (6, 34.503), (6, 34.505)), ((6, 34.636), (6.016, 34.767), (6.016, 34.898)), ((6.016, 38.531), (9.355, 41.984), (13.004, 41.984)), ((13.192, 41.984), (13.388, 42), (13.576, 42)), ((13.578, 42), (13.579, 42), (13.581, 42)), ((13.669, 42), (13.758, 41.992), (13.846, 41.992)), ((15.344, 41.992), (16.92, 41.08), (18, 40)))
        self.add_bezier('e13', (8, 18), ((6.936, 16.936), (6.016, 15.466), (6.016, 13.985)), ((6.016, 13.797), (6, 13.601), (6, 13.413)), ((6.008, 13.29), (6.008, 13.167), (6.016, 13.045)), ((6.016, 9.183), (9.535, 6.008), (13.298, 6.008)), ((13.467, 6.008), (13.636, 6), (13.806, 6)), ((13.808, 6), (13.811, 6), (13.814, 6)), ((13.945, 6), (14.075, 6.008), (14.206, 6.008)), ((15.704, 6.008), (16.936, 6.936), (18, 8)))
        self.add_bezier('e14', (30, 40), ((30.925, 40.925), (32.419, 41.984), (33.712, 41.984)), ((33.802, 41.984), (33.9, 42), (33.99, 42)), ((34.178, 42), (34.366, 41.984), (34.555, 41.984)), ((38.375, 41.984), (41.984, 38.49), (41.984, 34.661)), ((41.984, 34.522), (42, 34.383), (42, 34.244)), ((42, 34.105), (41.984, 33.974), (41.984, 33.835)), ((41.984, 32.427), (41.006, 31.006), (40, 30)))
        self.add_bezier('e15', (40, 18), ((41.015, 16.985), (41.984, 15.344), (41.984, 13.936)), ((41.984, 13.773), (42, 13.617), (42, 13.462)), ((42, 13.459), (42, 13.457), (42, 13.454)), ((42, 13.293), (41.992, 13.124), (41.992, 12.963)), ((41.992, 9.265), (38.506, 6.016), (34.874, 6.016)), ((34.743, 6.016), (34.62, 6), (34.489, 6)), ((34.342, 6), (34.195, 6.008), (34.055, 6.008)), ((32.607, 6.008), (31.039, 6.961), (30, 8)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e12', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e13', 'e5')
        self.add_contour('c4', 'e6', 'e14', 'e7')
        self.add_contour('c5', 'e8')
        self.add_contour('c6', 'e9')
        self.add_contour('c7', 'e10', 'e15', 'e11')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c6', 'c7')
