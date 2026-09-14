"""Affinity publisher logo (_uncategorized_01), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca67be63-3b5a-4b74-800b-f1df0601b64c'
SOURCE_PATH = 'icons-json/_uncategorized_01/affinity publisher logo_ca67be63-3b5a-4b74-800b-f1df0601b64c.json'
AUTHOR = 'json_to_solo'

class AffinityPublisherLogoUncategorized01(Solo48):
    icon_id = 'affinity-publisher-logo-uncategorized-01'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('affinity', 'publisher', 'logo', '_uncategorized_01')

    def build(self):
        self.add_line('e0', (18, 8), (14, 17))
        self.add_line('e1', (18, 8), (37, 42))
        self.add_line('e2', (18, 8), (20, 6))
        self.add_line('e3', (20, 6), (27, 6))
        self.add_line('e4', (28, 42), (14, 17))
        self.add_line('e5', (28, 42), (19, 42))
        self.add_line('e6', (28, 42), (37, 42))
        self.add_line('e7', (37, 42), (40, 42))
        self.add_line('e8', (42, 40), (42, 35))
        self.add_line('e9', (27, 6), (42, 35))
        self.add_line('e10', (27, 6), (40, 6))
        self.add_line('e11', (42, 8), (42, 35))
        self.add_line('e12', (10, 25), (19, 42))
        self.add_line('e13', (10, 25), (7, 31))
        self.add_line('e14', (6, 33), (6, 40))
        self.add_line('e15', (8, 42), (19, 42))
        self.add_line('e16', (10, 25), (14, 17))
        self.add_bezier('e17', (40, 42), ((40.614, 41.746), (41.673, 41.493), (41.926, 40.773)), ((41.943, 40.724), (41.984, 40.049), (42, 40)))
        self.add_bezier('e18', (40, 6), ((41.17, 6.45), (41.566, 6.895), (42, 8)))
        self.add_bezier('e19', (7, 31), ((6.73, 31.278), (6.27, 31.92), (6, 32.198)), ((6, 32.468), (6, 32.73), (6, 33)))
        self.add_bezier('e20', (6, 40), ((6.057, 40.131), (6.033, 40.65), (6.098, 40.781)), ((6.27, 41.157), (6.802, 41.755), (7.203, 41.902)), ((7.685, 42), (7.509, 41.755), (8, 42)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6')
        self.add_contour('c6', 'e7', 'e17', 'e8')
        self.add_contour('c7', 'e9')
        self.add_contour('c8', 'e10', 'e18', 'e11')
        self.add_contour('c9', 'e12')
        self.add_contour('c10', 'e13', 'e19', 'e14', 'e20', 'e15')
        self.add_contour('c11', 'e16')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c11')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c11', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c2', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c10', 'c4')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c4', 'c9')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c11', 'c9')
