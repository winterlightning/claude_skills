'layout-6: distinct review variant.\n\nConstruction: Layout with two upper panes and one full-width footer, distinct from the header-and-panes slot machine.\nKeyshape: SQUARE; exact SOLO48 envelope.\nConstruction reference: layout-grid from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'a299b5ca-1eed-416f-a091-4bb307b869ec'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout 6_a299b5ca-1eed-416f-a091-4bb307b869ec.svg'
AUTHOR = 'gpt-6'


class Layout6Variant2(Solo48):
    icon_id = 'layout-6-v2'
    variant_of = 'layout-6'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,ys=(30,),xs=(24,))
        line(self,'footer',(6,30),(42,30))
        line(self,'column',(24,6),(24,30))
        contacts(self)
