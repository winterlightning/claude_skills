"""Layout left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e4d2ef1c-4583-47fc-bc76-b5edcb616774'
SOURCE_PATH = 'icons-json/interface-essential/layout left_e4d2ef1c-4583-47fc-bc76-b5edcb616774.json'
AUTHOR = 'json_to_solo'

class LayoutLeftInterfaceEssential(Solo48):
    icon_id = 'layout-left-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'left', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (20, 42), (20, 6))
        self.add_line('sym-e1', (20, 6), (40, 6))
        self.add_bezier('sym-e2', (40, 6), ((41.391, 6), (41.648, 6.895), (42, 8)))
        self.add_line('sym-e3', (42, 8), (42, 24))
        self.add_line('sym-e4', (42, 24), (42, 40))
        self.add_bezier('sym-e5', (42, 40), ((41.648, 41.105), (41.391, 42), (40, 42)))
        self.add_line('sym-e6', (40, 42), (20, 42))
        self.add_line('sym-e7', (20, 42), (8, 42))
        self.add_bezier('sym-e8', (8, 42), ((6.936, 42), (6, 41.031), (6, 40)))
        self.add_line('sym-e9', (6, 40), (6, 24))
        self.add_line('sym-e10', (6, 24), (6, 8))
        self.add_bezier('sym-e11', (6, 8), ((6, 6.969), (6.936, 6), (8, 6)))
        self.add_line('sym-e12', (8, 6), (20, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
