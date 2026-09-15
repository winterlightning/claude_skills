'layout-left: independent smooth-curve repair.\n\nConstruction: Rounded panel grid; all dividers share exact edge nodes and evenly spaced repeated columns.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'e4d2ef1c-4583-47fc-bc76-b5edcb616774'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout left_e4d2ef1c-4583-47fc-bc76-b5edcb616774.svg'
AUTHOR = 'gpt-6'


class LayoutLeftVariant2(Solo48):
    icon_id = 'layout-left-v2'
    variant_of = 'layout-left'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'left', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(18,24,30),ys=(18,24,30))
        line(self,"sidebar",(18,6),(18,42))
        contacts(self)
