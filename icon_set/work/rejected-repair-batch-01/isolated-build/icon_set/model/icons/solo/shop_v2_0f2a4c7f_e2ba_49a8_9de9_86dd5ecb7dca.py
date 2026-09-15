'shop: independent smooth-curve repair.\n\nConstruction: Store awning with three broad smooth scallops above a joined shopfront. Reduce five cramped scallops to three.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/store.svg and atomic-debug/store.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '0f2a4c7f-e2ba-49a8-9de9-86dd5ecb7dca'
SOURCE_PATH = 'pictographic-primitives/shopping/shop_0f2a4c7f-e2ba-49a8-9de9-86dd5ecb7dca.svg'
AUTHOR = 'gpt-6'


class ShopVariant2(Solo48):
    icon_id = 'shop-v2'
    variant_of = 'shop'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shop', 'shopping')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'awning',(4,20),('L',(8,8)),('L',(40,8)),('L',(44,20)),('C',(44,23),(42,25),(40,25)),('C',(36,25),(33,23),(31,20)),('C',(29,26),(19,26),(17,20)),('C',(15,23),(12,25),(8,25)),('C',(6,25),(4,23),(4,20)),closed=True)
        poly(self,'shopfront',(8,25),(8,40),(40,40),(40,25))
        contacts(self)
