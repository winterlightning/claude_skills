'shopping-bag-shopping: independent smooth-curve repair.\n\nConstruction: Shopping bag with a semicircular handle and four matching rounded body corners.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/shopping-bag.svg and atomic-debug/shopping-bag.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '7cc3838b-e0d3-5bed-b6f7-a9a8754f6589'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping bag_7cc3838b-e0d3-5bed-b6f7-a9a8754f6589.svg'
AUTHOR = 'gpt-6'


class ShoppingBagShopping(Solo48):
    icon_id = 'shopping-bag-shopping'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ('shopping', 'bag')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'handle',(14,18),('L',(14,14)),('A',10,10,True,(24,4)),('A',10,10,True,(34,14)),('L',(34,18)))
        box(self,'bag',8,18,40,44,4,xs=(14,34))
        contacts(self)
