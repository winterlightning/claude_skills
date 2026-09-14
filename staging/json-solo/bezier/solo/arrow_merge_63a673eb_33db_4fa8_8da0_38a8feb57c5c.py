"""Arrow merge (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '63a673eb-33db-4fa8-8da0-38a8feb57c5c'
SOURCE_PATH = 'icons-json/symbol/arrow merge_63a673eb-33db-4fa8-8da0-38a8feb57c5c.json'
AUTHOR = 'json_to_solo'

class ArrowMergeSymbol(Solo48):
    icon_id = 'arrow-merge-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'merge', 'symbol')

    def build(self):
        self.add_line('e0', (16, 6), (6, 6))
        self.add_line('e1', (6, 17), (6, 6))
        self.add_line('e2', (24, 42), (24, 35))
        self.add_line('e3', (42, 17), (42, 6))
        self.add_line('e4', (32, 6), (42, 6))
        self.add_line('e5', (6, 6), (11, 10))
        self.add_line('e6', (22, 28), (24, 35))
        self.add_line('e7', (24, 35), (26, 28))
        self.add_line('e8', (36, 11), (42, 6))
        self.add_bezier('e9', (11, 10), ((12.145, 10.957), (13.045, 12.243), (14.01, 13.38)), ((16.972, 16.841), (19.345, 20.711), (21.185, 24.867)), ((21.644, 25.898), (21.755, 26.895), (22, 28)))
        self.add_bezier('e10', (26, 28), ((26.475, 25.848), (27.265, 23.812), (28.295, 21.889)), ((30.022, 18.674), (32.043, 15.548), (34.473, 12.824)), ((35.045, 12.177), (35.345, 11.565), (36, 11)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5', 'e9', 'e6')
        self.add_contour('c6', 'e7', 'e10', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
