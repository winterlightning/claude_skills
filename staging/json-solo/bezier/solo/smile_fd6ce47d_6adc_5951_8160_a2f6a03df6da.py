"""Smile (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd6ce47d-6adc-5951-8160-a2f6a03df6da'
SOURCE_PATH = 'icons-json/smileys/smile_fd6ce47d-6adc-5951-8160-a2f6a03df6da.json'
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
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('sym-e2', (13, 20), ((13.1, 19.355), (13.618, 19.564), (14, 19)))
        self.add_bezier('sym-e3', (14, 19), ((15.364, 16.991), (18.027, 16.736), (19, 19)))
        self.add_bezier('sym-e4', (19, 19), ((19.191, 19.427), (18.927, 19.555), (19, 20)))
        self.add_bezier('sym-e5', (14, 29), ((16.168, 32.968), (20.086, 34.977), (24, 35)))
        self.add_bezier('sym-e6', (24, 35), ((27.914, 34.977), (31.832, 32.968), (34, 29)))
        self.add_bezier('sym-e7', (35, 20), ((34.9, 19.355), (34.382, 19.564), (34, 19)))
        self.add_bezier('sym-e8', (34, 19), ((32.636, 16.991), (29.973, 16.736), (29, 19)))
        self.add_bezier('sym-e9', (29, 19), ((28.809, 19.427), (29.073, 19.555), (29, 20)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7', 'sym-e8', 'sym-e9')
