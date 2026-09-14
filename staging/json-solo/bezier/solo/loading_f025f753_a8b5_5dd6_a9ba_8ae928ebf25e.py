"""Loading (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f025f753-a8b5-5dd6-a9ba-8ae928ebf25e'
SOURCE_PATH = 'icons-json/interface-essential/loading_f025f753-a8b5-5dd6-a9ba-8ae928ebf25e.json'
AUTHOR = 'json_to_solo'

class Loading(Solo48):
    icon_id = 'loading'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('loading', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (6, 24), (17, 24))
        self.add_line('sym-e1', (42, 24), (31, 24))
        self.add_line('sym-e2', (24, 42), (24, 31))
        self.add_line('sym-e3', (12, 37), (18, 30))
        self.add_line('sym-e4', (36, 37), (30, 30))
        self.add_line('sym-e5', (24, 6), (24, 17))
        self.add_line('sym-e6', (12, 11), (18, 18))
        self.add_line('sym-e7', (36, 11), (30, 18))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2')
        self.add_contour('sym-c3', 'sym-e3')
        self.add_contour('sym-c4', 'sym-e4')
        self.add_contour('sym-c5', 'sym-e5')
        self.add_contour('sym-c6', 'sym-e6')
        self.add_contour('sym-c7', 'sym-e7')
