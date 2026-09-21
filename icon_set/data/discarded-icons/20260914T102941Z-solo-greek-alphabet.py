"""Greek alphabet (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f242159-ca9e-43ff-8d0b-a4a49bdb4507'
SOURCE_PATH = 'icons-json/interface-essential/greek alphabet_2f242159-ca9e-43ff-8d0b-a4a49bdb4507.json'
AUTHOR = 'json_to_solo'

class GreekAlphabet(Solo48):
    icon_id = 'greek-alphabet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('greek', 'alphabet', 'interface-essential')

    def build(self):
        self.add_line('sym-e1', (24, 6), (31, 7))
        self.add_arc('sym-e2', (31, 7), (40, 23), radius_x=17)
        self.add_line('sym-e3', (40, 23), (40, 27))
        self.add_arc('sym-e4', (40, 27), (32, 38), radius_x=17)
        self.add_arc('sym-e5', (32, 38), (29, 40), radius_x=25, sweep=False)
        self.add_line('sym-e6', (29, 40), (29, 42))
        self.add_line('sym-e7', (29, 42), (42, 42))
        self.add_line('sym-e9', (24, 6), (17, 7))
        self.add_arc('sym-e10', (17, 7), (8, 23), radius_x=18, sweep=False)
        self.add_line('sym-e11', (8, 23), (8, 27))
        self.add_arc('sym-e12', (8, 27), (16, 38), radius_x=17, sweep=False)
        self.add_line('sym-e13', (16, 38), (19, 40))
        self.add_line('sym-e14', (19, 40), (19, 42))
        self.add_line('sym-e15', (19, 42), (6, 42))
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c1', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.relate('connect', 'sym-c0', 'sym-c1')
