"""Microsoft visual studio logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f23c1fcf-345a-4ef4-b844-ecdca619586a'
SOURCE_PATH = 'pictographic-primitives/logos/microsoft visual studio logo_f23c1fcf-345a-4ef4-b844-ecdca619586a.svg'
AUTHOR = 'gpt-6'

class MicrosoftVisualStudioLogo(Solo48):
    icon_id = 'microsoft-visual-studio-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('microsoft', 'visual', 'studio', 'logo', 'logos')

    def build(self):
        self.add_line('sym-e0', (24, 24), (39, 40))
        self.add_line('sym-e1', (39, 40), (40, 40))
        self.add_arc('sym-e2', (40, 40), (41, 40), radius_x=40, radius_y=40, large_arc=False, sweep=True)
        self.add_line('sym-e5', (41, 40), (44, 37))
        self.add_line('sym-e6', (44, 37), (44, 12))
        self.add_arc('sym-e8', (44, 12), (44, 11), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('sym-e9', (44, 11), (43, 10), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e10', (43, 10), (41, 8))
        self.add_line('sym-e12', (41, 8), (39, 8))
        self.add_line('sym-e15', (39, 8), (9, 40))
        self.add_arc('sym-e17', (9, 40), (8, 40), radius_x=20, radius_y=20, large_arc=False, sweep=False)
        self.add_line('sym-e18', (8, 40), (7, 40))
        self.add_arc('sym-e21', (7, 40), (4, 37), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('sym-e22', (4, 37), (4, 11))
        self.add_line('sym-e25', (4, 11), (7, 8))
        self.add_line('sym-e28', (7, 8), (9, 8))
        self.add_line('sym-e31', (9, 8), (24, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e15', 'sym-e17', 'sym-e18', 'sym-e21', 'sym-e22', 'sym-e25', 'sym-e28', 'sym-e31', closed=True)
