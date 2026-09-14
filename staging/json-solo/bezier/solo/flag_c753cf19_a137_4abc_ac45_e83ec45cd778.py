"""Flag (social), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c753cf19-a137-4abc-ac45-e83ec45cd778'
SOURCE_PATH = 'icons-json/social/flag_c753cf19-a137-4abc-ac45-e83ec45cd778.json'
AUTHOR = 'json_to_solo'

class Flag(Solo48):
    icon_id = 'flag'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    aliases = ()
    keywords = ('flag', 'social')

    def build(self):
        self.add_line('e0', (8, 4), (8, 9))
        self.add_line('e1', (8, 44), (8, 29))
        self.add_line('e2', (23, 6), (28, 8))
        self.add_line('e3', (40, 7), (40, 28))
        self.add_line('e4', (28, 29), (22, 27))
        self.add_line('e5', (12, 27), (8, 29))
        self.add_line('e6', (8, 9), (8, 29))
        self.add_bezier('e7', (8, 9), ((9.145, 8.327), (10.451, 7), (11.705, 6.4)), ((15.335, 4.682), (19.227, 4.645), (23, 6)))
        self.add_bezier('e8', (28, 8), ((32.606, 9.655), (35.621, 8.818), (40, 7)))
        self.add_bezier('e9', (40, 28), ((38.998, 28.573), (38.004, 28.845), (36.935, 29.273)), ((34.451, 30.282), (30.493, 30.155), (28, 29)))
        self.add_bezier('e10', (22, 27), ((19.154, 25.682), (14.863, 25.764), (12, 27)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e7', 'e2', 'e8', 'e3', 'e9', 'e4', 'e10', 'e5')
        self.add_contour('c3', 'e6')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
