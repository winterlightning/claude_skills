"""Mobile phone control play (state), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0012287-f904-4bd1-be94-369aca27d22a'
SOURCE_PATH = 'icons-json/state/mobile phone control play_d0012287-f904-4bd1-be94-369aca27d22a.json'
AUTHOR = 'json_to_solo'

class MobilePhoneControlPlayState(Solo48):
    icon_id = 'mobile-phone-control-play-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('mobile', 'phone', 'control', 'play', 'state')

    def build(self):
        self.add_line('e0', (40, 36), (8, 36))
        self.add_line('e1', (18, 14), (31, 19))
        self.add_line('e2', (31, 21), (18, 27))
        self.add_line('e3', (17, 27), (17, 14))
        self.add_line('e4', (14, 44), (34, 44))
        self.add_line('e5', (40, 40), (40, 8))
        self.add_line('e6', (35, 4), (13, 4))
        self.add_line('e7', (8, 8), (8, 37))
        self.add_bezier('e8', (31, 19), ((31.126, 19.082), (31.12, 19.618), (31.246, 19.7)), ((31.68, 20.309), (31.354, 20.509), (31, 21)))
        self.add_bezier('e9', (18, 27), ((17.863, 27), (17.966, 26.882), (17.771, 26.882)), ((17.543, 26.882), (17.194, 27), (17, 27)))
        self.add_bezier('e10', (17, 14), ((17.194, 13.991), (17.577, 13.764), (17.771, 13.773)), ((17.909, 13.782), (17.863, 14), (18, 14)))
        self.add_bezier('e11', (8, 37), ((8, 37.482), (8.011, 37.691), (8.011, 38.173)), ((8.011, 40.455), (9.417, 42.773), (12.217, 43.655)), ((12.583, 43.764), (13.063, 43.982), (13.463, 43.982)), ((13.543, 43.982), (13.92, 44), (14, 44)))
        self.add_bezier('e12', (34, 44), ((34.034, 44), (34.366, 43.991), (34.4, 43.991)), ((36.389, 43.991), (39.977, 42.236), (39.977, 40.445)), ((39.989, 40.418), (39.989, 40.027), (40, 40)))
        self.add_bezier('e13', (40, 8), ((39.989, 7.973), (39.989, 7.582), (39.977, 7.555)), ((39.977, 5.864), (37.886, 4.009), (35.714, 4.009)), ((35.623, 4.009), (35.091, 4), (35, 4)))
        self.add_bezier('e14', (13, 4), ((12.966, 4), (12.503, 4.009), (12.469, 4.018)), ((10.366, 4.018), (8, 6.355), (8, 8)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e8', 'e2', 'e9', 'e3', 'e10', closed=True)
        self.add_contour('c2', 'e11', 'e4', 'e12', 'e5', 'e13', 'e6', 'e14', 'e7', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
