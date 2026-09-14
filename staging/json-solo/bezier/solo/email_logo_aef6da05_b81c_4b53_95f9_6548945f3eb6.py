"""Email logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aef6da05-b81c-4b53-95f9-6548945f3eb6'
SOURCE_PATH = 'icons-json/logos/email logo_aef6da05-b81c-4b53-95f9-6548945f3eb6.json'
AUTHOR = 'json_to_solo'

class EmailLogoLogos(Solo48):
    icon_id = 'email-logo-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('email', 'logo', 'logos')

    def build(self):
        self.add_line('sym-e0', (24, 8), (41, 8))
        self.add_bezier('sym-e1', (41, 8), ((41.055, 8), (40.945, 8), (41, 8)))
        self.add_bezier('sym-e2', (41, 8), ((41.855, 8), (44, 9.116), (44, 10)))
        self.add_bezier('sym-e3', (44, 10), ((44, 10.118), (44, 10.882), (44, 11)))
        self.add_line('sym-e4', (44, 11), (24, 26))
        self.add_line('sym-e5', (24, 26), (4, 11))
        self.add_bezier('sym-e6', (4, 11), ((4, 10.882), (4, 10.118), (4, 10)))
        self.add_bezier('sym-e7', (4, 10), ((4, 9.116), (6.145, 8), (7, 8)))
        self.add_bezier('sym-e8', (7, 8), ((7.055, 8), (6.945, 8), (7, 8)))
        self.add_line('sym-e9', (7, 8), (24, 8))
        self.add_line('sym-e10', (24, 40), (41, 40))
        self.add_bezier('sym-e11', (41, 40), ((42.018, 40), (44, 37.918), (44, 37)))
        self.add_line('sym-e12', (44, 37), (44, 11))
        self.add_line('sym-e13', (24, 40), (7, 40))
        self.add_bezier('sym-e14', (7, 40), ((5.982, 40), (4, 37.918), (4, 37)))
        self.add_line('sym-e15', (4, 37), (4, 11))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', closed=True)
        self.add_contour('sym-c1', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c2', 'sym-e13', 'sym-e14', 'sym-e15')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
