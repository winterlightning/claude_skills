"""Microsoft outlook logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dbcd5360-6234-437a-ae47-ddae4e90f952'
SOURCE_PATH = 'icons-json/logos/microsoft outlook logo_dbcd5360-6234-437a-ae47-ddae4e90f952.json'
AUTHOR = 'json_to_solo'

class MicrosoftOutlookLogoLogos(Solo48):
    icon_id = 'microsoft-outlook-logo-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('microsoft', 'outlook', 'logo', 'logos')

    def build(self):
        self.add_line('sym-e0', (4, 13), (22, 29))
        self.add_bezier('sym-e1', (22, 29), ((22.523, 29.46), (23.352, 30), (24, 30)))
        self.add_bezier('sym-e2', (24, 30), ((24.648, 30), (25.477, 29.46), (26, 29)))
        self.add_line('sym-e3', (26, 29), (44, 13))
        self.add_line('sym-e4', (44, 13), (44, 36))
        self.add_bezier('sym-e5', (44, 36), ((44, 37.4), (43.064, 39.3), (42, 40)))
        self.add_bezier('sym-e6', (42, 40), ((41.782, 40), (41.218, 39.9), (41, 40)))
        self.add_line('sym-e7', (41, 40), (24, 40))
        self.add_line('sym-e8', (24, 40), (7, 40))
        self.add_bezier('sym-e9', (7, 40), ((6.782, 39.9), (6.218, 40), (6, 40)))
        self.add_bezier('sym-e10', (6, 40), ((4.936, 39.3), (4, 37.4), (4, 36)))
        self.add_line('sym-e11', (4, 36), (4, 13))
        self.add_bezier('sym-e12', (4, 13), ((4, 12.78), (4, 12.21), (4, 12)))
        self.add_bezier('sym-e13', (4, 12), ((4, 10.26), (5.273, 8), (7, 8)))
        self.add_bezier('sym-e14', (7, 8), ((7.036, 8), (7.964, 8), (8, 8)))
        self.add_bezier('sym-e15', (8, 8), ((8.027, 8), (7.973, 8), (8, 8)))
        self.add_line('sym-e16', (8, 8), (24, 8))
        self.add_line('sym-e17', (24, 8), (40, 8))
        self.add_bezier('sym-e18', (40, 8), ((40.027, 8), (39.973, 8), (40, 8)))
        self.add_bezier('sym-e19', (40, 8), ((40.036, 8), (40.964, 8), (41, 8)))
        self.add_bezier('sym-e20', (41, 8), ((42.727, 8), (44, 10.26), (44, 12)))
        self.add_bezier('sym-e21', (44, 12), ((44, 12.21), (44, 12.78), (44, 13)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21')
