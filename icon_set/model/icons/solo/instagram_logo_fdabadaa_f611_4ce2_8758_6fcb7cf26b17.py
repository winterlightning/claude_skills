"""Instagram logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fdabadaa-f611-4ce2-8758-6fcb7cf26b17'
SOURCE_PATH = 'pictographic-primitives/logos/instagram logo_fdabadaa-f611-4ce2-8758-6fcb7cf26b17.svg'
AUTHOR = 'gpt-6'

class InstagramLogo(Solo48):
    icon_id = 'instagram-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('instagram', 'logo', 'logos')

    def build(self):
        self.add_arc('sym-e0', (16, 24), (32, 24), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('sym-e1', (32, 24), (16, 24), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('sym-e2', (24, 42), (36, 42))
        self.add_arc('sym-e4', (36, 42), (42, 36), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_line('sym-e5', (42, 36), (42, 12))
        self.add_arc('sym-e9', (42, 12), (36, 6), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_line('sym-e10', (36, 6), (12, 6))
        self.add_arc('sym-e14', (12, 6), (6, 12), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_line('sym-e15', (6, 12), (6, 36))
        self.add_arc('sym-e19', (6, 36), (12, 42), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_line('sym-e20', (12, 42), (24, 42))
        self.add_line('sym-e22', (31, 20), (42, 20))
        self.add_line('sym-e23', (17, 20), (6, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e9', 'sym-e10', 'sym-e14', 'sym-e15', 'sym-e19', 'sym-e20', closed=True)
        self.add_contour('sym-c2', 'sym-e22', closed=False)
        self.add_contour('sym-c3', 'sym-e23', closed=False)
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
