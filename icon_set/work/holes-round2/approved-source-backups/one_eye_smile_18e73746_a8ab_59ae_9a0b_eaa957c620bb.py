"""One eye smile (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18e73746-a8ab-59ae-9a0b-eaa957c620bb'
SOURCE_PATH = 'icons-json/smileys/one eye smile_18e73746-a8ab-59ae-9a0b-eaa957c620bb.json'
AUTHOR = 'json_to_solo'

class OneEyeSmile(Solo48):
    icon_id = 'one-eye-smile'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('one', 'eye', 'smile', 'smileys')

    def build(self):
        self.add_line('e0', (33, 18), (29, 20))
        self.add_line('e1', (29, 20), (33, 23))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e3', (15, 29), (33, 29), radius_x=10, sweep=False)
        self.add_arc('e4-1', (20, 21), (16, 22), radius_x=3)
        self.add_arc('e4-2', (16, 22), (16, 17), radius_x=4)
        self.add_arc('e4-3', (16, 17), (20, 21), radius_x=3)
        self.add_contour('c0', 'e3')
        self.add_contour('c1', 'e0', 'e1')
        self.add_contour('c2', 'e4-1', 'e4-2', 'e4-3', closed=True)
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
