"""Sign badge badge (maps), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51affb95-85ee-5312-8a83-f077a030e9a9'
SOURCE_PATH = 'icons-json/maps/sign badge badge_51affb95-85ee-5312-8a83-f077a030e9a9.json'
AUTHOR = 'json_to_solo'

class SignBadgeBadge51affb95(Solo48):
    icon_id = 'sign-badge-badge-51affb95'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('sign', 'badge', 'maps')

    def build(self):
        self.add_line('sym-e0', (8, 23), (8, 7))
        self.add_line('sym-e1', (8, 7), (11, 9))
        self.add_bezier('sym-e2', (11, 9), ((12.145, 9.927), (13.829, 9.691), (15, 9)))
        self.add_line('sym-e3', (15, 9), (24, 4))
        self.add_line('sym-e4', (24, 4), (33, 9))
        self.add_bezier('sym-e5', (33, 9), ((34.171, 9.691), (35.855, 9.927), (37, 9)))
        self.add_line('sym-e6', (37, 9), (40, 7))
        self.add_line('sym-e7', (40, 7), (40, 23))
        self.add_bezier('sym-e8', (40, 23), ((40, 23.218), (40, 23.773), (40, 24)))
        self.add_bezier('sym-e9', (40, 24), ((40, 30.745), (33.589, 36.2), (29, 40)))
        self.add_bezier('sym-e10', (29, 40), ((28.032, 40.8), (25.128, 44), (24, 44)))
        self.add_bezier('sym-e11', (24, 44), ((23.99, 44), (24.012, 44), (24, 44)))
        self.add_bezier('sym-e12', (24, 44), ((23.988, 44), (24.01, 44), (24, 44)))
        self.add_bezier('sym-e13', (24, 44), ((22.872, 44), (19.968, 40.8), (19, 40)))
        self.add_bezier('sym-e14', (19, 40), ((14.411, 36.2), (8, 30.745), (8, 24)))
        self.add_bezier('sym-e15', (8, 24), ((8, 23.773), (8, 23.218), (8, 23)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
