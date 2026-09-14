"""Keyboard button (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f64ef8b-f8cd-5add-84ab-cb04db2d8ac7'
SOURCE_PATH = 'icons-json/interface-essential/keyboard button_2f64ef8b-f8cd-5add-84ab-cb04db2d8ac7.json'
AUTHOR = 'json_to_solo'

class KeyboardButtonInterfaceEssential(Solo48):
    icon_id = 'keyboard-button-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'button', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (6, 24), (6, 13))
        self.add_bezier('sym-e1', (6, 13), ((6, 12.869), (6, 12.131), (6, 12)))
        self.add_bezier('sym-e2', (6, 12), ((6, 9.194), (8.333, 6.671), (11, 6)))
        self.add_bezier('sym-e3', (11, 6), ((11.9, 6), (13.084, 6), (14, 6)))
        self.add_bezier('sym-e4', (14, 6), ((14.466, 6), (14.534, 6), (15, 6)))
        self.add_line('sym-e5', (15, 6), (24, 6))
        self.add_line('sym-e6', (24, 6), (33, 6))
        self.add_bezier('sym-e7', (33, 6), ((33.466, 6), (33.534, 6), (34, 6)))
        self.add_bezier('sym-e8', (34, 6), ((34.916, 6), (36.1, 6), (37, 6)))
        self.add_bezier('sym-e9', (37, 6), ((39.667, 6.671), (42, 9.194), (42, 12)))
        self.add_bezier('sym-e10', (42, 12), ((42, 12.131), (42, 12.869), (42, 13)))
        self.add_line('sym-e11', (42, 13), (42, 24))
        self.add_line('sym-e12', (42, 24), (42, 35))
        self.add_bezier('sym-e13', (42, 35), ((42, 35.131), (42, 35.869), (42, 36)))
        self.add_bezier('sym-e14', (42, 36), ((42, 38.806), (39.667, 41.329), (37, 42)))
        self.add_bezier('sym-e15', (37, 42), ((36.1, 42), (34.916, 42), (34, 42)))
        self.add_bezier('sym-e16', (34, 42), ((33.534, 42), (33.466, 42), (33, 42)))
        self.add_line('sym-e17', (33, 42), (24, 42))
        self.add_line('sym-e18', (24, 42), (15, 42))
        self.add_bezier('sym-e19', (15, 42), ((14.534, 42), (14.466, 42), (14, 42)))
        self.add_bezier('sym-e20', (14, 42), ((13.084, 42), (11.9, 42), (11, 42)))
        self.add_bezier('sym-e21', (11, 42), ((8.333, 41.329), (6, 38.806), (6, 36)))
        self.add_bezier('sym-e22', (6, 36), ((6, 35.869), (6, 35.131), (6, 35)))
        self.add_line('sym-e23', (6, 35), (6, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
