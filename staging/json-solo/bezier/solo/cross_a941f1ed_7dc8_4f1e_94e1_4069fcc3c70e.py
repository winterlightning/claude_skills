"""Cross (health), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a941f1ed-7dc8-4f1e-94e1-4069fcc3c70e'
SOURCE_PATH = 'icons-json/health/cross_a941f1ed-7dc8-4f1e-94e1-4069fcc3c70e.json'
AUTHOR = 'json_to_solo'

class Cross(Solo48):
    icon_id = 'cross'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('cross', 'health')

    def build(self):
        self.add_line('e0', (30, 6), (19, 6))
        self.add_line('e1', (17, 8), (17, 17))
        self.add_line('e2', (17, 17), (7, 17))
        self.add_line('e3', (6, 19), (6, 28))
        self.add_line('e4', (8, 31), (17, 31))
        self.add_line('e5', (17, 31), (17, 40))
        self.add_line('e6', (19, 42), (28, 42))
        self.add_line('e7', (31, 41), (31, 31))
        self.add_line('e8', (31, 31), (40, 31))
        self.add_line('e9', (42, 29), (42, 21))
        self.add_line('e10', (40, 17), (31, 17))
        self.add_bezier('e11', (31, 17), ((30.975, 14.48), (31.167, 12.431), (30.979, 9.927)), ((30.889, 8.749), (31.053, 7.235), (30.243, 6.27)), ((30.095, 6.09), (30.18, 6.131), (30, 6)))
        self.add_bezier('e12', (19, 6), ((18.648, 6), (18.379, 6), (18.027, 6)), ((17.365, 6), (17, 7.403), (17, 8)))
        self.add_bezier('e13', (7, 17), ((6.624, 17.434), (6.016, 18.256), (6.016, 18.886)), ((6.008, 18.952), (6.008, 18.935), (6, 19)))
        self.add_bezier('e14', (6, 28), ((6, 28.123), (6, 28.328), (6, 28.451)), ((6, 30.046), (6.503, 31), (8, 31)))
        self.add_bezier('e15', (17, 40), ((17.524, 40.867), (17.667, 41.984), (18.805, 41.984)), ((18.903, 41.992), (18.902, 41.992), (19, 42)))
        self.add_bezier('e16', (28, 42), ((28.728, 42), (29.547, 41.984), (30.267, 41.984)), ((30.693, 41.984), (30.73, 41.245), (31, 41)))
        self.add_bezier('e17', (40, 31), ((41.268, 30.485), (41.493, 30.252), (42, 29)))
        self.add_bezier('e18', (42, 21), ((42, 20.877), (42, 20.474), (42, 20.351)), ((42, 18.608), (41.906, 17), (40, 17)))
        self.add_contour('c0', 'e11', 'e0', 'e12', 'e1', 'e2', 'e13', 'e3', 'e14', 'e4', 'e5', 'e15', 'e6', 'e16', 'e7', 'e8', 'e17', 'e9', 'e18', 'e10', closed=True)
