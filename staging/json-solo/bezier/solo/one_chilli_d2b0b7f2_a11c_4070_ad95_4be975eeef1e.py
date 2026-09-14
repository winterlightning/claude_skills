"""One chilli (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd2b0b7f2-a11c-4070-ad95-4be975eeef1e'
SOURCE_PATH = 'icons-json/symbol/one chilli_d2b0b7f2-a11c-4070-ad95-4be975eeef1e.json'
AUTHOR = 'json_to_solo'

class OneChilliSymbol(Solo48):
    icon_id = 'one-chilli-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('one', 'chilli', 'symbol')

    def build(self):
        self.add_line('e0', (40, 18), (43, 14))
        self.add_bezier('e1', (40, 18), ((38.945, 17.44), (38.164, 16.272), (37.045, 16.192)), ((33.173, 15.952), (30.309, 20.768), (27.055, 23.68)), ((24.4, 26.064), (21.518, 27.568), (18.6, 28.544)), ((15.391, 29.616), (12.145, 29.808), (8.891, 29.44)), ((7.636, 29.312), (6.391, 29.04), (5.136, 28.992)), ((4.975, 28.992), (4, 28.992), (4, 29.007)), ((4, 29.008), (4, 29.008), (4, 29.008)), ((4.155, 29.936), (4.318, 30.848), (4.473, 31.776)), ((4.773, 32.944), (6.609, 34.608), (7.255, 35.152)), ((10.127, 37.552), (13.182, 38.704), (16.318, 39.44)), ((17.318, 39.664), (18.364, 40), (19.364, 40)), ((19.365, 40), (19.366, 40), (19.367, 40)), ((19.448, 40), (19.519, 40), (19.6, 40)), ((20.209, 40), (20.809, 39.968), (21.409, 39.968)), ((27.027, 39.968), (33.164, 37.584), (37.882, 32.048)), ((39.827, 29.76), (42.691, 25.632), (41.664, 20.912)), ((41.4, 19.696), (40.436, 19.008), (40, 18)))
        self.add_bezier('e2', (43, 14), ((43.291, 13.344), (44, 12.848), (44, 11.936)), ((44, 10.624), (44, 9.312), (44, 8)))
        self.add_contour('c0', 'e1', closed=True)
        self.add_contour('c1', 'e0', 'e2')
        self.relate('connect', 'c0', 'c1')
