"""Stapler (office), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '769934a7-f4c1-53a0-94f4-8cabcbf5384b'
SOURCE_PATH = 'icons-json/office/stapler_769934a7-f4c1-53a0-94f4-8cabcbf5384b.json'
AUTHOR = 'json_to_solo'

class StaplerOffice(Solo48):
    icon_id = 'stapler-office'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('stapler', 'office')

    def build(self):
        self.add_line('e0', (37, 40), (7, 40))
        self.add_line('e1', (39, 34), (12, 12))
        self.add_line('e2', (12, 12), (16, 9))
        self.add_line('e3', (22, 10), (43, 27))
        self.add_line('e4', (43, 31), (39, 34))
        self.add_line('e5', (26, 33), (6, 33))
        self.add_line('e6', (6, 33), (6, 29))
        self.add_line('e7', (8, 20), (14, 14))
        self.add_bezier('e8', (39, 34), ((39.009, 35.869), (39.927, 38.072), (38.2, 39.427)), ((37.809, 39.731), (37.527, 40), (37, 40)))
        self.add_bezier('e9', (7, 40), ((6.936, 40), (6.609, 40), (6.545, 39.992)), ((5.109, 39.992), (4, 38.88), (4, 37.583)), ((4, 37.582), (4, 37.581), (4, 37.58)), ((4, 37.522), (4, 37.464), (4, 37.415)), ((4, 36.893), (4.136, 36.32), (4.2, 35.789)), ((4.391, 34.257), (4.655, 33.977), (6, 33)))
        self.add_bezier('e10', (16, 9), ((16.627, 8.419), (17.4, 8.017), (18.255, 8.017)), ((18.398, 8.009), (18.541, 8), (18.684, 8)), ((18.686, 8), (18.689, 8), (18.691, 8)), ((20.127, 8), (21, 9.158), (22, 10)))
        self.add_bezier('e11', (43, 27), ((43.3, 27.48), (43.991, 28.505), (43.991, 29.086)), ((43.991, 29.144), (44, 29.194), (44, 29.252)), ((44, 29.253), (44, 29.254), (44, 29.255)), ((43.991, 29.314), (43.991, 29.373), (43.982, 29.432)), ((43.982, 29.844), (43.3, 30.722), (43, 31)))
        self.add_bezier('e12', (29, 27), ((25.955, 29.509), (26.327, 29.16), (26, 33)))
        self.add_contour('c0', 'e8', 'e0', 'e9')
        self.add_contour('c1', 'e1', 'e2', 'e10', 'e3', 'e11', 'e4', closed=True)
        self.add_contour('c2', 'e12', 'e5')
        self.add_contour('c3', 'e6')
        self.add_contour('c4', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c4', 'c1')
