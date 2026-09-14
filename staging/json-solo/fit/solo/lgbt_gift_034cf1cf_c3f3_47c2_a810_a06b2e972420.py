"""Lgbt gift (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
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
        self.add_line('sym-e8', (11, 42), (8, 40))
        self.add_line('sym-e9', (8, 40), (8, 16))
        self.add_arc('sym-e10', (24, 16), (22, 12), radius_x=27)
        self.add_arc('sym-e11', (22, 12), (13, 6), radius_x=12, sweep=False)
        self.add_line('sym-e13', (13, 6), (12, 6))
        self.add_arc('sym-e14', (12, 6), (9, 10), radius_x=4, sweep=False)
        self.add_arc('sym-e15', (9, 10), (13, 14), radius_x=4, sweep=False)
        self.add_line('sym-e16', (13, 14), (18, 16))
        self.add_line('sym-e17', (24, 42), (37, 42))
        self.add_line('sym-e19', (37, 42), (40, 40))
        self.add_line('sym-e20', (40, 40), (40, 16))
        self.add_arc('sym-e21', (24, 16), (26, 12), radius_x=27)
        self.add_arc('sym-e22', (26, 12), (35, 6), radius_x=12)
        self.add_line('sym-e24', (35, 6), (36, 6))
        self.add_arc('sym-e25', (36, 6), (39, 10), radius_x=4)
        self.add_arc('sym-e26', (39, 10), (35, 14), radius_x=4)
        self.add_line('sym-e27', (35, 14), (30, 16))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c2', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
        self.add_contour('sym-c3', 'sym-e17', 'sym-e19', 'sym-e20')
        self.add_contour('sym-c4', 'sym-e21', 'sym-e22', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27')
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
