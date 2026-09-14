"""Sum symbol (state), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '534e35bc-f17a-4308-b045-175383e7b0e9'
SOURCE_PATH = 'icons-json/state/sum symbol_534e35bc-f17a-4308-b045-175383e7b0e9.json'
AUTHOR = 'json_to_solo'

class SumSymbolState(Solo48):
    icon_id = 'sum-symbol-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('sum', 'symbol', 'state')

    def build(self):
        self.add_line('e0', (40, 4), (8, 4))
        self.add_line('e1', (8, 4), (25, 24))
        self.add_line('e2', (25, 24), (8, 44))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
