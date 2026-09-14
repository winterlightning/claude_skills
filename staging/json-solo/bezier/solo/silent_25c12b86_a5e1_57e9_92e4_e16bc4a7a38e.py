"""Silent (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25c12b86-a5e1-57e9-92e4-e16bc4a7a38e'
SOURCE_PATH = 'icons-json/smileys/silent_25c12b86-a5e1-57e9-92e4-e16bc4a7a38e.json'
AUTHOR = 'json_to_solo'

class SilentSmileys(Solo48):
    icon_id = 'silent-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('silent', 'smileys')

    def build(self):
        self.add_line('e0', (30, 17), (30, 21))
        self.add_line('e1', (18, 17), (18, 21))
        self.add_line('e2', (14, 29), (34, 29))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
