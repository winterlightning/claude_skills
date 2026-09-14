"""Androiddauto logo (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '71152ade-b3e4-473c-81ba-42eb4346c810'
SOURCE_PATH = 'icons-json/_uncategorized_03/androiddauto logo_71152ade-b3e4-473c-81ba-42eb4346c810.json'
AUTHOR = 'json_to_solo'

class AndroiddautoLogo(Solo48):
    icon_id = 'androiddauto-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('androiddauto', 'logo', '_uncategorized_03')

    def build(self):
        self.add_arc('sym-e1', (24, 4), (26, 5), radius_x=3)
        self.add_line('sym-e2', (26, 5), (40, 29))
        self.add_line('sym-e3', (40, 29), (40, 30))
        self.add_arc('sym-e6', (40, 30), (40, 31), radius_x=32, sweep=False)
        self.add_arc('sym-e7', (40, 31), (38, 32), radius_x=2)
        self.add_line('sym-e8', (38, 32), (30, 31))
        self.add_line('sym-e9', (30, 31), (35, 41))
        self.add_arc('sym-e10', (35, 41), (33, 44), radius_x=3)
        self.add_line('sym-e11', (33, 44), (24, 44))
        self.add_line('sym-e12', (24, 44), (15, 44))
        self.add_arc('sym-e13', (15, 44), (13, 41), radius_x=3)
        self.add_line('sym-e14', (13, 41), (18, 31))
        self.add_line('sym-e15', (18, 31), (10, 32))
        self.add_arc('sym-e16', (10, 32), (8, 31), radius_x=2)
        self.add_line('sym-e17', (8, 31), (8, 30))
        self.add_line('sym-e20', (8, 30), (8, 29))
        self.add_line('sym-e21', (8, 29), (22, 5))
        self.add_arc('sym-e22', (22, 5), (24, 4), radius_x=3)
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e20', 'sym-e21', 'sym-e22', closed=True)
