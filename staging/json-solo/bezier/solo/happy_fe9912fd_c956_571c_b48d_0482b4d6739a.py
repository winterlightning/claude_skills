"""Happy (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fe9912fd-c956-571c-b48d-0482b4d6739a'
SOURCE_PATH = 'icons-json/smileys/happy_fe9912fd-c956-571c-b48d-0482b4d6739a.json'
AUTHOR = 'json_to_solo'

class HappyFe9912fd(Solo48):
    icon_id = 'happy-fe9912fd'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('happy', 'smileys')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('sym-e2', (14, 20), ((14.136, 19.409), (14.682, 19.536), (15, 19)))
        self.add_bezier('sym-e3', (15, 19), ((15.855, 17.527), (17.845, 16.764), (19, 18)))
        self.add_bezier('sym-e4', (19, 18), ((19.564, 18.609), (18.809, 19.236), (19, 20)))
        self.add_bezier('sym-e5', (14, 29), ((15.958, 33.316), (19.98, 34.994), (24, 35)))
        self.add_bezier('sym-e6', (24, 35), ((28.02, 34.994), (32.042, 33.316), (34, 29)))
        self.add_bezier('sym-e7', (34, 20), ((33.864, 19.409), (33.318, 19.536), (33, 19)))
        self.add_bezier('sym-e8', (33, 19), ((32.145, 17.527), (30.155, 16.764), (29, 18)))
        self.add_bezier('sym-e9', (29, 18), ((28.436, 18.609), (29.191, 19.236), (29, 20)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7', 'sym-e8', 'sym-e9')
