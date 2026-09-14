"""Dog bark (pets), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca5793fd-6124-5adc-af11-d58e19f57b73'
SOURCE_PATH = 'icons-json/pets/dog bark_ca5793fd-6124-5adc-af11-d58e19f57b73.json'
AUTHOR = 'json_to_solo'

class DogBarkPets(Solo48):
    icon_id = 'dog-bark-pets'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('dog', 'bark', 'pets')

    def build(self):
        self.add_line('e0', (34, 14), (26, 15))
        self.add_line('e1', (22, 18), (16, 18))
        self.add_line('e2', (23, 32), (30, 31))
        self.add_line('e3', (30, 31), (35, 40))
        self.add_line('e4', (44, 15), (44, 21))
        self.add_line('e5', (4, 16), (8, 19))
        self.add_line('e6', (4, 26), (9, 26))
        self.add_line('e7', (6, 35), (9, 32))
        self.add_bezier('e8', (39, 8), ((38, 10.375), (37.245, 13.663), (34, 14)))
        self.add_bezier('e9', (26, 15), ((25.536, 15.328), (24.9, 15.352), (24.573, 15.815)), ((24.191, 16.354), (23.882, 17.095), (23.345, 17.516)), ((23, 17.785), (22.391, 17.815), (22, 18)))
        self.add_bezier('e10', (16, 18), ((15.827, 19.844), (15.691, 21.853), (17.364, 23.116)), ((17.673, 23.343), (18.036, 23.638), (18.418, 23.756)), ((19.718, 24.152), (23.755, 24.328), (24.027, 25.651)), ((24.3, 26.973), (20.818, 28.733), (19.809, 29.238)), ((19.364, 29.457), (18.2, 30.055), (18.2, 30.08)), ((18.264, 32.152), (21.273, 32.396), (23, 32)))
        self.add_bezier('e11', (39, 8), ((39.182, 8.101), (39.845, 8.101), (40.027, 8.219)), ((42.091, 9.608), (43.991, 11.857), (43.991, 14.341)), ((43.991, 14.467), (44, 14.865), (44, 15)))
        self.add_contour('c0', 'e8', 'e0', 'e9', 'e1', 'e10', 'e2', 'e3')
        self.add_contour('c1', 'e11', 'e4')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e6')
        self.add_contour('c4', 'e7')
