"""Microsoft visual studio logo 1 (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2d7127b-4a91-4f1f-9461-fcc33608bdcb'
SOURCE_PATH = 'icons-json/logos/microsoft visual studio logo 1_c2d7127b-4a91-4f1f-9461-fcc33608bdcb.json'
AUTHOR = 'json_to_solo'

class MicrosoftVisualStudioLogo1Logos(Solo48):
    icon_id = 'microsoft-visual-studio-logo-1-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('microsoft', 'visual', 'studio', 'logo', 'logos')

    def build(self):
        self.add_line('sym-e0', (24, 22), (29, 32))
        self.add_arc('sym-e1', (29, 32), (34, 39), radius_x=15, sweep=False)
        self.add_line('sym-e2', (34, 39), (36, 40))
        self.add_arc('sym-e3-1', (36, 40), (42, 35), radius_x=8, sweep=False)
        self.add_line('sym-e3-2', (42, 35), (44, 25))
        self.add_line('sym-e5-1', (44, 25), (44, 24))
        self.add_arc('sym-e5-2', (44, 24), (44, 23), radius_x=28)
        self.add_arc('sym-e6-1', (44, 23), (41, 12), radius_x=22, sweep=False)
        self.add_arc('sym-e6-2', (41, 12), (35, 8), radius_x=7, sweep=False)
        self.add_arc('sym-e8', (35, 8), (29, 13), radius_x=9, sweep=False)
        self.add_line('sym-e9', (29, 13), (25, 20))
        self.add_arc('sym-e10', (25, 20), (24, 22), radius_x=48, sweep=False)
        self.add_line('sym-e11', (24, 22), (19, 32))
        self.add_arc('sym-e12', (19, 32), (14, 39), radius_x=15)
        self.add_line('sym-e13', (14, 39), (12, 40))
        self.add_arc('sym-e14-1', (12, 40), (6, 35), radius_x=8)
        self.add_line('sym-e14-2', (6, 35), (4, 25))
        self.add_line('sym-e16', (4, 25), (4, 23))
        self.add_arc('sym-e17-1', (4, 23), (7, 12), radius_x=22)
        self.add_arc('sym-e17-2', (7, 12), (13, 8), radius_x=7)
        self.add_arc('sym-e19', (13, 8), (19, 13), radius_x=9)
        self.add_arc('sym-e20', (19, 13), (23, 20), radius_x=47)
        self.add_line('sym-e21', (23, 20), (24, 22))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3-1', 'sym-e3-2', 'sym-e5-1', 'sym-e5-2', 'sym-e6-1', 'sym-e6-2', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14-1', 'sym-e14-2', 'sym-e16', 'sym-e17-1', 'sym-e17-2', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
