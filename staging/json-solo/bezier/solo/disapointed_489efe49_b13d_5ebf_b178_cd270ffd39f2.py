"""Disapointed (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e2', (12, 19), ((15.1, 19.336), (16.918, 19.345), (19, 17)))
        self.add_bezier('sym-e3', (15, 27), ((17.073, 26.773), (18.327, 26.018), (19, 24)))
        self.add_bezier('sym-e4', (17, 34), ((19.068, 31.376), (21.395, 30), (24, 30)))
        self.add_bezier('sym-e5', (24, 30), ((26.605, 30), (28.932, 31.376), (31, 34)))
        self.add_bezier('sym-e6', (36, 19), ((32.9, 19.336), (31.082, 19.345), (29, 17)))
        self.add_bezier('sym-e7', (33, 27), ((30.927, 26.773), (29.673, 26.018), (29, 24)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3')
        self.add_contour('sym-c3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c4', 'sym-e6')
        self.add_contour('sym-c5', 'sym-e7')
