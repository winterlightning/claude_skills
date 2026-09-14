"""Shapes (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80482a3e-5b08-4ded-ac07-3afb54321744'
SOURCE_PATH = 'icons-json/design/shapes_80482a3e-5b08-4ded-ac07-3afb54321744.json'
AUTHOR = 'json_to_solo'

class Shapes80482a3e(Solo48):
    icon_id = 'shapes-80482a3e'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('shapes', 'design')

    def build(self):
        self.add_line('e0', (31, 20), (42, 20))
        self.add_line('e1', (42, 20), (42, 42))
        self.add_line('e2', (42, 42), (20, 42))
        self.add_line('e3', (20, 42), (20, 31))
        self.add_line('e4', (31, 20), (20, 20))
        self.add_line('e5', (20, 20), (20, 31))
        self.add_bezier('e6', (31, 20), ((31.016, 18.077), (30.521, 16.203), (29.948, 14.345)), ((28.557, 9.837), (23.951, 6.008), (19.124, 6.008)), ((19.059, 6.008), (18.995, 6), (18.93, 6)), ((18.929, 6), (18.928, 6), (18.927, 6)), ((18.608, 6), (18.281, 6.008), (17.962, 6.008)), ((11.654, 6.008), (6.008, 11.834), (6.008, 18.117)), ((6.008, 18.182), (6, 18.246), (6, 18.311)), ((6, 18.312), (6, 18.313), (6, 18.314)), ((6, 18.584), (6.008, 18.845), (6.008, 19.115)), ((6.008, 24.376), (9.935, 28.917), (14.681, 30.676)), ((16.375, 31.306), (18.216, 30.992), (20, 31)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4', 'e5')
        self.add_contour('c2', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
