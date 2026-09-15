'warehouse-shipping: distinct review variant.\n\nConstruction: Shipping warehouse with a central loading door and a horizontal roll-up panel; retain the smooth roof silhouette.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nConstruction reference: warehouse from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '8f5402f0-5566-4c6d-ac0c-c86e0360848e'
SOURCE_PATH = 'pictographic-primitives/shipping/warehouse_8f5402f0-5566-4c6d-ac0c-c86e0360848e.svg'
AUTHOR = 'gpt-6'


class WarehouseShippingVariant2(Solo48):
    icon_id = 'warehouse-shipping-v2'
    variant_of = 'warehouse-shipping'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('warehouse', 'shipping')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'warehouse',(4,36),('L',(4,22)),('C',(4,20),(5,19),(7,18)),('L',(24,8)),('L',(41,18)),('C',(43,19),(44,20),(44,22)),('L',(44,36)),('A',4,4,True,(40,40)),('L',(8,40)),('A',4,4,True,(4,36)),closed=True)
        poly(self,'loading-door',(16,40),(16,24),(32,24),(32,40))
        line(self,'door-panel',(16,32),(32,32))
        contacts(self)
