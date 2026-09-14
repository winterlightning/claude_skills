"""D (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e1', (24, 44), ((24.97, 44), (26.07, 43.264), (27, 43)))
        self.add_bezier('sym-e2', (27, 43), ((32.76, 41.364), (37.31, 37.309), (39, 32)))
        self.add_bezier('sym-e3', (39, 32), ((39.33, 30.964), (40, 30.082), (40, 29)))
        self.add_bezier('sym-e4', (40, 29), ((40, 28.927), (40, 29.073), (40, 29)))
        self.add_bezier('sym-e5', (40, 29), ((40, 28.627), (40, 28.364), (40, 28)))
        self.add_line('sym-e6', (40, 28), (40, 24))
        self.add_line('sym-e7', (40, 24), (40, 20))
        self.add_bezier('sym-e8', (40, 20), ((40, 19.636), (40, 19.373), (40, 19)))
        self.add_bezier('sym-e9', (40, 19), ((40, 18.927), (40, 19.073), (40, 19)))
        self.add_bezier('sym-e10', (40, 19), ((40, 17.918), (39.33, 17.036), (39, 16)))
        self.add_bezier('sym-e11', (39, 16), ((37.31, 10.691), (32.76, 6.636), (27, 5)))
        self.add_bezier('sym-e12', (27, 5), ((26.07, 4.736), (24.97, 4), (24, 4)))
        self.add_line('sym-e13', (24, 4), (8, 4))
        self.add_line('sym-e14', (8, 4), (8, 24))
        self.add_line('sym-e15', (8, 24), (8, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
