"""Eject (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '458c9640-e242-4ef4-92b2-a6a2f8d73b15'
SOURCE_PATH = 'icons-json/symbol/eject_458c9640-e242-4ef4-92b2-a6a2f8d73b15.json'
AUTHOR = 'json_to_solo'

class EjectSymbol(Solo48):
    icon_id = 'eject-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('eject', 'symbol')

    def build(self):
        self.add_line('e0', (42, 42), (6, 42))
        self.add_line('e1', (42, 29), (24, 6))
        self.add_line('e2', (24, 6), (6, 29))
        self.add_line('e3', (6, 29), (42, 29))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', closed=True)
