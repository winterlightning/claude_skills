'layout-four-columns-1: independent smooth-curve repair.\n\nConstruction: Rounded panel grid; all dividers share exact edge nodes and evenly spaced repeated columns.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '2e6ab6ab-9563-453f-b186-5fff824eaf12'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout four columns 1_2e6ab6ab-9563-453f-b186-5fff824eaf12.svg'
AUTHOR = 'gpt-6'


class LayoutFourColumns1Variant2(Solo48):
    icon_id = 'layout-four-columns-1-v2'
    variant_of = 'layout-four-columns-1'
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
