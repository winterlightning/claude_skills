"""Dinosaur footprint (animals), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec456c34-7c0b-56af-aad1-9dbebe847e95'
SOURCE_PATH = 'icons-json/animals/dinosaur footprint_ec456c34-7c0b-56af-aad1-9dbebe847e95.json'
AUTHOR = 'json_to_solo'

class DinosaurFootprintAnimals(Solo48):
    icon_id = 'dinosaur-footprint-animals'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('dinosaur', 'footprint', 'animals')

    def build(self):
        self.add_bezier('sym-e0', (24, 44), ((24.148, 43.997), (23.857, 44), (24, 44)))
        self.add_bezier('sym-e1', (24, 44), ((26.888, 44), (30.122, 42.236), (32, 40)))
        self.add_bezier('sym-e2', (32, 40), ((32.547, 39.345), (32.773, 38.864), (33, 38)))
        self.add_line('sym-e3', (33, 38), (35, 31))
        self.add_bezier('sym-e4', (35, 31), ((35.547, 28.927), (37.057, 26.918), (38, 25)))
        self.add_bezier('sym-e5', (38, 25), ((39.154, 22.636), (40, 20.691), (40, 18)))
        self.add_bezier('sym-e6', (40, 18), ((40, 17.918), (40, 17.082), (40, 17)))
        self.add_bezier('sym-e7', (40, 17), ((40, 16.7), (40, 17.3), (40, 17)))
        self.add_bezier('sym-e8', (40, 17), ((40, 16.291), (39.446, 12.309), (39, 12)))
        self.add_bezier('sym-e9', (39, 12), ((38.966, 11.973), (37.505, 12.618), (37, 13)))
        self.add_bezier('sym-e10', (37, 13), ((35.173, 14.391), (33.011, 16.818), (32, 19)))
        self.add_line('sym-e11', (32, 19), (30, 24))
        self.add_line('sym-e12', (30, 24), (28, 20))
        self.add_line('sym-e13', (28, 20), (28, 16))
        self.add_bezier('sym-e14', (28, 16), ((28, 12.709), (27.634, 8.791), (26, 6)))
        self.add_bezier('sym-e15', (26, 6), ((25.834, 5.714), (24.196, 4.066), (24, 4)))
        self.add_bezier('sym-e16', (24, 4), ((23.804, 4.066), (22.166, 5.714), (22, 6)))
        self.add_bezier('sym-e17', (22, 6), ((20.366, 8.791), (20, 12.709), (20, 16)))
        self.add_line('sym-e18', (20, 16), (20, 20))
        self.add_line('sym-e19', (20, 20), (18, 24))
        self.add_line('sym-e20', (18, 24), (16, 19))
        self.add_bezier('sym-e21', (16, 19), ((14.989, 16.818), (12.827, 14.391), (11, 13)))
        self.add_bezier('sym-e22', (11, 13), ((10.495, 12.618), (9.034, 11.973), (9, 12)))
        self.add_bezier('sym-e23', (9, 12), ((8.554, 12.309), (8, 16.291), (8, 17)))
        self.add_bezier('sym-e24', (8, 17), ((8, 17.3), (8, 16.7), (8, 17)))
        self.add_bezier('sym-e25', (8, 17), ((8, 17.082), (8, 17.918), (8, 18)))
        self.add_bezier('sym-e26', (8, 18), ((8, 20.691), (8.846, 22.636), (10, 25)))
        self.add_bezier('sym-e27', (10, 25), ((10.943, 26.918), (12.453, 28.927), (13, 31)))
        self.add_line('sym-e28', (13, 31), (15, 38))
        self.add_bezier('sym-e29', (15, 38), ((15.227, 38.864), (15.453, 39.345), (16, 40)))
        self.add_bezier('sym-e30', (16, 40), ((17.878, 42.236), (21.112, 44), (24, 44)))
        self.add_bezier('sym-e31', (24, 44), ((24.143, 44), (23.852, 43.997), (24, 44)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', closed=True)
