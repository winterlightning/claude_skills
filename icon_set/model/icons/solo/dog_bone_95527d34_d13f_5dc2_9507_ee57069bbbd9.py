"""Dog bone (pets), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95527d34-d13f-5dc2-9507-ee57069bbbd9'
SOURCE_PATH = 'icons-json/pets/dog bone_95527d34-d13f-5dc2-9507-ee57069bbbd9.json'
AUTHOR = 'json_to_solo'

class DogBone(Solo48):
    icon_id = 'dog-bone'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('dog', 'bone', 'pets')

    def build(self):
        self.add_line('sym-e0', (41, 24), (42, 24))
        self.add_bezier('sym-e1', (16, 17), ((15.209, 13.247), (14.573, 10.324), (12, 9)))
        self.add_bezier('sym-e2', (12, 9), ((11.591, 8.782), (10.427, 8), (10, 8)))
        self.add_bezier('sym-e3', (10, 8), ((9.891, 8), (10.109, 8), (10, 8)))
        self.add_bezier('sym-e4', (10, 8), ((9.791, 8), (9.209, 8), (9, 8)))
        self.add_bezier('sym-e5', (9, 8), ((6.063, 8), (4, 12.541), (4, 17)))
        self.add_bezier('sym-e6', (4, 17), ((4, 17.964), (4, 19.053), (4, 20)))
        self.add_bezier('sym-e7', (4, 20), ((4.355, 21.425), (5.318, 21.953), (6, 23)))
        self.add_bezier('sym-e8', (6, 23), ((6.102, 23.149), (6.925, 23.767), (7, 24)))
        self.add_bezier('sym-e9', (7, 24), ((6.925, 24.233), (6.102, 24.851), (6, 25)))
        self.add_bezier('sym-e10', (6, 25), ((5.318, 26.047), (4.355, 26.575), (4, 28)))
        self.add_bezier('sym-e11', (4, 28), ((4, 28.947), (4, 30.036), (4, 31)))
        self.add_bezier('sym-e12', (4, 31), ((4, 35.459), (6.063, 40), (9, 40)))
        self.add_bezier('sym-e13', (9, 40), ((9.209, 40), (9.791, 40), (10, 40)))
        self.add_bezier('sym-e14', (10, 40), ((10.109, 40), (9.891, 40), (10, 40)))
        self.add_bezier('sym-e15', (10, 40), ((10.427, 40), (11.591, 39.218), (12, 39)))
        self.add_bezier('sym-e16', (12, 39), ((14.573, 37.676), (15.209, 34.753), (16, 31)))
        self.add_line('sym-e17', (16, 31), (32, 31))
        self.add_bezier('sym-e18', (32, 31), ((32.318, 32.542), (32.4, 34.662), (33, 36)))
        self.add_bezier('sym-e19', (33, 36), ((34.082, 38.415), (36.136, 40), (38, 40)))
        self.add_bezier('sym-e20', (38, 40), ((38.164, 40), (38.845, 40), (39, 40)))
        self.add_bezier('sym-e21', (39, 40), ((39.073, 40), (38.927, 40), (39, 40)))
        self.add_bezier('sym-e22', (39, 40), ((41.791, 40), (44, 35.276), (44, 31)))
        self.add_bezier('sym-e23', (44, 31), ((44, 30.884), (44, 31.116), (44, 31)))
        self.add_bezier('sym-e24', (44, 31), ((44, 30.884), (44, 31.116), (44, 31)))
        self.add_bezier('sym-e25', (44, 31), ((44, 29.269), (43.682, 27.265), (43, 26)))
        self.add_bezier('sym-e26', (43, 26), ((42.709, 25.462), (42.309, 24.495), (42, 24)))
        self.add_bezier('sym-e27', (42, 24), ((42.309, 23.505), (42.709, 22.538), (43, 22)))
        self.add_bezier('sym-e28', (43, 22), ((43.682, 20.735), (44, 18.731), (44, 17)))
        self.add_bezier('sym-e29', (44, 17), ((44, 16.884), (44, 17.116), (44, 17)))
        self.add_bezier('sym-e30', (44, 17), ((44, 16.884), (44, 17.116), (44, 17)))
        self.add_bezier('sym-e31', (44, 17), ((44, 12.724), (41.791, 8), (39, 8)))
        self.add_bezier('sym-e32', (39, 8), ((38.927, 8), (39.073, 8), (39, 8)))
        self.add_bezier('sym-e33', (39, 8), ((38.845, 8), (38.164, 8), (38, 8)))
        self.add_bezier('sym-e34', (38, 8), ((36.136, 8), (34.082, 9.585), (33, 12)))
        self.add_bezier('sym-e35', (33, 12), ((32.4, 13.338), (32.318, 15.458), (32, 17)))
        self.add_line('sym-e36', (32, 17), (16, 17))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26')
        self.add_contour('sym-c2', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36')
        self.relate('connect', 'sym-c1', 'sym-c2')
