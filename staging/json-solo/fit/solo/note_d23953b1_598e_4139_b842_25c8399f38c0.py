"""Note (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd23953b1-598e-4139-b842-25c8399f38c0'
SOURCE_PATH = 'icons-json/symbol/note_d23953b1-598e-4139-b842-25c8399f38c0.json'
AUTHOR = 'json_to_solo'

class NoteSymbol(Solo48):
    icon_id = 'note-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('note', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 13), (24, 9))
        self.add_line('sym-e1', (24, 9), (24, 6))
        self.add_line('sym-e2', (13, 13), (13, 9))
        self.add_line('sym-e3', (13, 9), (13, 6))
        self.add_line('sym-e4', (24, 42), (8, 42))
        self.add_arc('sym-e5', (8, 42), (6, 40), radius_x=2)
        self.add_line('sym-e6', (6, 40), (6, 11))
        self.add_line('sym-e7', (6, 11), (6, 10))
        self.add_arc('sym-e8', (6, 10), (8, 9), radius_x=2)
        self.add_line('sym-e9', (8, 9), (13, 9))
        self.add_line('sym-e10', (13, 9), (24, 9))
        self.add_line('sym-e11', (24, 9), (35, 9))
        self.add_line('sym-e12', (35, 9), (35, 13))
        self.add_line('sym-e13', (35, 6), (35, 9))
        self.add_line('sym-e14', (35, 9), (40, 9))
        self.add_arc('sym-e15', (40, 9), (42, 10), radius_x=2)
        self.add_arc('sym-e16', (42, 10), (42, 11), radius_x=1, sweep=False)
        self.add_line('sym-e17', (42, 11), (42, 40))
        self.add_arc('sym-e18', (42, 40), (40, 42), radius_x=2)
        self.add_line('sym-e19', (40, 42), (24, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c3', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
