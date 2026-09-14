"""Keyboard asterisk (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4aff3aef-75a6-5746-bf7d-ae18d5b3397e'
SOURCE_PATH = 'icons-json/interface-essential/keyboard asterisk_4aff3aef-75a6-5746-bf7d-ae18d5b3397e.json'
AUTHOR = 'json_to_solo'

class KeyboardAsterisk4aff3aef(Solo48):
    icon_id = 'keyboard-asterisk-4aff3aef'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'asterisk', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (20, 28), (20, 40))
        self.add_bezier('sym-e1', (20, 40), ((20, 41.219), (20.699, 42), (22, 42)))
        self.add_bezier('sym-e2', (22, 42), ((22.098, 42), (21.902, 42), (22, 42)))
        self.add_bezier('sym-e3', (22, 42), ((22.745, 42), (24.255, 42), (25, 42)))
        self.add_bezier('sym-e4', (25, 42), ((25.147, 42), (24.853, 42), (25, 42)))
        self.add_bezier('sym-e5', (25, 42), ((25.385, 42), (25.615, 42), (26, 42)))
        self.add_bezier('sym-e6', (26, 42), ((27.235, 42), (28, 41.015), (28, 40)))
        self.add_line('sym-e7', (28, 40), (28, 28))
        self.add_line('sym-e8', (28, 28), (39, 28))
        self.add_bezier('sym-e9', (39, 28), ((40.669, 28), (42, 28.095), (42, 26)))
        self.add_bezier('sym-e10', (42, 26), ((42, 25.321), (42, 24.687), (42, 24)))
        self.add_bezier('sym-e11', (42, 24), ((42, 23.828), (42, 23.172), (42, 23)))
        self.add_bezier('sym-e12', (42, 23), ((42, 22.853), (42, 23.147), (42, 23)))
        self.add_bezier('sym-e13', (42, 23), ((42, 20.742), (41.242, 20), (39, 20)))
        self.add_line('sym-e14', (39, 20), (28, 20))
        self.add_line('sym-e15', (28, 20), (28, 9))
        self.add_bezier('sym-e16', (28, 9), ((28, 6.758), (27.258, 6), (25, 6)))
        self.add_bezier('sym-e17', (25, 6), ((24.853, 6), (25.147, 6), (25, 6)))
        self.add_bezier('sym-e18', (25, 6), ((24.828, 6), (24.172, 6), (24, 6)))
        self.add_bezier('sym-e19', (24, 6), ((23.313, 6), (22.679, 6), (22, 6)))
        self.add_bezier('sym-e20', (22, 6), ((19.905, 6), (20, 7.331), (20, 9)))
        self.add_line('sym-e21', (20, 9), (20, 20))
        self.add_line('sym-e22', (20, 20), (8, 20))
        self.add_bezier('sym-e23', (8, 20), ((6.985, 20), (6, 20.765), (6, 22)))
        self.add_bezier('sym-e24', (6, 22), ((6, 22.385), (6, 22.615), (6, 23)))
        self.add_bezier('sym-e25', (6, 23), ((6, 23.147), (6, 22.853), (6, 23)))
        self.add_bezier('sym-e26', (6, 23), ((6, 23.745), (6, 25.255), (6, 26)))
        self.add_bezier('sym-e27', (6, 26), ((6, 26.098), (6, 25.902), (6, 26)))
        self.add_bezier('sym-e28', (6, 26), ((6, 27.301), (6.781, 28), (8, 28)))
        self.add_line('sym-e29', (8, 28), (20, 28))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', closed=True)
