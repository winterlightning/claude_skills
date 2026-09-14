"""Loading (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd472b1c1-49d3-4bb8-b76f-109c04be5a74'
SOURCE_PATH = 'icons-json/interface-essential/loading_d472b1c1-49d3-4bb8-b76f-109c04be5a74.json'
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
        self.add_line('sym-e0', (37, 24), (42, 24))
        self.add_line('sym-e1', (11, 24), (6, 24))
        self.add_line('sym-e2', (24, 42), (24, 37))
        self.add_line('sym-e3', (34, 34), (36, 36))
        self.add_line('sym-e4', (14, 34), (12, 36))
        self.add_line('sym-e5', (24, 6), (24, 11))
        self.add_line('sym-e6', (34, 14), (36, 12))
        self.add_line('sym-e7', (14, 14), (12, 12))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2')
        self.add_contour('sym-c3', 'sym-e3')
        self.add_contour('sym-c4', 'sym-e4')
        self.add_contour('sym-c5', 'sym-e5')
        self.add_contour('sym-c6', 'sym-e6')
        self.add_contour('sym-c7', 'sym-e7')
