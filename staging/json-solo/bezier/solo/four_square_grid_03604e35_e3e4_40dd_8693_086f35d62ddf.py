"""Four square grid (_uncategorized_01), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03604e35-e3e4-40dd-8693-086f35d62ddf'
SOURCE_PATH = 'icons-json/_uncategorized_01/Four Square Grid_03604e35-e3e4-40dd-8693-086f35d62ddf.json'
AUTHOR = 'json_to_solo'

class FourSquareGridUncategorized01(Solo48):
    icon_id = 'four-square-grid-uncategorized-01'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('four', 'square', 'grid', '_uncategorized_01')

    def build(self):
        self.add_line('sym-e0', (6, 24), (24, 24))
        self.add_line('sym-e1', (24, 24), (42, 24))
        self.add_line('sym-e2', (42, 24), (42, 8))
        self.add_bezier('sym-e3', (42, 8), ((41.517, 6.985), (41.006, 6.466), (40, 6)))
        self.add_line('sym-e4', (40, 6), (24, 6))
        self.add_line('sym-e5', (24, 6), (24, 24))
        self.add_line('sym-e6', (24, 24), (24, 42))
        self.add_line('sym-e7', (24, 42), (8, 42))
        self.add_bezier('sym-e8', (8, 42), ((6.994, 41.534), (6.483, 41.015), (6, 40)))
        self.add_line('sym-e9', (6, 40), (6, 24))
        self.add_line('sym-e10', (6, 24), (6, 8))
        self.add_bezier('sym-e11', (6, 8), ((6.483, 6.985), (6.994, 6.466), (8, 6)))
        self.add_line('sym-e12', (8, 6), (24, 6))
        self.add_line('sym-e13', (42, 24), (42, 40))
        self.add_bezier('sym-e14', (42, 40), ((41.517, 41.015), (41.006, 41.534), (40, 42)))
        self.add_line('sym-e15', (40, 42), (24, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c1', 'sym-e13', 'sym-e14', 'sym-e15')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
