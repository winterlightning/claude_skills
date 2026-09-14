"""Kickstarter logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94e0f013-4f57-4c6b-8b28-449bba9c98f1'
SOURCE_PATH = 'icons-json/logos/kickstarter logo_94e0f013-4f57-4c6b-8b28-449bba9c98f1.json'
AUTHOR = 'json_to_solo'

class KickstarterLogoLogos(Solo48):
    icon_id = 'kickstarter-logo-logos'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('kickstarter', 'logo', 'logos')

    def build(self):
        self.add_line('sym-e0', (32, 24), (37, 30))
        self.add_bezier('sym-e1', (37, 30), ((38.128, 31.218), (40, 34.245), (40, 36)))
        self.add_bezier('sym-e2', (40, 36), ((40, 36.091), (40, 35.918), (40, 36)))
        self.add_bezier('sym-e3', (40, 36), ((40, 36.091), (40, 36.918), (40, 37)))
        self.add_bezier('sym-e4', (40, 37), ((40, 39.936), (36.804, 44), (34, 44)))
        self.add_bezier('sym-e5', (34, 44), ((33.924, 44), (34.076, 44), (34, 44)))
        self.add_bezier('sym-e6', (34, 44), ((33.848, 44), (33.143, 44), (33, 44)))
        self.add_bezier('sym-e7', (33, 44), ((31.257, 44), (29.238, 42.182), (28, 41)))
        self.add_line('sym-e8', (28, 41), (21, 34))
        self.add_bezier('sym-e9', (21, 34), ((21.025, 37.227), (21.107, 41.091), (18, 43)))
        self.add_bezier('sym-e10', (18, 43), ((17.107, 43.545), (16.027, 44), (15, 44)))
        self.add_bezier('sym-e11', (15, 44), ((14.924, 44), (15.076, 44), (15, 44)))
        self.add_bezier('sym-e12', (15, 44), ((14.848, 44), (15.152, 44), (15, 44)))
        self.add_bezier('sym-e13', (15, 44), ((12.373, 44), (9.011, 42.627), (8, 40)))
        self.add_bezier('sym-e14', (8, 40), ((8, 39.482), (8, 38.573), (8, 38)))
        self.add_bezier('sym-e15', (8, 38), ((8, 37.918), (8, 38.082), (8, 38)))
        self.add_line('sym-e16', (8, 38), (8, 24))
        self.add_line('sym-e17', (8, 24), (8, 10))
        self.add_bezier('sym-e18', (8, 10), ((8, 9.918), (8, 10.082), (8, 10)))
        self.add_bezier('sym-e19', (8, 10), ((8, 9.427), (8, 8.518), (8, 8)))
        self.add_bezier('sym-e20', (8, 8), ((9.011, 5.373), (12.373, 4), (15, 4)))
        self.add_bezier('sym-e21', (15, 4), ((15.152, 4), (14.848, 4), (15, 4)))
        self.add_bezier('sym-e22', (15, 4), ((15.076, 4), (14.924, 4), (15, 4)))
        self.add_bezier('sym-e23', (15, 4), ((16.027, 4), (17.107, 4.455), (18, 5)))
        self.add_bezier('sym-e24', (18, 5), ((21.107, 6.909), (21.025, 10.773), (21, 14)))
        self.add_line('sym-e25', (21, 14), (28, 7))
        self.add_bezier('sym-e26', (28, 7), ((29.238, 5.818), (31.257, 4), (33, 4)))
        self.add_bezier('sym-e27', (33, 4), ((33.143, 4), (33.848, 4), (34, 4)))
        self.add_bezier('sym-e28', (34, 4), ((34.076, 4), (33.924, 4), (34, 4)))
        self.add_bezier('sym-e29', (34, 4), ((36.804, 4), (40, 8.064), (40, 11)))
        self.add_bezier('sym-e30', (40, 11), ((40, 11.082), (40, 11.909), (40, 12)))
        self.add_bezier('sym-e31', (40, 12), ((40, 12.082), (40, 11.909), (40, 12)))
        self.add_bezier('sym-e32', (40, 12), ((40, 13.755), (38.128, 16.782), (37, 18)))
        self.add_line('sym-e33', (37, 18), (32, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', closed=True)
