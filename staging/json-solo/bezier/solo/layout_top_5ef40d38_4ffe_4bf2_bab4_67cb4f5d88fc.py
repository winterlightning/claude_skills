"""Layout top (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ef40d38-4ffe-4bf2-bab4-67cb4f5d88fc'
SOURCE_PATH = 'icons-json/interface-essential/layout top_5ef40d38-4ffe-4bf2-bab4-67cb4f5d88fc.json'
AUTHOR = 'json_to_solo'

class LayoutTopInterfaceEssential(Solo48):
    icon_id = 'layout-top-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'top', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (6, 16), (42, 16))
        self.add_line('sym-e1', (42, 16), (42, 40))
        self.add_bezier('sym-e2', (42, 40), ((42, 41.35), (41.047, 41.624), (40, 42)))
        self.add_line('sym-e3', (40, 42), (24, 42))
        self.add_line('sym-e4', (24, 42), (8, 42))
        self.add_bezier('sym-e5', (8, 42), ((6.953, 41.624), (6, 41.35), (6, 40)))
        self.add_line('sym-e6', (6, 40), (6, 16))
        self.add_line('sym-e7', (6, 16), (6, 8))
        self.add_bezier('sym-e8', (6, 8), ((6.074, 7.812), (6, 8.18), (6, 8)))
        self.add_bezier('sym-e9', (6, 8), ((6.36, 7.247), (7.247, 6.36), (8, 6)))
        self.add_bezier('sym-e10', (8, 6), ((8.172, 6), (7.82, 6.065), (8, 6)))
        self.add_line('sym-e11', (8, 6), (24, 6))
        self.add_line('sym-e12', (24, 6), (40, 6))
        self.add_bezier('sym-e13', (40, 6), ((40.18, 6.065), (39.828, 6), (40, 6)))
        self.add_bezier('sym-e14', (40, 6), ((40.753, 6.36), (41.64, 7.247), (42, 8)))
        self.add_bezier('sym-e15', (42, 8), ((42, 8.18), (41.926, 7.812), (42, 8)))
        self.add_line('sym-e16', (42, 8), (42, 16))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
