"""B4 (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8220eff5-889a-4ed4-abe8-9cb5b3c749d9'
SOURCE_PATH = 'icons-json/state/B4_8220eff5-889a-4ed4-abe8-9cb5b3c749d9.json'
AUTHOR = 'json_to_solo'

class B4State(Solo48):
    icon_id = 'b4-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('b4', 'state')

    def build(self):
        self.add_line('e0', (4, 8), (4, 40))
        self.add_line('e1', (4, 40), (10, 40))
        self.add_line('e2', (12, 8), (4, 8))
        self.add_line('e3', (13, 24), (4, 24))
        self.add_line('e4', (44, 33), (29, 33))
        self.add_line('e5', (29, 33), (41, 8))
        self.add_line('e6', (41, 8), (41, 40))
        self.add_bezier('e7', (10, 40), ((10.627, 40), (11.618, 39.975), (12.255, 39.975)), ((13.773, 39.975), (15.364, 39.68), (16.691, 38.572)), ((19.345, 36.369), (20.445, 30.658), (18.355, 27.249)), ((17.491, 25.858), (16.245, 25.071), (14.973, 24.615)), ((14.573, 24.48), (13.336, 24.283), (13.091, 24)), ((13.082, 23.988), (13.427, 23.902), (13.818, 23.754)), ((14.409, 23.52), (14.991, 23.225), (15.518, 22.794)), ((16.936, 21.662), (18.027, 19.84), (18.391, 17.649)), ((19.318, 11.988), (16.118, 8), (12, 8)))
        self.add_contour('c0', 'e0', 'e1', 'e7', 'e2', closed=True)
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e5', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
