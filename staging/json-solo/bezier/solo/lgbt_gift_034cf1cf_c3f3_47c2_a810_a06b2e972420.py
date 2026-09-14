"""Lgbt gift (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '034cf1cf-c3f3-47c2-a810-a06b2e972420'
SOURCE_PATH = 'icons-json/symbol/lgbt gift_034cf1cf-c3f3-47c2-a810-a06b2e972420.json'
AUTHOR = 'json_to_solo'

class LgbtGiftSymbol(Solo48):
    icon_id = 'lgbt-gift-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('lgbt', 'gift', 'symbol')

    def build(self):
        self.add_line('sym-e0', (42, 16), (40, 16))
        self.add_line('sym-e1', (40, 16), (30, 16))
        self.add_line('sym-e2', (30, 16), (24, 16))
        self.add_line('sym-e3', (24, 16), (18, 16))
        self.add_line('sym-e4', (18, 16), (8, 16))
        self.add_line('sym-e5', (8, 16), (6, 16))
        self.add_line('sym-e6', (24, 42), (11, 42))
        self.add_bezier('sym-e7', (11, 42), ((10.91, 42), (11.09, 42), (11, 42)))
        self.add_bezier('sym-e8', (11, 42), ((9.683, 42), (8, 41.252), (8, 40)))
        self.add_line('sym-e9', (8, 40), (8, 16))
        self.add_bezier('sym-e10', (24, 16), ((23.272, 14.552), (22.974, 13.309), (22, 12)))
        self.add_bezier('sym-e11', (22, 12), ((20.102, 9.439), (16.395, 6), (13, 6)))
        self.add_bezier('sym-e12', (13, 6), ((12.885, 6), (13.115, 6), (13, 6)))
        self.add_bezier('sym-e13', (13, 6), ((12.885, 6), (12.115, 6), (12, 6)))
        self.add_bezier('sym-e14', (12, 6), ((9.905, 6), (8.665, 8.085), (9, 10)))
        self.add_bezier('sym-e15', (9, 10), ((9.303, 11.792), (11.265, 13.509), (13, 14)))
        self.add_line('sym-e16', (13, 14), (18, 16))
        self.add_line('sym-e17', (24, 42), (37, 42))
        self.add_bezier('sym-e18', (37, 42), ((37.09, 42), (36.91, 42), (37, 42)))
        self.add_bezier('sym-e19', (37, 42), ((38.317, 42), (40, 41.252), (40, 40)))
        self.add_line('sym-e20', (40, 40), (40, 16))
        self.add_bezier('sym-e21', (24, 16), ((24.728, 14.552), (25.026, 13.309), (26, 12)))
        self.add_bezier('sym-e22', (26, 12), ((27.898, 9.439), (31.605, 6), (35, 6)))
        self.add_bezier('sym-e23', (35, 6), ((35.115, 6), (34.885, 6), (35, 6)))
        self.add_bezier('sym-e24', (35, 6), ((35.115, 6), (35.885, 6), (36, 6)))
        self.add_bezier('sym-e25', (36, 6), ((38.095, 6), (39.335, 8.085), (39, 10)))
        self.add_bezier('sym-e26', (39, 10), ((38.697, 11.792), (36.735, 13.509), (35, 14)))
        self.add_line('sym-e27', (35, 14), (30, 16))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c2', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
        self.add_contour('sym-c3', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20')
        self.add_contour('sym-c4', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
