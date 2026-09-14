"""Oculus logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '12bd1899-000c-4b67-950e-b0cf9be91bc2'
SOURCE_PATH = 'icons-json/logos/oculus logo_12bd1899-000c-4b67-950e-b0cf9be91bc2.json'
AUTHOR = 'json_to_solo'

class OculusLogoLogos(Solo48):
    icon_id = 'oculus-logo-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('oculus', 'logo', 'logos')

    def build(self):
        self.add_line('sym-e0', (35, 40), (24, 40))
        self.add_line('sym-e1', (24, 40), (13, 40))
        self.add_bezier('sym-e2', (13, 40), ((12.264, 40), (11.682, 39.345), (11, 39)))
        self.add_bezier('sym-e3', (11, 39), ((6.755, 36.846), (4, 30.969), (4, 25)))
        self.add_bezier('sym-e4', (4, 25), ((4, 24.705), (4, 24.295), (4, 24)))
        self.add_bezier('sym-e5', (4, 24), ((4, 23.902), (4, 23.098), (4, 23)))
        self.add_bezier('sym-e6', (4, 23), ((4, 16.982), (6.718, 11.154), (11, 9)))
        self.add_bezier('sym-e7', (11, 9), ((11.618, 8.692), (12.336, 8), (13, 8)))
        self.add_bezier('sym-e8', (13, 8), ((13.064, 8), (12.936, 8.012), (13, 8)))
        self.add_line('sym-e9', (13, 8), (24, 8))
        self.add_line('sym-e10', (24, 8), (35, 8))
        self.add_bezier('sym-e11', (35, 8), ((35.064, 8.012), (34.936, 8), (35, 8)))
        self.add_bezier('sym-e12', (35, 8), ((35.664, 8), (36.382, 8.692), (37, 9)))
        self.add_bezier('sym-e13', (37, 9), ((41.282, 11.154), (44, 16.982), (44, 23)))
        self.add_bezier('sym-e14', (44, 23), ((44, 23.098), (44, 23.902), (44, 24)))
        self.add_bezier('sym-e15', (44, 24), ((44, 24.295), (44, 24.705), (44, 25)))
        self.add_bezier('sym-e16', (44, 25), ((44, 30.969), (41.245, 36.846), (37, 39)))
        self.add_bezier('sym-e17', (37, 39), ((36.318, 39.345), (35.736, 40), (35, 40)))
        self.add_line('sym-e18', (33, 19), (24, 19))
        self.add_line('sym-e19', (24, 19), (15, 19))
        self.add_bezier('sym-e20', (15, 19), ((13.536, 19.689), (12.264, 20.822), (12, 23)))
        self.add_bezier('sym-e21', (12, 23), ((11.727, 25.228), (13.073, 29), (15, 29)))
        self.add_line('sym-e22', (15, 29), (24, 29))
        self.add_line('sym-e23', (24, 29), (33, 29))
        self.add_bezier('sym-e24', (33, 29), ((34.927, 29), (36.273, 25.228), (36, 23)))
        self.add_bezier('sym-e25', (36, 23), ((35.736, 20.822), (34.464, 19.689), (33, 19)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
        self.add_contour('sym-c1', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
