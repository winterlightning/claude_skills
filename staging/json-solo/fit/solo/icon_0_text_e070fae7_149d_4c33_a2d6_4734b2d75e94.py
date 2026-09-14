"""0 (text) (other), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e070fae7-149d-4c33-a2d6-4734b2d75e94'
SOURCE_PATH = 'icons-json/other/0 (text)_e070fae7-149d-4c33-a2d6-4734b2d75e94.json'
AUTHOR = 'json_to_solo'

class Icon0TextOther(Solo48):
    icon_id = 'icon-0-text-other'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('text', 'other')

    def build(self):
        self.add_line('sym-e0', (8, 24), (8, 24))
        self.add_line('sym-e1', (8, 24), (8, 23))
        self.add_line('sym-e2-1', (8, 23), (9, 16))
        self.add_line('sym-e2-2', (9, 16), (13, 8))
        self.add_arc('sym-e3-1', (13, 8), (18, 5), radius_x=14, sweep=False)
        self.add_arc('sym-e3-2', (18, 5), (23, 4), radius_x=13)
        self.add_line('sym-e4', (23, 4), (24, 4))
        self.add_line('sym-e9', (24, 4), (25, 4))
        self.add_arc('sym-e10-1', (25, 4), (30, 5), radius_x=13)
        self.add_arc('sym-e10-2', (30, 5), (35, 8), radius_x=14, sweep=False)
        self.add_line('sym-e11-1', (35, 8), (39, 16))
        self.add_line('sym-e11-2', (39, 16), (40, 23))
        self.add_line('sym-e12', (40, 23), (40, 24))
        self.add_line('sym-e13', (40, 24), (40, 24))
        self.add_line('sym-e14', (40, 24), (40, 25))
        self.add_line('sym-e15-1', (40, 25), (39, 32))
        self.add_line('sym-e15-2', (39, 32), (35, 40))
        self.add_line('sym-e16-1', (35, 40), (30, 43))
        self.add_arc('sym-e16-2', (30, 43), (25, 44), radius_x=13)
        self.add_line('sym-e17', (25, 44), (24, 44))
        self.add_line('sym-e22', (24, 44), (23, 44))
        self.add_arc('sym-e23-1', (23, 44), (18, 43), radius_x=13)
        self.add_line('sym-e23-2', (18, 43), (13, 40))
        self.add_line('sym-e24-1', (13, 40), (9, 32))
        self.add_line('sym-e24-2', (9, 32), (8, 25))
        self.add_line('sym-e25', (8, 25), (8, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2-1', 'sym-e2-2', 'sym-e3-1', 'sym-e3-2', 'sym-e4', 'sym-e9', 'sym-e10-1', 'sym-e10-2', 'sym-e11-1', 'sym-e11-2', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15-1', 'sym-e15-2', 'sym-e16-1', 'sym-e16-2', 'sym-e17', 'sym-e22', 'sym-e23-1', 'sym-e23-2', 'sym-e24-1', 'sym-e24-2', 'sym-e25', closed=True)
