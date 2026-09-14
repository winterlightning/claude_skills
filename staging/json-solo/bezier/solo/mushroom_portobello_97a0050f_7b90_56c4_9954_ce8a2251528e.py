"""Mushroom portobello (food), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97a0050f-7b90-56c4-9954-ce8a2251528e'
SOURCE_PATH = 'icons-json/food/mushroom portobello_97a0050f-7b90-56c4-9954-ce8a2251528e.json'
AUTHOR = 'json_to_solo'

class MushroomPortobelloFood(Solo48):
    icon_id = 'mushroom-portobello-food'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('mushroom', 'portobello', 'food')

    def build(self):
        self.add_bezier('sym-e0', (30, 25), ((30.836, 29.589), (33.582, 37.962), (27, 40)))
        self.add_bezier('sym-e1', (27, 40), ((26.291, 40), (25.755, 40), (25, 40)))
        self.add_bezier('sym-e2', (25, 40), ((24.718, 40), (24.282, 40), (24, 40)))
        self.add_bezier('sym-e3', (24, 40), ((23.964, 40), (24.036, 40), (24, 40)))
        self.add_bezier('sym-e4', (24, 40), ((23.964, 40), (24.036, 40), (24, 40)))
        self.add_bezier('sym-e5', (24, 40), ((23.718, 40), (23.282, 40), (23, 40)))
        self.add_bezier('sym-e6', (23, 40), ((22.245, 40), (21.709, 40), (21, 40)))
        self.add_bezier('sym-e7', (21, 40), ((14.418, 37.962), (17.164, 29.589), (18, 25)))
        self.add_bezier('sym-e8', (18, 25), ((20.213, 24.809), (21.891, 25), (24, 25)))
        self.add_bezier('sym-e9', (24, 25), ((26.109, 25), (27.787, 24.809), (30, 25)))
        self.add_bezier('sym-e10', (30, 25), ((31.209, 25.101), (32.8, 24.722), (34, 25)))
        self.add_line('sym-e11', (34, 25), (41, 27))
        self.add_bezier('sym-e12', (41, 27), ((41.236, 27.051), (41.764, 26.042), (42, 26)))
        self.add_bezier('sym-e13', (42, 26), ((43.473, 25.731), (44, 25.238), (44, 24)))
        self.add_bezier('sym-e14', (44, 24), ((44, 23.907), (44, 23.093), (44, 23)))
        self.add_bezier('sym-e15', (44, 23), ((44, 22.259), (44, 21.724), (44, 21)))
        self.add_bezier('sym-e16', (44, 21), ((42.418, 12.949), (32.3, 8), (24, 8)))
        self.add_bezier('sym-e17', (24, 8), ((23.873, 8), (24.127, 8), (24, 8)))
        self.add_bezier('sym-e18', (24, 8), ((23.873, 8), (24.127, 8), (24, 8)))
        self.add_bezier('sym-e19', (24, 8), ((15.7, 8), (5.582, 12.949), (4, 21)))
        self.add_bezier('sym-e20', (4, 21), ((4, 21.724), (4, 22.259), (4, 23)))
        self.add_bezier('sym-e21', (4, 23), ((4, 23.093), (4, 23.907), (4, 24)))
        self.add_bezier('sym-e22', (4, 24), ((4, 25.238), (4.527, 25.731), (6, 26)))
        self.add_bezier('sym-e23', (6, 26), ((6.236, 26.042), (6.764, 27.051), (7, 27)))
        self.add_line('sym-e24', (7, 27), (14, 25))
        self.add_bezier('sym-e25', (14, 25), ((15.2, 24.722), (16.791, 25.101), (18, 25)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25')
