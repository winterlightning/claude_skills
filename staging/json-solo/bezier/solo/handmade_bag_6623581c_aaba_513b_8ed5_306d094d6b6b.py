"""Handmade bag (hobbies), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6623581c-aaba-513b-8ed5-306d094d6b6b'
SOURCE_PATH = 'icons-json/hobbies/handmade bag_6623581c-aaba-513b-8ed5-306d094d6b6b.json'
AUTHOR = 'json_to_solo'

class HandmadeBagHobbies(Solo48):
    icon_id = 'handmade-bag-hobbies'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    aliases = ()
    keywords = ('handmade', 'bag', 'hobbies')

    def build(self):
        self.add_line('sym-e0', (15, 23), (15, 13))
        self.add_bezier('sym-e1', (15, 13), ((15, 12.804), (15.894, 12.254), (16, 12)))
        self.add_bezier('sym-e2', (16, 12), ((17.285, 8.842), (19.474, 6), (23, 6)))
        self.add_bezier('sym-e3', (23, 6), ((23.131, 6), (23.877, 6), (24, 6)))
        self.add_bezier('sym-e4', (24, 6), ((24.044, 6), (23.956, 6), (24, 6)))
        self.add_bezier('sym-e5', (24, 6), ((24.044, 6), (23.956, 6), (24, 6)))
        self.add_bezier('sym-e6', (24, 6), ((24.123, 6), (24.869, 6), (25, 6)))
        self.add_bezier('sym-e7', (25, 6), ((28.526, 6), (30.715, 8.842), (32, 12)))
        self.add_bezier('sym-e8', (32, 12), ((32.106, 12.254), (33, 12.804), (33, 13)))
        self.add_line('sym-e9', (33, 13), (33, 23))
        self.add_line('sym-e10', (9, 18), (24, 18))
        self.add_line('sym-e11', (24, 18), (39, 18))
        self.add_bezier('sym-e12', (39, 18), ((39.638, 18.36), (39.91, 19.141), (40, 20)))
        self.add_line('sym-e13', (40, 20), (42, 35))
        self.add_bezier('sym-e14', (42, 35), ((42, 35.916), (42, 37.092), (42, 38)))
        self.add_bezier('sym-e15', (42, 38), ((42, 38.335), (42, 38.714), (42, 39)))
        self.add_bezier('sym-e16', (42, 39), ((41.092, 40.726), (38.906, 42), (37, 42)))
        self.add_bezier('sym-e17', (37, 42), ((36.861, 42), (36.139, 42), (36, 42)))
        self.add_line('sym-e18', (36, 42), (24, 42))
        self.add_line('sym-e19', (24, 42), (12, 42))
        self.add_bezier('sym-e20', (12, 42), ((11.861, 42), (11.139, 42), (11, 42)))
        self.add_bezier('sym-e21', (11, 42), ((9.094, 42), (6.908, 40.726), (6, 39)))
        self.add_bezier('sym-e22', (6, 39), ((6, 38.714), (6, 38.335), (6, 38)))
        self.add_bezier('sym-e23', (6, 38), ((6, 37.092), (6, 35.916), (6, 35)))
        self.add_line('sym-e24', (6, 35), (8, 20))
        self.add_bezier('sym-e25', (8, 20), ((8.09, 19.141), (8.362, 18.36), (9, 18)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c1', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
