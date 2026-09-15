'shop-shopping: independent smooth-curve repair.\n\nConstruction: Store awning with three broad smooth scallops above a joined shopfront. Reduce five cramped scallops to three.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/store.svg and atomic-debug/store.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '36560de1-1707-4464-8a11-ce1847210523'
SOURCE_PATH = 'pictographic-primitives/shopping/shop_36560de1-1707-4464-8a11-ce1847210523.svg'
AUTHOR = 'gpt-6'


class ShopShoppingVariant2(Solo48):
    icon_id = 'shop-shopping-v2'
    variant_of = 'shop-shopping'
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
