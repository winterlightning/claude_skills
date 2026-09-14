"""Email logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aef6da05-b81c-4b53-95f9-6548945f3eb6'
SOURCE_PATH = 'icons-json/logos/email logo_aef6da05-b81c-4b53-95f9-6548945f3eb6.json'
AUTHOR = 'json_to_solo'

class EmailLogo(Solo48):
    icon_id = 'email-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('email', 'logo', 'logos')

    def build(self):
        self.add_line('sym-e0', (24, 8), (41, 8))
        self.add_arc('sym-e2', (41, 8), (44, 10), radius_x=4)
        self.add_arc('sym-e3', (44, 10), (44, 11), radius_x=23, sweep=False)
        self.add_line('sym-e4', (44, 11), (24, 26))
        self.add_line('sym-e5', (24, 26), (4, 11))
        self.add_line('sym-e6', (4, 11), (4, 10))
        self.add_arc('sym-e7', (4, 10), (7, 8), radius_x=4)
        self.add_line('sym-e9', (7, 8), (24, 8))
        self.add_line('sym-e10', (24, 40), (41, 40))
        self.add_arc('sym-e11', (41, 40), (44, 37), radius_x=3, sweep=False)
        self.add_line('sym-e12', (44, 37), (44, 11))
        self.add_line('sym-e13', (24, 40), (7, 40))
        self.add_arc('sym-e14', (7, 40), (4, 37), radius_x=3)
        self.add_line('sym-e15', (4, 37), (4, 11))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e9', closed=True)
        self.add_contour('sym-c1', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c2', 'sym-e13', 'sym-e14', 'sym-e15')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
