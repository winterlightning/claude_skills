'warehouse-shipping: independent smooth-curve repair.\n\nConstruction: Warehouse silhouette with a gabled roof, smooth eave transitions and rounded lower corners.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/warehouse.svg and atomic-debug/warehouse.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '8f5402f0-5566-4c6d-ac0c-c86e0360848e'
SOURCE_PATH = 'pictographic-primitives/shipping/warehouse_8f5402f0-5566-4c6d-ac0c-c86e0360848e.svg'
AUTHOR = 'gpt-6'


class WarehouseShipping(Solo48):
    icon_id = 'warehouse-shipping'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('warehouse', 'shipping')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'warehouse',(4,36),('L',(4,22)),('C',(4,20),(5,19),(7,18)),('L',(24,8)),('L',(41,18)),('C',(43,19),(44,20),(44,22)),('L',(44,36)),('A',4,4,True,(40,40)),('L',(8,40)),('A',4,4,True,(4,36)),closed=True)
        contacts(self)
