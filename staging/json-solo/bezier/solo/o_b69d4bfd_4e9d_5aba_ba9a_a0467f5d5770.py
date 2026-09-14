"""O (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b69d4bfd-4e9d-5aba-ba9a-a0467f5d5770'
SOURCE_PATH = 'icons-json/typeface/O_b69d4bfd-4e9d-5aba-ba9a-a0467f5d5770.json'
AUTHOR = 'json_to_solo'

class OB69d4bfd(Solo48):
    icon_id = 'o-b69d4bfd'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('o', 'typeface')

    def build(self):
        self.add_bezier('sym-e0', (8, 33), ((8, 33), (8, 33), (8, 33)))
        self.add_bezier('sym-e1', (8, 33), ((8, 38.8), (15.283, 44), (23, 44)))
        self.add_bezier('sym-e2', (23, 44), ((23.197, 44), (23.791, 43.991), (24, 44)))
        self.add_bezier('sym-e3', (24, 44), ((24.043, 44), (23.956, 44), (24, 44)))
        self.add_bezier('sym-e4', (24, 44), ((24.022, 44), (23.978, 44), (24, 44)))
        self.add_bezier('sym-e5', (24, 44), ((24.022, 44), (23.978, 44), (24, 44)))
        self.add_bezier('sym-e6', (24, 44), ((24.044, 44), (23.957, 44), (24, 44)))
        self.add_bezier('sym-e7', (24, 44), ((24.209, 43.991), (24.803, 44), (25, 44)))
        self.add_bezier('sym-e8', (25, 44), ((32.717, 44), (40, 38.8), (40, 33)))
        self.add_bezier('sym-e9', (40, 33), ((40, 33), (40, 33), (40, 33)))
        self.add_line('sym-e10', (40, 33), (40, 24))
        self.add_line('sym-e11', (40, 24), (40, 15))
        self.add_bezier('sym-e12', (40, 15), ((40, 15), (40, 15), (40, 15)))
        self.add_bezier('sym-e13', (40, 15), ((40, 9.2), (32.717, 4), (25, 4)))
        self.add_bezier('sym-e14', (25, 4), ((24.803, 4), (24.209, 4.009), (24, 4)))
        self.add_bezier('sym-e15', (24, 4), ((23.957, 4), (24.044, 4), (24, 4)))
        self.add_bezier('sym-e16', (24, 4), ((23.978, 4), (24.022, 4), (24, 4)))
        self.add_bezier('sym-e17', (24, 4), ((23.978, 4), (24.022, 4), (24, 4)))
        self.add_bezier('sym-e18', (24, 4), ((23.956, 4), (24.043, 4), (24, 4)))
        self.add_bezier('sym-e19', (24, 4), ((23.791, 4.009), (23.197, 4), (23, 4)))
        self.add_bezier('sym-e20', (23, 4), ((15.283, 4), (8, 9.2), (8, 15)))
        self.add_bezier('sym-e21', (8, 15), ((8, 15), (8, 15), (8, 15)))
        self.add_line('sym-e22', (8, 15), (8, 24))
        self.add_line('sym-e23', (8, 24), (8, 33))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
