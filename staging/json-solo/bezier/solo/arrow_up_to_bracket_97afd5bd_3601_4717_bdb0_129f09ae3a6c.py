"""Arrow up to bracket (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97afd5bd-3601-4717-bdb0-129f09ae3a6c'
SOURCE_PATH = 'icons-json/symbol/arrow up to bracket_97afd5bd-3601-4717-bdb0-129f09ae3a6c.json'
AUTHOR = 'json_to_solo'

class ArrowUpToBracketSymbol(Solo48):
    icon_id = 'arrow-up-to-bracket-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'up', 'to', 'bracket', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 6), (24, 31))
        self.add_line('sym-e1', (15, 16), (24, 6))
        self.add_line('sym-e2', (24, 6), (33, 16))
        self.add_line('sym-e3', (6, 32), (6, 37))
        self.add_bezier('sym-e4', (6, 37), ((6, 39.242), (7.496, 42), (10, 42)))
        self.add_line('sym-e5', (10, 42), (24, 42))
        self.add_line('sym-e6', (24, 42), (38, 42))
        self.add_bezier('sym-e7', (38, 42), ((40.504, 42), (42, 39.242), (42, 37)))
        self.add_line('sym-e8', (42, 37), (42, 32))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
