"""Underwear bra (clothes), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3b3183b-a5c5-5cf0-9723-f3424e6fedf1'
SOURCE_PATH = 'icons-json/clothes/underwear bra_c3b3183b-a5c5-5cf0-9723-f3424e6fedf1.json'
AUTHOR = 'json_to_solo'

class UnderwearBraC3b3183b(Solo48):
    icon_id = 'underwear-bra-c3b3183b'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('underwear', 'bra', 'clothes')

    def build(self):
        self.add_line('sym-e0', (26, 34), (22, 34))
        self.add_bezier('sym-e1', (22, 34), ((20.718, 37.293), (18, 40), (14, 40)))
        self.add_bezier('sym-e2', (14, 40), ((13.873, 40), (14.127, 40), (14, 40)))
        self.add_bezier('sym-e3', (14, 40), ((13.8, 40), (13.2, 40), (13, 40)))
        self.add_bezier('sym-e4', (13, 40), ((7.773, 40), (4, 34.497), (4, 30)))
        self.add_bezier('sym-e5', (4, 30), ((4, 29.798), (4, 30.202), (4, 30)))
        self.add_bezier('sym-e6', (4, 30), ((4, 29.806), (4, 29.202), (4, 29)))
        self.add_bezier('sym-e7', (4, 29), ((4, 25.497), (6.3, 22.998), (8, 20)))
        self.add_bezier('sym-e8', (8, 20), ((8.327, 18.855), (7.855, 17.187), (8, 16)))
        self.add_bezier('sym-e9', (8, 16), ((8.312, 13.503), (9, 11.516), (9, 9)))
        self.add_bezier('sym-e10', (9, 9), ((9, 8.733), (8.994, 8.267), (9, 8)))
        self.add_bezier('sym-e11', (39, 8), ((39.006, 8.267), (39, 8.733), (39, 9)))
        self.add_bezier('sym-e12', (39, 9), ((39, 11.516), (39.688, 13.503), (40, 16)))
        self.add_bezier('sym-e13', (40, 16), ((40.145, 17.187), (39.673, 18.855), (40, 20)))
        self.add_bezier('sym-e14', (40, 20), ((41.7, 22.998), (44, 25.497), (44, 29)))
        self.add_bezier('sym-e15', (44, 29), ((44, 29.202), (44, 29.806), (44, 30)))
        self.add_bezier('sym-e16', (44, 30), ((44, 30.202), (44, 29.798), (44, 30)))
        self.add_bezier('sym-e17', (44, 30), ((44, 34.497), (40.227, 40), (35, 40)))
        self.add_bezier('sym-e18', (35, 40), ((34.8, 40), (34.2, 40), (34, 40)))
        self.add_bezier('sym-e19', (34, 40), ((33.873, 40), (34.127, 40), (34, 40)))
        self.add_bezier('sym-e20', (34, 40), ((30, 40), (27.282, 37.293), (26, 34)))
        self.add_bezier('sym-e21', (26, 34), ((27.373, 30.261), (27.409, 27.543), (31, 25)))
        self.add_bezier('sym-e22', (31, 25), ((31.945, 24.335), (33.909, 24.429), (35, 24)))
        self.add_bezier('sym-e23', (35, 24), ((36.427, 23.436), (37.818, 22.985), (39, 22)))
        self.add_bezier('sym-e24', (39, 22), ((39.673, 21.436), (39.509, 20.682), (40, 20)))
        self.add_bezier('sym-e25', (22, 34), ((20.627, 30.261), (20.591, 27.543), (17, 25)))
        self.add_bezier('sym-e26', (17, 25), ((16.055, 24.335), (14.091, 24.429), (13, 24)))
        self.add_bezier('sym-e27', (13, 24), ((11.573, 23.436), (10.182, 22.985), (9, 22)))
        self.add_bezier('sym-e28', (9, 22), ((8.327, 21.436), (8.491, 20.682), (8, 20)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c1', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24')
        self.add_contour('sym-c2', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
