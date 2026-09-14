"""Smile (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '83cd55ce-7a5d-588c-85a9-6b8cc54ce8fc'
SOURCE_PATH = 'icons-json/smileys/smile_83cd55ce-7a5d-588c-85a9-6b8cc54ce8fc.json'
AUTHOR = 'json_to_solo'

class Smile(Solo48):
    icon_id = 'smile'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('smile', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e1', (14, 20), ((14.145, 19.355), (14.236, 19.045), (14.564, 18.445)), ((15.509, 16.745), (17.918, 16.309), (18.918, 18.227)), ((19.282, 18.927), (18.9, 19.218), (19, 20)))
        self.add_bezier('e2', (29, 19), ((29.136, 18.427), (28.755, 18.255), (29.091, 17.764)), ((30.1, 16.282), (32.027, 16.518), (33.045, 17.855)), ((33.582, 18.564), (33.8, 19.164), (34, 20)))
        self.add_bezier('e3', (13, 29), ((16.127, 36.082), (26.209, 38.2), (31.736, 32.355)), ((32.791, 31.255), (33.445, 30.4), (34, 29)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
