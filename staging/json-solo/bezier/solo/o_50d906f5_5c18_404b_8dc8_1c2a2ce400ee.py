"""O (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50d906f5-5c18-404b-8dc8-1c2a2ce400ee'
SOURCE_PATH = 'icons-json/typeface/o_50d906f5-5c18-404b-8dc8-1c2a2ce400ee.json'
AUTHOR = 'json_to_solo'

class O(Solo48):
    icon_id = 'o'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('o', 'typeface')

    def build(self):
        self.add_bezier('sym-e0', (24, 44), ((24.194, 44), (24.806, 44), (25, 44)))
        self.add_bezier('sym-e1', (25, 44), ((35.072, 44), (40, 34.982), (40, 25)))
        self.add_bezier('sym-e2', (40, 25), ((40, 24.724), (39.999, 24.276), (40, 24)))
        self.add_bezier('sym-e3', (40, 24), ((39.999, 23.724), (40, 23.276), (40, 23)))
        self.add_bezier('sym-e4', (40, 23), ((40, 13.018), (35.072, 4), (25, 4)))
        self.add_bezier('sym-e5', (25, 4), ((24.806, 4), (24.194, 4), (24, 4)))
        self.add_bezier('sym-e6', (24, 4), ((23.806, 4), (23.194, 4), (23, 4)))
        self.add_bezier('sym-e7', (23, 4), ((12.928, 4), (8, 13.018), (8, 23)))
        self.add_bezier('sym-e8', (8, 23), ((8, 23.276), (8.001, 23.724), (8, 24)))
        self.add_bezier('sym-e9', (8, 24), ((8.001, 24.276), (8, 24.724), (8, 25)))
        self.add_bezier('sym-e10', (8, 25), ((8, 34.982), (12.928, 44), (23, 44)))
        self.add_bezier('sym-e11', (23, 44), ((23.194, 44), (23.806, 44), (24, 44)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', closed=True)
