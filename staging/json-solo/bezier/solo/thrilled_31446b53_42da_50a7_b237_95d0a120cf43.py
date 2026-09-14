"""Thrilled (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31446b53-42da-50a7-b237-95d0a120cf43'
SOURCE_PATH = 'icons-json/smileys/thrilled_31446b53-42da-50a7-b237-95d0a120cf43.json'
AUTHOR = 'json_to_solo'

class ThrilledSmileys(Solo48):
    icon_id = 'thrilled-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('thrilled', 'smileys')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('sym-e2', (13, 26), ((13.173, 26.755), (13.636, 27.309), (14, 28)))
        self.add_bezier('sym-e3', (14, 28), ((14.7, 29.327), (15.8, 30.118), (17, 31)))
        self.add_bezier('sym-e4', (17, 31), ((19.103, 32.555), (21.465, 34), (24, 34)))
        self.add_bezier('sym-e5', (24, 34), ((26.535, 34), (28.897, 32.555), (31, 31)))
        self.add_bezier('sym-e6', (31, 31), ((32.2, 30.118), (33.3, 29.327), (34, 28)))
        self.add_bezier('sym-e7', (34, 28), ((34.364, 27.309), (34.827, 26.755), (35, 26)))
        self.add_bezier('sym-e8', (13, 19), ((13.127, 18.309), (13.609, 18.6), (14, 18)))
        self.add_bezier('sym-e9', (14, 18), ((15.673, 15.436), (19.573, 15.3), (21, 18)))
        self.add_bezier('sym-e10', (21, 18), ((21.264, 18.509), (20.891, 18.445), (21, 19)))
        self.add_bezier('sym-e11', (35, 19), ((34.873, 18.309), (34.391, 18.6), (34, 18)))
        self.add_bezier('sym-e12', (34, 18), ((32.327, 15.436), (28.427, 15.3), (27, 18)))
        self.add_bezier('sym-e13', (27, 18), ((26.736, 18.509), (27.109, 18.445), (27, 19)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c2', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c3', 'sym-e11', 'sym-e12', 'sym-e13')
