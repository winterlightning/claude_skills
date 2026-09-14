"""Very happy (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '882fdc6f-fb69-486c-9abe-a9e651b9caf0'
SOURCE_PATH = 'icons-json/smileys/very happy_882fdc6f-fb69-486c-9abe-a9e651b9caf0.json'
AUTHOR = 'json_to_solo'

class VeryHappySmileys(Solo48):
    icon_id = 'very-happy-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('very', 'happy', 'smileys')

    def build(self):
        self.add_line('e0', (17, 28), (31, 28))
        self.add_arc('e1-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e1-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e2', (10, 19), (19, 19), radius_x=5)
        self.add_arc('e3', (29, 19), (38, 19), radius_x=5)
        self.add_arc('e4-1', (31, 28), (23, 36), radius_x=7)
        self.add_arc('e4-2', (23, 36), (17, 28), radius_x=7)
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e0', 'e4-1', 'e4-2', closed=True)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
