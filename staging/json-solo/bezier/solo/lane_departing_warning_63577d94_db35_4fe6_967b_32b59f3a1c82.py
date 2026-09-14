"""Lane departing warning (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '63577d94-db35-4fe6-967b-32b59f3a1c82'
SOURCE_PATH = 'icons-json/transportation/lane departing warning_63577d94-db35-4fe6-967b-32b59f3a1c82.json'
AUTHOR = 'json_to_solo'

class LaneDepartingWarningTransportation(Solo48):
    icon_id = 'lane-departing-warning-transportation'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('lane', 'departing', 'warning', 'transportation')

    def build(self):
        self.add_line('e0', (6, 42), (16, 6))
        self.add_line('e1', (32, 6), (42, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
