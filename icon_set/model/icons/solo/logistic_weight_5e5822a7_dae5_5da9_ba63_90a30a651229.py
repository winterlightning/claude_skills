"""Logistic weight (shipping), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5e5822a7-dae5-5da9-ba63-90a30a651229'
SOURCE_PATH = 'pictographic-primitives/shipping/logistic weight_5e5822a7-dae5-5da9-ba63-90a30a651229.svg'
AUTHOR = 'gpt-6'

class LogisticWeight(Solo48):
    icon_id = 'logistic-weight'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('logistic', 'weight', 'shipping')

    def build(self):
        self.add_arc('sym-e0', (28, 14), (29, 11), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('sym-e1', (29, 11), (26, 6), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e2', (26, 6), (25, 6))
        self.add_arc('sym-e3', (25, 6), (24, 6), radius_x=52, radius_y=52, large_arc=False, sweep=True)
        self.add_line('sym-e8', (24, 6), (22, 6))
        self.add_arc('sym-e10', (22, 6), (19, 11), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('sym-e11', (19, 11), (20, 14), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_line('sym-e12', (20, 14), (34, 14))
        self.add_arc('sym-e15', (34, 14), (37, 17), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e16', (37, 17), (42, 39))
        self.add_line('sym-e17', (42, 39), (42, 40))
        self.add_line('sym-e18', (42, 40), (40, 42))
        self.add_line('sym-e19', (40, 42), (8, 42))
        self.add_line('sym-e21', (8, 42), (6, 40))
        self.add_line('sym-e22', (6, 40), (6, 39))
        self.add_line('sym-e23', (6, 39), (11, 17))
        self.add_arc('sym-e24', (11, 17), (14, 14), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e25', (14, 14), (20, 14))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=False)
