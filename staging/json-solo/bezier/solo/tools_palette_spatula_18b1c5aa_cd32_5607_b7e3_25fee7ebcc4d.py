"""Tools palette spatula (tools), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18b1c5aa-cd32-5607-b7e3-25fee7ebcc4d'
SOURCE_PATH = 'icons-json/tools/tools palette spatula_18b1c5aa-cd32-5607-b7e3-25fee7ebcc4d.json'
AUTHOR = 'json_to_solo'

class ToolsPaletteSpatulaTools(Solo48):
    icon_id = 'tools-palette-spatula-tools'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tools'
    aliases = ()
    keywords = ('tools', 'palette', 'spatula')

    def build(self):
        self.add_line('sym-e0', (36, 19), (12, 19))
        self.add_bezier('sym-e1', (24, 44), ((23.87, 43.997), (24.127, 44), (24, 44)))
        self.add_bezier('sym-e2', (24, 44), ((22.893, 44), (20.84, 43.464), (20, 43)))
        self.add_bezier('sym-e3', (20, 43), ((16.973, 41.355), (18.627, 39.318), (19, 37)))
        self.add_line('sym-e4', (19, 37), (20, 29))
        self.add_bezier('sym-e5', (20, 29), ((20.413, 26.5), (16.093, 25.345), (14, 24)))
        self.add_bezier('sym-e6', (14, 24), ((12.333, 22.927), (12.4, 21.464), (12, 20)))
        self.add_line('sym-e7', (12, 20), (8, 6))
        self.add_bezier('sym-e8', (8, 6), ((8, 5.636), (8, 5.364), (8, 5)))
        self.add_bezier('sym-e9', (8, 5), ((8, 4.545), (8.373, 4), (9, 4)))
        self.add_bezier('sym-e10', (9, 4), ((9.187, 4), (9.813, 4.009), (10, 4)))
        self.add_bezier('sym-e11', (10, 4), ((10.773, 4), (11.227, 4), (12, 4)))
        self.add_line('sym-e12', (12, 4), (24, 4))
        self.add_line('sym-e13', (24, 4), (36, 4))
        self.add_bezier('sym-e14', (36, 4), ((36.773, 4), (37.227, 4), (38, 4)))
        self.add_bezier('sym-e15', (38, 4), ((38.187, 4.009), (38.813, 4), (39, 4)))
        self.add_bezier('sym-e16', (39, 4), ((39.627, 4), (40, 4.545), (40, 5)))
        self.add_bezier('sym-e17', (40, 5), ((40, 5.364), (40, 5.636), (40, 6)))
        self.add_line('sym-e18', (40, 6), (36, 20))
        self.add_bezier('sym-e19', (36, 20), ((35.6, 21.464), (35.667, 22.927), (34, 24)))
        self.add_bezier('sym-e20', (34, 24), ((31.907, 25.345), (27.587, 26.5), (28, 29)))
        self.add_line('sym-e21', (28, 29), (29, 37))
        self.add_bezier('sym-e22', (29, 37), ((29.373, 39.318), (31.027, 41.355), (28, 43)))
        self.add_bezier('sym-e23', (28, 43), ((27.16, 43.464), (25.107, 44), (24, 44)))
        self.add_bezier('sym-e24', (24, 44), ((23.873, 44), (24.13, 43.997), (24, 44)))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
