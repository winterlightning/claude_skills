"""Bad (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8cbc437-b9e5-5c6d-99ac-831170873a90'
SOURCE_PATH = 'icons-json/smileys/bad_b8cbc437-b9e5-5c6d-99ac-831170873a90.json'
AUTHOR = 'json_to_solo'

class BadSmileys(Solo48):
    icon_id = 'bad-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('bad', 'smileys')

    def build(self):
        self.add_line('e0', (13, 20), (19, 20))
        self.add_line('e1', (29, 20), (35, 20))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e3', (17, 33), (31, 33), radius_x=8)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e3')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
