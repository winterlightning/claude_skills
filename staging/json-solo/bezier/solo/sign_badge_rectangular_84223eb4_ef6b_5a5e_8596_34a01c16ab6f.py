"""Sign badge rectangular (maps), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84223eb4-ef6b-5a5e-8596-34a01c16ab6f'
SOURCE_PATH = 'icons-json/maps/sign badge rectangular_84223eb4-ef6b-5a5e-8596-34a01c16ab6f.json'
AUTHOR = 'json_to_solo'

class SignBadgeRectangularMaps(Solo48):
    icon_id = 'sign-badge-rectangular-maps'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('sign', 'badge', 'rectangular', 'maps')

    def build(self):
        self.add_line('e0', (42, 6), (6, 6))
        self.add_line('e1', (6, 6), (6, 42))
        self.add_line('e2', (6, 42), (42, 42))
        self.add_line('e3', (42, 42), (42, 6))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', closed=True)
