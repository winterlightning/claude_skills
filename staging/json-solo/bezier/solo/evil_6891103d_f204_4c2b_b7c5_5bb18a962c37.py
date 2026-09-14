"""Evil (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6891103d-f204-4c2b-b7c5-5bb18a962c37'
SOURCE_PATH = 'icons-json/smileys/evil_6891103d-f204-4c2b-b7c5-5bb18a962c37.json'
AUTHOR = 'json_to_solo'

class EvilSmileys(Solo48):
    icon_id = 'evil-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('evil', 'smileys')

    def build(self):
        self.add_line('e0', (13, 17), (20, 21))
        self.add_line('e1', (28, 21), (35, 17))
        self.add_line('e2', (14, 34), (17, 28))
        self.add_line('e3', (17, 28), (20, 34))
        self.add_line('e4', (20, 34), (24, 28))
        self.add_line('e5', (24, 28), (28, 34))
        self.add_line('e6', (28, 34), (31, 28))
        self.add_line('e7', (31, 28), (34, 33))
        self.add_arc('e8-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e8-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
