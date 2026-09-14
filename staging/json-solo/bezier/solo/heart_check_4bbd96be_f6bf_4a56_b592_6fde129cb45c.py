"""Heart check (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4bbd96be-f6bf-4a56-b592-6fde129cb45c'
SOURCE_PATH = 'icons-json/state/heart check_4bbd96be-f6bf-4a56-b592-6fde129cb45c.json'
AUTHOR = 'json_to_solo'

class HeartCheckState(Solo48):
    icon_id = 'heart-check-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('heart', 'check', 'state')

    def build(self):
        self.add_line('e0', (34, 18), (23, 28))
        self.add_line('e1', (23, 28), (17, 22))
        self.add_line('e2', (24, 40), (8, 25))
        self.add_line('e3', (41, 24), (24, 40))
        self.add_bezier('e4', (8, 25), ((6.082, 23.223), (4.018, 20.396), (4.018, 17.794)), ((4.009, 17.659), (4.009, 17.524), (4, 17.398)), ((4, 17.396), (4, 17.394), (4, 17.392)), ((4, 17.259), (4.009, 17.126), (4.009, 17.002)), ((4.009, 11.848), (10.264, 8), (15.7, 8.084)), ((16.755, 8.244), (17.809, 8.648), (18.782, 9.036)), ((20.236, 9.617), (21.627, 10.636), (22.745, 11.663)), ((23.118, 12), (23.491, 12.354), (23.855, 12.699)), ((23.909, 12.758), (23.973, 12.808), (24.027, 12.867)), ((24.118, 12.859), (26.318, 10.804), (26.673, 10.526)), ((28.255, 9.272), (30.973, 8), (33.1, 8)), ((33.103, 8), (33.107, 8), (33.11, 8)), ((33.325, 8), (33.549, 8.017), (33.764, 8.017)), ((39.155, 8.017), (43.982, 12.539), (43.982, 17.499)), ((43.991, 17.632), (44, 17.756), (44, 17.88)), ((44, 17.882), (44, 17.884), (44, 17.886)), ((44, 20.034), (42.636, 22.484), (41, 24)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e4', 'e3', closed=True)
