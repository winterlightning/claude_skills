"""Loading (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35b4ace4-6ffa-5ad8-a6c0-f1e837f61b64'
SOURCE_PATH = 'icons-json/interface-essential/loading_35b4ace4-6ffa-5ad8-a6c0-f1e837f61b64.json'
AUTHOR = 'json_to_solo'

class Loading35b4ace4(Solo48):
    icon_id = 'loading-35b4ace4'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('loading', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (35, 24), (42, 24))
        self.add_line('sym-e1', (13, 24), (6, 24))
        self.add_line('sym-e2', (24, 35), (24, 42))
        self.add_line('sym-e3', (32, 33), (37, 37))
        self.add_line('sym-e4', (16, 33), (11, 37))
        self.add_line('sym-e5', (24, 13), (24, 6))
        self.add_line('sym-e6', (32, 15), (37, 11))
        self.add_line('sym-e7', (16, 15), (11, 11))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2')
        self.add_contour('sym-c3', 'sym-e3')
        self.add_contour('sym-c4', 'sym-e4')
        self.add_contour('sym-c5', 'sym-e5')
        self.add_contour('sym-c6', 'sym-e6')
        self.add_contour('sym-c7', 'sym-e7')
