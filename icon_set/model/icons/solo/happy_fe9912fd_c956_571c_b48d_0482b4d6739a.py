"""Happy (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fe9912fd-c956-571c-b48d-0482b4d6739a'
SOURCE_PATH = 'icons-json/smileys/happy_fe9912fd-c956-571c-b48d-0482b4d6739a.json'
AUTHOR = 'json_to_solo'

class HappySmileys(Solo48):
    icon_id = 'happy-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('happy', 'smileys')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_arc('sym-e2', (14, 20), (15, 19), radius_x=5)
        self.add_arc('sym-e3', (15, 19), (19, 18), radius_x=3)
        self.add_line('sym-e4', (19, 18), (19, 20))
        self.add_arc('sym-e5', (14, 29), (24, 35), radius_x=10, sweep=False)
        self.add_arc('sym-e6', (24, 35), (34, 29), radius_x=10, sweep=False)
        self.add_arc('sym-e7', (34, 20), (33, 19), radius_x=5, sweep=False)
        self.add_arc('sym-e8', (33, 19), (29, 18), radius_x=3, sweep=False)
        self.add_line('sym-e9', (29, 18), (29, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7', 'sym-e8', 'sym-e9')
