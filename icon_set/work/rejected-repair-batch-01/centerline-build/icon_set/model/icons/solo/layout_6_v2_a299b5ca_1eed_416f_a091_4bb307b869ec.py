'layout-6: independent smooth-curve repair.\n\nConstruction: Rounded panel grid; all dividers share exact edge nodes and evenly spaced repeated columns.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'a299b5ca-1eed-416f-a091-4bb307b869ec'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout 6_a299b5ca-1eed-416f-a091-4bb307b869ec.svg'
AUTHOR = 'gpt-6'


class Layout6Variant2(Solo48):
    icon_id = 'layout-6-v2'
    variant_of = 'layout-6'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(18,24,30),ys=(18,24,30))
        line(self,"header",(6,18),(42,18))
        line(self,"column-a",(18,18),(18,42))
        line(self,"column-b",(30,18),(30,42))
        contacts(self)
