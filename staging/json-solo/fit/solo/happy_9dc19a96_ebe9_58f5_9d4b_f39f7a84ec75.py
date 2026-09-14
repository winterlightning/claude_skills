"""Happy (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9dc19a96-ebe9-58f5-9d4b-f39f7a84ec75'
SOURCE_PATH = 'icons-json/smileys/happy_9dc19a96-ebe9-58f5-9d4b-f39f7a84ec75.json'
AUTHOR = 'json_to_solo'

class Happy9dc19a96(Solo48):
    icon_id = 'happy-9dc19a96'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('happy', 'smileys')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_line('sym-e2', (14, 20), (14, 19))
        self.add_arc('sym-e3', (14, 19), (19, 19), radius_x=3)
        self.add_line('sym-e4', (19, 19), (19, 20))
        self.add_line('sym-e5', (15, 28), (18, 32))
        self.add_arc('sym-e6', (18, 32), (24, 34), radius_x=8, sweep=False)
        self.add_arc('sym-e9', (24, 34), (30, 32), radius_x=8, sweep=False)
        self.add_line('sym-e10', (30, 32), (33, 28))
        self.add_line('sym-e11', (34, 20), (34, 19))
        self.add_arc('sym-e12', (34, 19), (29, 19), radius_x=3, sweep=False)
        self.add_line('sym-e13', (29, 19), (29, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c3', 'sym-e11', 'sym-e12', 'sym-e13')
