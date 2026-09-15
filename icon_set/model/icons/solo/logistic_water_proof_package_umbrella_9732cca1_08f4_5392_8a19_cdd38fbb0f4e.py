"""Logistic water proof package umbrella (shipping), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9732cca1-08f4-5392-8a19-cdd38fbb0f4e'
SOURCE_PATH = 'pictographic-primitives/shipping/logistic water proof package umbrella_9732cca1-08f4-5392-8a19-cdd38fbb0f4e.svg'
AUTHOR = 'gpt-6'

class LogisticWaterProofPackageUmbrella(Solo48):
    icon_id = 'logistic-water-proof-package-umbrella'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('logistic', 'water', 'proof', 'package', 'umbrella', 'shipping')

    def build(self):
        self.add_line('e0', (24, 32), (13, 29))
        self.add_line('e1', (13, 29), (24, 25))
        self.add_line('e2', (24, 32), (24, 44))
        self.add_line('e3', (24, 32), (35, 29))
        self.add_line('e4', (35, 29), (24, 25))
        self.add_line('e5', (24, 44), (13, 39))
        self.add_line('e6', (13, 39), (13, 29))
        self.add_line('e7', (24, 44), (35, 39))
        self.add_line('e8', (35, 39), (35, 29))
        self.add_line('e9', (24, 25), (24, 17))
        self.add_line('e10', (24, 4), (24, 6))
        self.add_arc('e11-1', (40, 19), (26, 6), radius_x=15, radius_y=15, large_arc=False, sweep=False)
        self.add_arc('e11-2', (26, 6), (8, 18), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_line('e11-3', (8, 18), (11, 17))
        self.add_arc('e11-4', (11, 17), (18, 18), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('e11-5', (18, 18), (19, 19))
        self.add_arc('e11-6', (19, 19), (26, 17), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('e11-7', (26, 17), (28, 18), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('e11-8', (28, 18), (32, 17), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('e11-9', (32, 17), (40, 19), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('c0', 'e11-1', 'e11-2', 'e11-3', 'e11-4', 'e11-5', 'e11-6', 'e11-7', 'e11-8', 'e11-9', closed=True)
        self.add_contour('c1', 'e0', 'e1', closed=False)
        self.add_contour('c2', 'e2', closed=False)
        self.add_contour('c3', 'e3', 'e4', closed=False)
        self.add_contour('c4', 'e5', 'e6', closed=False)
        self.add_contour('c5', 'e7', 'e8', closed=False)
        self.add_contour('c6', 'e9', closed=False)
        self.add_contour('c7', 'e10', closed=False)
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c6', 'c0')
        self.relate('connect', 'c7', 'c0')
