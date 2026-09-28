'layout-four-columns: independent smooth-curve repair.\n\nConstruction: Rounded panel grid; all dividers share exact edge nodes and evenly spaced repeated columns.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'bc6b1b30-4674-46a9-b8ad-d1d3ff92bb20'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__layout-four-columns/20260927T072903Z-thuan-mac-1/reference/layout four columns_bc6b1b30-4674-46a9-b8ad-d1d3ff92bb20.svg'
AUTHOR = "gpt-6"


class LayoutFourColumns(Solo48):
    icon_id = 'layout-four-columns'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('layout', 'four', 'columns', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,5,xs=(18,24,30),ys=(18,24,30))
        for x in (18,30): line(self,f"column-{x}",(x,6),(x,42))
        contacts(self)
