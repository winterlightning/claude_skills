"""Layout 16 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7517780d-21e9-4a66-bbc8-b5debc9349f7'
SOURCE_PATH = 'icons-json/interface-essential/layout 16_7517780d-21e9-4a66-bbc8-b5debc9349f7.json'
AUTHOR = 'json_to_solo'

class Layout16InterfaceEssential(Solo48):
    icon_id = 'layout-16-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        self.add_line('e0', (31, 16), (31, 42))
        self.add_line('e1', (31, 16), (42, 16))
        self.add_line('e2', (31, 16), (6, 16))
        self.add_line('e3', (42, 16), (42, 40))
        self.add_line('e4', (40, 42), (31, 42))
        self.add_line('e5', (42, 16), (42, 8))
        self.add_line('e6', (40, 6), (8, 6))
        self.add_line('e7', (6, 8), (6, 16))
        self.add_line('e8', (31, 42), (8, 42))
        self.add_line('e9', (6, 40), (6, 16))
        self.add_bezier('e10', (42, 40), ((42, 41.121), (41.113, 42), (40, 42)))
        self.add_bezier('e11', (42, 8), ((42, 7.01), (40.895, 6.524), (40.077, 6.139)), ((39.905, 6.057), (40.172, 6.065), (40, 6)))
        self.add_bezier('e12', (8, 6), ((6.527, 6.507), (6.524, 6.535), (6, 8)))
        self.add_bezier('e13', (8, 42), ((7.828, 41.935), (8.103, 41.959), (7.931, 41.877)), ((7.121, 41.493), (6, 40.99), (6, 40)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e10', 'e4')
        self.add_contour('c4', 'e5', 'e11', 'e6', 'e12', 'e7')
        self.add_contour('c5', 'e8', 'e13', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
