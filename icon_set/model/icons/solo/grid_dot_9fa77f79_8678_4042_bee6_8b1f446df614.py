"""Grid dot (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9fa77f79-8678-4042-bee6-8b1f446df614'
SOURCE_PATH = 'icons-json/design/grid dot_9fa77f79-8678-4042-bee6-8b1f446df614.json'
AUTHOR = 'json_to_solo'

class GridDot(Solo48):
    icon_id = 'grid-dot'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('grid', 'dot', 'design')

    def build(self):
        self.add_line('sym-e0', (6, 24), (6, 9))
        self.add_arc('sym-e1', (6, 9), (9, 6), radius_x=4)
        self.add_line('sym-e2', (9, 6), (24, 6))
        self.add_line('sym-e3', (24, 6), (39, 6))
        self.add_arc('sym-e4', (39, 6), (42, 9), radius_x=4)
        self.add_line('sym-e5', (42, 9), (42, 24))
        self.add_line('sym-e6', (42, 24), (42, 39))
        self.add_arc('sym-e7', (42, 39), (39, 42), radius_x=4)
        self.add_line('sym-e8', (39, 42), (24, 42))
        self.add_line('sym-e9', (24, 42), (9, 42))
        self.add_arc('sym-e10', (9, 42), (6, 39), radius_x=5)
        self.add_line('sym-e11', (6, 39), (6, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', closed=True)
