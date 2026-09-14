"""Water protection drop (ecology), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8b0b36ff-d085-4310-a3d0-47de75b20b4d'
SOURCE_PATH = 'icons-json/ecology/water protection drop_8b0b36ff-d085-4310-a3d0-47de75b20b4d.json'
AUTHOR = 'json_to_solo'

class WaterProtectionDrop(Solo48):
    icon_id = 'water-protection-drop'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'ecology'
    aliases = ()
    keywords = ('water', 'protection', 'drop', 'ecology')

    def build(self):
        self.add_line('sym-e0', (22, 7), (16, 15))
        self.add_bezier('sym-e1', (16, 15), ((13.32, 18.655), (8, 24.482), (8, 29)))
        self.add_bezier('sym-e2', (8, 29), ((8, 29.136), (8, 28.864), (8, 29)))
        self.add_bezier('sym-e3', (8, 29), ((8, 29.309), (8, 29.691), (8, 30)))
        self.add_bezier('sym-e4', (8, 30), ((8, 37.136), (15.25, 44), (23, 44)))
        self.add_bezier('sym-e5', (23, 44), ((23.05, 44), (22.95, 44), (23, 44)))
        self.add_bezier('sym-e6', (23, 44), ((23.187, 44), (23.813, 44), (24, 44)))
        self.add_bezier('sym-e7', (24, 44), ((24.187, 44), (24.813, 44), (25, 44)))
        self.add_bezier('sym-e8', (25, 44), ((25.05, 44), (24.95, 44), (25, 44)))
        self.add_bezier('sym-e9', (25, 44), ((32.75, 44), (40, 37.136), (40, 30)))
        self.add_bezier('sym-e10', (40, 30), ((40, 29.691), (40, 29.309), (40, 29)))
        self.add_bezier('sym-e11', (40, 29), ((40, 28.864), (40, 29.136), (40, 29)))
        self.add_bezier('sym-e12', (40, 29), ((40, 24.482), (34.68, 18.655), (32, 15)))
        self.add_line('sym-e13', (32, 15), (26, 7))
        self.add_line('sym-e14', (26, 7), (24, 4))
        self.add_line('sym-e15', (24, 4), (22, 7))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
