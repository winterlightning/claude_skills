"""Happy (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9dc19a96-ebe9-58f5-9d4b-f39f7a84ec75'
SOURCE_PATH = 'pictographic-primitives/smileys/happy_9dc19a96-ebe9-58f5-9d4b-f39f7a84ec75.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Happy(Solo48):
    icon_id = 'happy'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('happy', 'smileys')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('sym-e2', (14, 20), ((14.073, 19.564), (13.818, 19.418), (14, 19)))
        self.add_bezier('sym-e3', (14, 19), ((14.873, 17.055), (17.845, 17.209), (19, 19)))
        self.add_bezier('sym-e4', (19, 19), ((19.336, 19.527), (18.909, 19.409), (19, 20)))
        self.add_bezier('sym-e5', (15, 28), ((15.727, 29.582), (16.682, 30.836), (18, 32)))
        self.add_bezier('sym-e6', (18, 32), ((19.765, 33.57), (21.822, 34), (24, 34)))
        self.add_bezier('sym-e7', (24, 34), ((24.017, 34), (23.983, 34), (24, 34)))
        self.add_bezier('sym-e8', (24, 34), ((24.017, 34), (23.983, 34), (24, 34)))
        self.add_bezier('sym-e9', (24, 34), ((26.178, 34), (28.235, 33.57), (30, 32)))
        self.add_bezier('sym-e10', (30, 32), ((31.318, 30.836), (32.273, 29.582), (33, 28)))
        self.add_bezier('sym-e11', (34, 20), ((33.927, 19.564), (34.182, 19.418), (34, 19)))
        self.add_bezier('sym-e12', (34, 19), ((33.127, 17.055), (30.155, 17.209), (29, 19)))
        self.add_bezier('sym-e13', (29, 19), ((28.664, 19.527), (29.091, 19.409), (29, 20)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c3', 'sym-e11', 'sym-e12', 'sym-e13')
