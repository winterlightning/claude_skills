"""Battery 2 (photography), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d87115c-6db3-51bc-bed2-f5fd070b0c3d'
SOURCE_PATH = 'icons-json/photography/battery 2_8d87115c-6db3-51bc-bed2-f5fd070b0c3d.json'
AUTHOR = 'json_to_solo'

class Battery2(Solo48):
    icon_id = 'battery-2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('battery', 'photography')

    def build(self):
        self.add_line('sym-e0', (40, 27), (8, 27))
        self.add_line('sym-e1', (8, 27), (8, 9))
        self.add_arc('sym-e2', (8, 9), (14, 8), radius_x=4)
        self.add_arc('sym-e4', (14, 8), (14, 6), radius_x=3)
        self.add_line('sym-e5', (14, 6), (17, 4))
        self.add_line('sym-e6', (17, 4), (18, 4))
        self.add_line('sym-e7', (18, 4), (24, 4))
        self.add_line('sym-e8', (24, 4), (30, 4))
        self.add_line('sym-e9', (30, 4), (31, 4))
        self.add_line('sym-e10', (31, 4), (34, 6))
        self.add_arc('sym-e11', (34, 6), (34, 8), radius_x=3)
        self.add_arc('sym-e13', (34, 8), (40, 9), radius_x=4)
        self.add_line('sym-e14', (40, 9), (40, 27))
        self.add_line('sym-e15', (40, 27), (40, 41))
        self.add_arc('sym-e16', (40, 41), (40, 42), radius_x=41, sweep=False)
        self.add_line('sym-e17', (40, 42), (36, 44))
        self.add_line('sym-e18', (36, 44), (24, 44))
        self.add_line('sym-e19', (24, 44), (12, 44))
        self.add_line('sym-e20', (12, 44), (8, 42))
        self.add_line('sym-e21', (8, 42), (8, 41))
        self.add_line('sym-e22', (8, 41), (8, 27))
        self.add_line('sym-e23', (24, 11), (24, 20))
        self.add_line('sym-e24', (18, 16), (30, 16))
        self.add_line('sym-e25', (19, 35), (29, 35))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22')
        self.add_contour('sym-c1', 'sym-e23')
        self.add_contour('sym-c2', 'sym-e24')
        self.add_contour('sym-c3', 'sym-e25')
