"""Microsoft outlook logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('sym-e1', (22, 29), (24, 30), radius_x=3)
        self.add_arc('sym-e2', (24, 30), (26, 29), radius_x=3)
        self.add_line('sym-e3', (26, 29), (44, 13))
        self.add_line('sym-e4', (44, 13), (44, 36))
        self.add_arc('sym-e5', (44, 36), (42, 40), radius_x=6)
        self.add_line('sym-e6', (42, 40), (41, 40))
        self.add_line('sym-e7', (41, 40), (24, 40))
        self.add_line('sym-e8', (24, 40), (7, 40))
        self.add_arc('sym-e9', (7, 40), (6, 40), radius_x=1, sweep=False)
        self.add_arc('sym-e10', (6, 40), (4, 36), radius_x=6)
        self.add_line('sym-e11', (4, 36), (4, 13))
        self.add_line('sym-e12', (4, 13), (4, 12))
        self.add_arc('sym-e13', (4, 12), (7, 8), radius_x=5)
        self.add_arc('sym-e14', (7, 8), (8, 8), radius_x=8, sweep=False)
        self.add_line('sym-e16', (8, 8), (24, 8))
        self.add_line('sym-e17', (24, 8), (40, 8))
        self.add_line('sym-e19', (40, 8), (41, 8))
        self.add_arc('sym-e20', (41, 8), (44, 12), radius_x=5)
        self.add_arc('sym-e21', (44, 12), (44, 13), radius_x=1, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e16', 'sym-e17', 'sym-e19', 'sym-e20', 'sym-e21')
