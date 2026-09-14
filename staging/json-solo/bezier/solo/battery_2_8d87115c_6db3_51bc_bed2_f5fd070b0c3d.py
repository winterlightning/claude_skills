"""Battery 2 (photography), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d87115c-6db3-51bc-bed2-f5fd070b0c3d'
SOURCE_PATH = 'icons-json/photography/battery 2_8d87115c-6db3-51bc-bed2-f5fd070b0c3d.json'
AUTHOR = 'json_to_solo'

class Battery2Photography(Solo48):
    icon_id = 'battery-2-photography'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('battery', 'photography')

    def build(self):
        self.add_line('sym-e0', (40, 27), (8, 27))
        self.add_line('sym-e1', (8, 27), (8, 9))
        self.add_bezier('sym-e2', (8, 9), ((8, 6.818), (12.129, 8.009), (14, 8)))
        self.add_bezier('sym-e3', (14, 8), ((14.222, 8), (13.778, 8), (14, 8)))
        self.add_bezier('sym-e4', (14, 8), ((14.111, 7.927), (13.988, 6.145), (14, 6)))
        self.add_bezier('sym-e5', (14, 6), ((14.025, 4.691), (14.785, 4), (17, 4)))
        self.add_bezier('sym-e6', (17, 4), ((17.357, 4), (17.643, 4), (18, 4)))
        self.add_line('sym-e7', (18, 4), (24, 4))
        self.add_line('sym-e8', (24, 4), (30, 4))
        self.add_bezier('sym-e9', (30, 4), ((30.357, 4), (30.643, 4), (31, 4)))
        self.add_bezier('sym-e10', (31, 4), ((33.215, 4), (33.975, 4.691), (34, 6)))
        self.add_bezier('sym-e11', (34, 6), ((34.012, 6.145), (33.889, 7.927), (34, 8)))
        self.add_bezier('sym-e12', (34, 8), ((34.222, 8), (33.778, 8), (34, 8)))
        self.add_bezier('sym-e13', (34, 8), ((35.871, 8.009), (40, 6.818), (40, 9)))
        self.add_line('sym-e14', (40, 9), (40, 27))
        self.add_line('sym-e15', (40, 27), (40, 41))
        self.add_bezier('sym-e16', (40, 41), ((40, 41.082), (40, 41.918), (40, 42)))
        self.add_bezier('sym-e17', (40, 42), ((40, 43.309), (37.662, 44), (36, 44)))
        self.add_line('sym-e18', (36, 44), (24, 44))
        self.add_line('sym-e19', (24, 44), (12, 44))
        self.add_bezier('sym-e20', (12, 44), ((10.338, 44), (8, 43.309), (8, 42)))
        self.add_bezier('sym-e21', (8, 42), ((8, 41.918), (8, 41.082), (8, 41)))
        self.add_line('sym-e22', (8, 41), (8, 27))
        self.add_line('sym-e23', (24, 11), (24, 20))
        self.add_line('sym-e24', (18, 16), (30, 16))
        self.add_line('sym-e25', (19, 35), (29, 35))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22')
        self.add_contour('sym-c1', 'sym-e23')
        self.add_contour('sym-c2', 'sym-e24')
        self.add_contour('sym-c3', 'sym-e25')
