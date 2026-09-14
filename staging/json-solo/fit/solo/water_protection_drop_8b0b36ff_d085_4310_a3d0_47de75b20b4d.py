"""Water protection drop (ecology), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8b0b36ff-d085-4310-a3d0-47de75b20b4d'
SOURCE_PATH = 'icons-json/ecology/water protection drop_8b0b36ff-d085-4310-a3d0-47de75b20b4d.json'
AUTHOR = 'json_to_solo'

class WaterProtectionDropEcology(Solo48):
    icon_id = 'water-protection-drop-ecology'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'ecology'
    aliases = ()
    keywords = ('water', 'protection', 'drop', 'ecology')

    def build(self):
        self.add_line('sym-e0', (22, 7), (16, 15))
        self.add_arc('sym-e1', (16, 15), (8, 29), radius_x=31, sweep=False)
        self.add_line('sym-e3', (8, 29), (8, 30))
        self.add_arc('sym-e4', (8, 30), (23, 44), radius_x=16, sweep=False)
        self.add_line('sym-e6', (23, 44), (24, 44))
        self.add_arc('sym-e7', (24, 44), (25, 44), radius_x=29)
        self.add_arc('sym-e9', (25, 44), (40, 30), radius_x=16, sweep=False)
        self.add_line('sym-e10', (40, 30), (40, 29))
        self.add_arc('sym-e12', (40, 29), (32, 15), radius_x=31, sweep=False)
        self.add_line('sym-e13', (32, 15), (26, 7))
        self.add_line('sym-e14', (26, 7), (24, 4))
        self.add_line('sym-e15', (24, 4), (22, 7))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
