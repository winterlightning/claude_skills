"""You are here (maps), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82a3c844-00ee-4332-b0d6-05e549a272c0'
SOURCE_PATH = 'icons-json/maps/you are here_82a3c844-00ee-4332-b0d6-05e549a272c0.json'
AUTHOR = 'json_to_solo'

class YouAreHereMaps(Solo48):
    icon_id = 'you-are-here-maps'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('you', 'are', 'here', 'maps')

    def build(self):
        self.add_arc('sym-e0', (18, 18), (30, 18), radius_x=6, radius_y=5)
        self.add_arc('sym-e1', (30, 18), (18, 18), radius_x=6, radius_y=5)
        self.add_bezier('sym-e2', (8, 41), ((12.28, 43.218), (18.12, 44), (23, 44)))
        self.add_bezier('sym-e3', (23, 44), ((23.21, 44), (22.79, 44), (23, 44)))
        self.add_bezier('sym-e4', (23, 44), ((23.187, 44), (23.814, 44), (24, 44)))
        self.add_bezier('sym-e5', (24, 44), ((24.186, 44), (24.813, 44), (25, 44)))
        self.add_bezier('sym-e6', (25, 44), ((25.21, 44), (24.79, 44), (25, 44)))
        self.add_bezier('sym-e7', (25, 44), ((29.88, 44), (35.72, 43.218), (40, 41)))
        self.add_line('sym-e8', (23, 38), (14, 29))
        self.add_bezier('sym-e9', (14, 29), ((11.14, 26.118), (8, 22.064), (8, 18)))
        self.add_bezier('sym-e10', (8, 18), ((8, 17.891), (8, 17.109), (8, 17)))
        self.add_bezier('sym-e11', (8, 17), ((8, 16.718), (8, 17.282), (8, 17)))
        self.add_bezier('sym-e12', (8, 17), ((8, 9.991), (15.66, 4), (23, 4)))
        self.add_bezier('sym-e13', (23, 4), ((23.1, 4), (22.9, 4), (23, 4)))
        self.add_bezier('sym-e14', (23, 4), ((23.206, 4), (23.797, 4), (24, 4)))
        self.add_bezier('sym-e15', (24, 4), ((24.203, 4), (24.794, 4), (25, 4)))
        self.add_bezier('sym-e16', (25, 4), ((25.1, 4), (24.9, 4), (25, 4)))
        self.add_bezier('sym-e17', (25, 4), ((32.34, 4), (40, 9.991), (40, 17)))
        self.add_bezier('sym-e18', (40, 17), ((40, 17.282), (40, 16.718), (40, 17)))
        self.add_bezier('sym-e19', (40, 17), ((40, 17.109), (40, 17.891), (40, 18)))
        self.add_bezier('sym-e20', (40, 18), ((40, 22.064), (36.86, 26.118), (34, 29)))
        self.add_line('sym-e21', (34, 29), (25, 38))
        self.add_bezier('sym-e22', (25, 38), ((24.68, 38.318), (24.33, 38.7), (24, 39)))
        self.add_bezier('sym-e23', (24, 39), ((23.67, 38.7), (23.32, 38.318), (23, 38)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c2', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
