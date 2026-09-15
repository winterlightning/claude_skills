'transit-gateway: independent smooth-curve repair.\n\nConstruction: Transit gateway with a rounded central node and aligned inlet and arrow outlet.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/arrow-right.svg and atomic-debug/arrow-right.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'ed53f150-82ce-586d-8d45-acbd76391d39'
SOURCE_PATH = 'pictographic-primitives/programing/transit gateway_ed53f150-82ce-586d-8d45-acbd76391d39.svg'
AUTHOR = 'gpt-6'


class TransitGatewayVariant2(Solo48):
    icon_id = 'transit-gateway-v2'
    variant_of = 'transit-gateway'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('transit', 'gateway', 'programing')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'gateway',14,8,34,40,4,ys=(24,))
        line(self,'inlet',(4,24),(24,24));line(self,'outlet',(34,24),(44,24))
        poly(self,'arrow',(39,19),(44,24),(39,29))
        contacts(self)
