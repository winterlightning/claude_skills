"""Dryer hair (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '34e94fc5-ce90-4627-9cd4-0ded39755e20'
SOURCE_PATH = 'icons-json/symbol/dryer hair_34e94fc5-ce90-4627-9cd4-0ded39755e20.json'
AUTHOR = 'json_to_solo'

class DryerHairSymbol(Solo48):
    icon_id = 'dryer-hair-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('dryer', 'hair', 'symbol')

    def build(self):
        self.add_line('e0', (31, 39), (37, 26))
        self.add_line('e1', (37, 26), (40, 24))
        self.add_line('e2', (29, 6), (6, 9))
        self.add_line('e3', (6, 9), (6, 22))
        self.add_line('e4', (6, 22), (26, 25))
        self.add_line('e5', (26, 28), (22, 40))
        self.add_bezier('e6', (22, 40), ((23.186, 40.548), (24.319, 41.992), (25.653, 41.992)), ((25.717, 42), (25.79, 42), (25.854, 42)), ((25.855, 42), (25.856, 42), (25.857, 42)), ((25.931, 42), (25.996, 42), (26.062, 41.992)), ((27.854, 41.992), (30.231, 40.645), (31, 39)))
        self.add_bezier('e7', (40, 24), ((41.325, 22.675), (41.984, 18.715), (41.984, 16.882)), ((41.984, 16.677), (42, 16.465), (42, 16.26)), ((42, 16.257), (42, 16.254), (42, 16.25)), ((42, 16.049), (41.984, 15.848), (41.984, 15.646)), ((41.984, 14.845), (41.755, 14.075), (41.525, 13.315)), ((40.315, 9.224), (36.51, 6.016), (32.125, 6.016)), ((31.969, 6.016), (31.814, 6), (31.658, 6)), ((30.742, 6), (29.916, 6), (29, 6)))
        self.add_bezier('e8', (26, 25), ((26.025, 25.835), (26.27, 27.19), (26, 28)))
        self.add_contour('c0', 'e6', 'e0', 'e1', 'e7', 'e2', 'e3', 'e4', 'e8', 'e5', closed=True)
