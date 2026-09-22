"""Right-facing box truck. HRECT_L (4,8)-(44,40); repeated radius-four
wheel lobes share y=36 and chassis contacts. Cargo box owns a split cab attachment
at (24,16). Lucide truck informs integrated wheel lobes. Omit window
crossbar to preserve wheel clearance; retain sloped windshield and tall box.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '6bb7f733-561a-4d2b-a952-3879ff5bb90f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_34/shipper_6bb7f733-561a-4d2b-a952-3879ff5bb90f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'plain-box-delivery-truck'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ['Delivery Truck']
    keywords = ['truck','box','delivery','vehicle','cab','transport']
    def build(self):
        self.add_polyline('upper',(4,36),(4,8),(24,8),(24,16),(35,16),(44,26),(44,36),(40,36))
        self.add_arc('front-wheel',(40,36),(32,36),radius_x=4)
        self.add_line('chassis-front',(32,36),(24,36))
        self.add_line('chassis-rear',(24,36),(16,36))
        self.add_arc('rear-wheel',(16,36),(8,36),radius_x=4)
        self.add_line('tail',(8,36),(4,36))
        self.add_contour('underbody','front-wheel','chassis-front','chassis-rear','rear-wheel','tail')
        self.relate('connect','upper-7','front-wheel')
        self.relate('connect','tail','upper-1')
        self.add_line('divider',(24,16),(24,36))
        for edge in ['upper-3','upper-4','chassis-front','chassis-rear']:self.relate('connect','divider',edge)
