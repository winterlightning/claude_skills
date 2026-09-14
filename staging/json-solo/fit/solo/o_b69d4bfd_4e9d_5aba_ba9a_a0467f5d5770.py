"""O (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('sym-e1-1', (8, 33), (12, 40), radius_x=9, sweep=False)
        self.add_arc('sym-e1-2', (12, 40), (23, 44), radius_x=18, sweep=False)
        self.add_line('sym-e2', (23, 44), (24, 44))
        self.add_line('sym-e7', (24, 44), (25, 44))
        self.add_arc('sym-e8-1', (25, 44), (36, 40), radius_x=18, sweep=False)
        self.add_arc('sym-e8-2', (36, 40), (40, 33), radius_x=9, sweep=False)
        self.add_line('sym-e10', (40, 33), (40, 24))
        self.add_line('sym-e11', (40, 24), (40, 15))
        self.add_arc('sym-e13-1', (40, 15), (36, 8), radius_x=9, sweep=False)
        self.add_arc('sym-e13-2', (36, 8), (25, 4), radius_x=18, sweep=False)
        self.add_line('sym-e14', (25, 4), (24, 4))
        self.add_line('sym-e19', (24, 4), (23, 4))
        self.add_arc('sym-e20-1', (23, 4), (12, 8), radius_x=18, sweep=False)
        self.add_arc('sym-e20-2', (12, 8), (8, 15), radius_x=9, sweep=False)
        self.add_line('sym-e22', (8, 15), (8, 24))
        self.add_line('sym-e23', (8, 24), (8, 33))
        self.add_contour('sym-c0', 'sym-e1-1', 'sym-e1-2', 'sym-e2', 'sym-e7', 'sym-e8-1', 'sym-e8-2', 'sym-e10', 'sym-e11', 'sym-e13-1', 'sym-e13-2', 'sym-e14', 'sym-e19', 'sym-e20-1', 'sym-e20-2', 'sym-e22', 'sym-e23', closed=True)
