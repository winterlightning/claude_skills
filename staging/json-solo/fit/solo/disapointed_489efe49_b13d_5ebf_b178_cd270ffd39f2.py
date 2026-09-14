"""Disapointed (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '489efe49-b13d-5ebf-b178-cd270ffd39f2'
SOURCE_PATH = 'icons-json/smileys/disapointed_489efe49-b13d-5ebf-b178-cd270ffd39f2.json'
AUTHOR = 'json_to_solo'

class DisapointedSmileys(Solo48):
    icon_id = 'disapointed-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('disapointed', 'smileys')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_arc('sym-e2', (12, 19), (19, 17), radius_x=7, sweep=False)
        self.add_arc('sym-e3', (15, 27), (19, 24), radius_x=4, sweep=False)
        self.add_arc('sym-e4', (17, 34), (24, 30), radius_x=9)
        self.add_arc('sym-e5', (24, 30), (31, 34), radius_x=9)
        self.add_arc('sym-e6', (36, 19), (29, 17), radius_x=7)
        self.add_arc('sym-e7', (33, 27), (29, 24), radius_x=4)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3')
        self.add_contour('sym-c3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c4', 'sym-e6')
        self.add_contour('sym-c5', 'sym-e7')
