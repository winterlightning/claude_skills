"""Arrow rotate left (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aae9a13a-212b-4153-933b-96407d00ab7a'
SOURCE_PATH = 'icons-json/symbol/arrow rotate left_aae9a13a-212b-4153-933b-96407d00ab7a.json'
AUTHOR = 'json_to_solo'

class ArrowRotateLeftSymbol(Solo48):
    icon_id = 'arrow-rotate-left-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'rotate', 'left', 'symbol')

    def build(self):
        self.add_line('e0', (15, 6), (6, 15))
        self.add_line('e1', (15, 23), (6, 15))
        self.add_line('e2', (42, 42), (42, 16))
        self.add_line('e3', (40, 15), (6, 15))
        self.add_bezier('e4', (42, 16), ((41.935, 15.951), (41.853, 15.491), (41.795, 15.442)), ((41.46, 15.139), (40.442, 15), (40, 15)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e4', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
