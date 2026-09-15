'layout-four-columns: independent smooth-curve repair.\n\nConstruction: Rounded panel grid; all dividers share exact edge nodes and evenly spaced repeated columns.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'bc6b1b30-4674-46a9-b8ad-d1d3ff92bb20'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout four columns_bc6b1b30-4674-46a9-b8ad-d1d3ff92bb20.svg'
AUTHOR = 'gpt-6'


class LayoutFourColumnsVariant2(Solo48):
    icon_id = 'layout-four-columns-v2'
    variant_of = 'layout-four-columns'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'four', 'columns', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(18,24,30),ys=(18,24,30))
        for x in (18,30): line(self,f"column-{x}",(x,6),(x,42))
        contacts(self)
