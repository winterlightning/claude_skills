"""Horizontal (photography), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b9ce706c-0cd4-56ff-81af-2368b477ac76'
SOURCE_PATH = 'icons-json/photography/horizontal_b9ce706c-0cd4-56ff-81af-2368b477ac76.json'
AUTHOR = 'json_to_solo'

class HorizontalPhotography(Solo48):
    icon_id = 'horizontal-photography'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('horizontal', 'photography')

    def build(self):
        self.add_line('e0', (8, 9), (4, 8))
        self.add_line('e1', (4, 8), (4, 40))
        self.add_line('e2', (4, 40), (10, 38))
        self.add_line('e3', (38, 38), (44, 40))
        self.add_line('e4', (44, 40), (44, 8))
        self.add_bezier('e5', (44, 8), ((36.509, 11.274), (29.491, 13.206), (21.555, 12.714)), ((16.782, 12.418), (12.609, 10.563), (8, 9)))
        self.add_bezier('e6', (10, 38), ((11.309, 37.495), (13.055, 36.763), (14.4, 36.455)), ((20.864, 35.003), (27.545, 34.991), (34, 36.542)), ((35.209, 36.825), (36.818, 37.545), (38, 38)))
        self.add_contour('c0', 'e5', 'e0', 'e1', 'e2', 'e6', 'e3', 'e4', closed=True)
