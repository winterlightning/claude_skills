'layout-top: independent smooth-curve repair.\n\nConstruction: Rounded panel grid; all dividers share exact edge nodes and evenly spaced repeated columns.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '5ef40d38-4ffe-4bf2-bab4-67cb4f5d88fc'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout top_5ef40d38-4ffe-4bf2-bab4-67cb4f5d88fc.svg'
AUTHOR = 'gpt-6'


class LayoutTop(Solo48):
    icon_id = 'layout-top'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('layout', 'top', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(18,24,30),ys=(18,24,30))
        line(self,"header",(6,18),(42,18))
        contacts(self)
