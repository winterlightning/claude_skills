"""Funnel (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '107e54f1-5e5c-40e0-a51b-c1aeca9aed3a'
SOURCE_PATH = 'icons-json/symbol/funnel_107e54f1-5e5c-40e0-a51b-c1aeca9aed3a.json'
AUTHOR = 'json_to_solo'

class FunnelSymbol(Solo48):
    icon_id = 'funnel-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('funnel', 'symbol')

    def build(self):
        self.add_line('e0', (19, 42), (19, 28))
        self.add_line('e1', (19, 26), (6, 6))
        self.add_line('e2', (6, 6), (42, 6))
        self.add_line('e3', (42, 6), (29, 26))
        self.add_line('e4', (29, 33), (19, 42))
        self.add_bezier('e5', (19, 28), ((19, 27.182), (19.025, 26.826), (19, 26)))
        self.add_bezier('e6', (29, 26), ((28.362, 27.988), (28.811, 28.688), (29.024, 30.644)), ((29.114, 31.445), (29.098, 32.206), (29, 33)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e2', 'e3', 'e6', 'e4', closed=True)
