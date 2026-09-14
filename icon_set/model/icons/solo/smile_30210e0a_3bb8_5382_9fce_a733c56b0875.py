"""Smile (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30210e0a-3bb8-5382-9fce-a733c56b0875'
SOURCE_PATH = 'icons-json/smileys/smile_30210e0a-3bb8-5382-9fce-a733c56b0875.json'
AUTHOR = 'json_to_solo'

class SmileSmileys(Solo48):
    icon_id = 'smile-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('smile', 'smileys')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('sym-e2', (14, 20), ((14.082, 19.491), (13.773, 19.473), (14, 19)))
        self.add_bezier('sym-e3', (14, 19), ((14.927, 17.118), (17.845, 17.164), (19, 19)))
        self.add_bezier('sym-e4', (19, 19), ((19.364, 19.582), (18.918, 19.345), (19, 20)))
        self.add_bezier('sym-e5', (13, 28), ((15.386, 32.318), (19.447, 34.951), (24, 35)))
        self.add_bezier('sym-e6', (24, 35), ((28.553, 34.951), (32.614, 32.318), (35, 28)))
        self.add_bezier('sym-e7', (34, 20), ((33.918, 19.491), (34.227, 19.473), (34, 19)))
        self.add_bezier('sym-e8', (34, 19), ((33.073, 17.118), (30.155, 17.164), (29, 19)))
        self.add_bezier('sym-e9', (29, 19), ((28.636, 19.582), (29.082, 19.345), (29, 20)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7', 'sym-e8', 'sym-e9')
