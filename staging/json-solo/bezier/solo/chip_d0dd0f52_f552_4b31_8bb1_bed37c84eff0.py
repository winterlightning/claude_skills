"""Chip (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0dd0f52-f552-4b31-8bb1-bed37c84eff0'
SOURCE_PATH = 'icons-json/symbol/chip_d0dd0f52-f552-4b31-8bb1-bed37c84eff0.json'
AUTHOR = 'json_to_solo'

class ChipD0dd0f52(Solo48):
    icon_id = 'chip-d0dd0f52'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('chip', 'symbol')

    def build(self):
        self.add_line('e0', (18, 6), (18, 13))
        self.add_line('e1', (6, 19), (13, 19))
        self.add_line('e2', (6, 30), (13, 30))
        self.add_line('e3', (18, 42), (18, 35))
        self.add_line('e4', (30, 42), (30, 35))
        self.add_line('e5', (35, 30), (42, 30))
        self.add_line('e6', (42, 19), (35, 19))
        self.add_line('e7', (30, 6), (30, 13))
        self.add_line('e8', (32, 35), (17, 35))
        self.add_line('e9', (13, 32), (13, 20))
        self.add_line('e10', (17, 13), (32, 13))
        self.add_line('e11', (35, 16), (35, 28))
        self.add_bezier('e12', (35, 28), ((35, 31.265), (34.669, 26.749), (34.636, 29.727)), ((34.62, 31.175), (35.234, 33.057), (33.875, 34.088)), ((33.393, 34.448), (32.597, 35), (32, 35)))
        self.add_bezier('e13', (17, 35), ((14.856, 35), (13.753, 34.168), (13, 32)))
        self.add_bezier('e14', (13, 20), ((13, 19.73), (13.355, 19.369), (13.364, 19.091)), ((13.413, 16.653), (13.572, 13), (17, 13)))
        self.add_bezier('e15', (32, 13), ((33.505, 13.491), (34.542, 14.486), (35, 16)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e12', 'e8', 'e13', 'e9', 'e14', 'e10', 'e15', 'e11', closed=True)
        self.relate('connect', 'c0', 'c8')
        self.relate('connect', 'c1', 'c8')
        self.relate('connect', 'c2', 'c8')
        self.relate('connect', 'c3', 'c8')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
