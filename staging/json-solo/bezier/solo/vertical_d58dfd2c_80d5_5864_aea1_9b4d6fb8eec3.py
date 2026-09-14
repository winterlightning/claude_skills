"""Vertical (photography), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd58dfd2c-80d5-5864-aea1-9b4d6fb8eec3'
SOURCE_PATH = 'icons-json/photography/vertical_d58dfd2c-80d5-5864-aea1-9b4d6fb8eec3.json'
AUTHOR = 'json_to_solo'

class VerticalPhotography(Solo48):
    icon_id = 'vertical-photography'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('vertical', 'photography')

    def build(self):
        self.add_bezier('sym-e0', (8, 4), ((8.87, 6.455), (9.39, 8.482), (10, 11)))
        self.add_bezier('sym-e1', (10, 11), ((10.987, 15.137), (12, 19.792), (12, 24)))
        self.add_bezier('sym-e2', (12, 24), ((12, 28.208), (10.987, 32.863), (10, 37)))
        self.add_bezier('sym-e3', (10, 37), ((9.39, 39.518), (8.87, 41.545), (8, 44)))
        self.add_line('sym-e4', (8, 44), (24, 44))
        self.add_line('sym-e5', (24, 44), (40, 44))
        self.add_bezier('sym-e6', (40, 44), ((39.13, 41.545), (38.61, 39.518), (38, 37)))
        self.add_bezier('sym-e7', (38, 37), ((37.013, 32.863), (36, 28.208), (36, 24)))
        self.add_bezier('sym-e8', (36, 24), ((36, 19.792), (37.013, 15.137), (38, 11)))
        self.add_bezier('sym-e9', (38, 11), ((38.61, 8.482), (39.13, 6.455), (40, 4)))
        self.add_line('sym-e10', (40, 4), (24, 4))
        self.add_line('sym-e11', (24, 4), (8, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', closed=True)
