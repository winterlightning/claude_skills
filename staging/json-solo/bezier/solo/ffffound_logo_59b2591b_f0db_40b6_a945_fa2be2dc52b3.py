"""Ffffound logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59b2591b-f0db-40b6-a945-fa2be2dc52b3'
SOURCE_PATH = 'icons-json/logos/ffffound logo_59b2591b-f0db-40b6-a945-fa2be2dc52b3.json'
AUTHOR = 'json_to_solo'

class FfffoundLogoLogos(Solo48):
    icon_id = 'ffffound-logo-logos'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('ffffound', 'logo', 'logos')

    def build(self):
        self.add_bezier('sym-e0', (24, 11), ((24.216, 10.534), (24.784, 10.467), (25, 10)))
        self.add_bezier('sym-e1', (25, 10), ((25.328, 9.282), (25.554, 7.645), (26, 7)))
        self.add_bezier('sym-e2', (26, 7), ((27.373, 5.018), (29.651, 4), (32, 4)))
        self.add_bezier('sym-e3', (32, 4), ((32.059, 4), (31.941, 4), (32, 4)))
        self.add_bezier('sym-e4', (32, 4), ((32.236, 4), (32.764, 4), (33, 4)))
        self.add_bezier('sym-e5', (33, 4), ((36.621, 4), (40, 7.964), (40, 12)))
        self.add_bezier('sym-e6', (40, 12), ((40, 12.127), (40, 11.873), (40, 12)))
        self.add_bezier('sym-e7', (40, 12), ((40, 12.127), (40, 11.873), (40, 12)))
        self.add_bezier('sym-e8', (40, 12), ((40, 14.9), (38.423, 17.7), (37, 20)))
        self.add_line('sym-e9', (37, 20), (30, 31))
        self.add_bezier('sym-e10', (30, 31), ((28.333, 33.709), (26.204, 37.009), (25, 40)))
        self.add_bezier('sym-e11', (25, 40), ((24.444, 41.382), (24.446, 42.573), (24, 44)))
        self.add_bezier('sym-e12', (24, 44), ((23.554, 42.573), (23.556, 41.382), (23, 40)))
        self.add_bezier('sym-e13', (23, 40), ((21.796, 37.009), (19.667, 33.709), (18, 31)))
        self.add_line('sym-e14', (18, 31), (11, 20))
        self.add_bezier('sym-e15', (11, 20), ((9.577, 17.7), (8, 14.9), (8, 12)))
        self.add_bezier('sym-e16', (8, 12), ((8, 11.873), (8, 12.127), (8, 12)))
        self.add_bezier('sym-e17', (8, 12), ((8, 11.873), (8, 12.127), (8, 12)))
        self.add_bezier('sym-e18', (8, 12), ((8, 7.964), (11.379, 4), (15, 4)))
        self.add_bezier('sym-e19', (15, 4), ((15.236, 4), (15.764, 4), (16, 4)))
        self.add_bezier('sym-e20', (16, 4), ((16.059, 4), (15.941, 4), (16, 4)))
        self.add_bezier('sym-e21', (16, 4), ((18.349, 4), (20.627, 5.018), (22, 7)))
        self.add_bezier('sym-e22', (22, 7), ((22.446, 7.645), (22.672, 9.282), (23, 10)))
        self.add_bezier('sym-e23', (23, 10), ((23.216, 10.467), (23.784, 10.534), (24, 11)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
