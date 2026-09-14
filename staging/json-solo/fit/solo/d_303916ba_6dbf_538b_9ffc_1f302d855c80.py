"""D (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '303916ba-6dbf-538b-9ffc-1f302d855c80'
SOURCE_PATH = 'icons-json/typeface/D_303916ba-6dbf-538b-9ffc-1f302d855c80.json'
AUTHOR = 'json_to_solo'

class D303916ba(Solo48):
    icon_id = 'd-303916ba'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('d', 'typeface')

    def build(self):
        self.add_line('sym-e0', (8, 44), (24, 44))
        self.add_arc('sym-e1', (24, 44), (27, 43), radius_x=11, sweep=False)
        self.add_arc('sym-e2', (27, 43), (39, 32), radius_x=17, sweep=False)
        self.add_arc('sym-e3', (39, 32), (40, 29), radius_x=10, sweep=False)
        self.add_line('sym-e5', (40, 29), (40, 28))
        self.add_line('sym-e6', (40, 28), (40, 24))
        self.add_line('sym-e7', (40, 24), (40, 20))
        self.add_line('sym-e8', (40, 20), (40, 19))
        self.add_arc('sym-e10', (40, 19), (39, 16), radius_x=10, sweep=False)
        self.add_arc('sym-e11', (39, 16), (27, 5), radius_x=17, sweep=False)
        self.add_arc('sym-e12', (27, 5), (24, 4), radius_x=11, sweep=False)
        self.add_line('sym-e13', (24, 4), (8, 4))
        self.add_line('sym-e14', (8, 4), (8, 24))
        self.add_line('sym-e15', (8, 24), (8, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
