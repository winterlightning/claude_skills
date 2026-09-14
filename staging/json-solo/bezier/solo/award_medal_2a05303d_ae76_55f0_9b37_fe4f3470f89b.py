"""Award medal (rewards), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a05303d-ae76-55f0-9b37-fe4f3470f89b'
SOURCE_PATH = 'icons-json/rewards/award medal_2a05303d-ae76-55f0-9b37-fe4f3470f89b.json'
AUTHOR = 'json_to_solo'

class AwardMedal2a05303d(Solo48):
    icon_id = 'award-medal-2a05303d'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rewards'
    aliases = ()
    keywords = ('award', 'medal', 'rewards')

    def build(self):
        self.add_line('e0', (19, 22), (8, 4))
        self.add_line('e1', (8, 4), (40, 4))
        self.add_line('e2', (40, 4), (29, 22))
        self.add_line('e3', (34, 13), (14, 13))
        self.add_bezier('e4', (29, 22), ((30.05, 22.473), (31.16, 23.127), (32.09, 23.791)), ((34.48, 25.482), (36.22, 28.245), (36.69, 30.964)), ((37.84, 37.591), (31.99, 43.982), (24.54, 43.982)), ((24.29, 43.982), (24.03, 44), (23.78, 44)), ((23.775, 44), (23.769, 44), (23.764, 44)), ((23.429, 44), (23.085, 43.982), (22.75, 43.982)), ((21.37, 43.982), (19.8, 43.491), (18.57, 42.973)), ((12.83, 40.564), (9.96, 34.582), (12.02, 29.118)), ((13.35, 25.591), (15.58, 23.782), (19, 22)))
        self.add_bezier('e5', (29, 22), ((25.66, 21.255), (22.32, 21.164), (19, 22)))
        self.add_contour('c0', 'e4', 'e0', 'e1', 'e2', closed=True)
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c2', 'c0')
