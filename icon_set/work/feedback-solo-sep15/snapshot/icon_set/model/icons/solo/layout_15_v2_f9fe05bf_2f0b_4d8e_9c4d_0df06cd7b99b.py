'layout-15: independent smooth-curve repair.\n\nConstruction: Rounded panel grid; all dividers share exact edge nodes and evenly spaced repeated columns.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'f9fe05bf-2f0b-4d8e-9c4d-0df06cd7b99b'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout 15_f9fe05bf-2f0b-4d8e-9c4d-0df06cd7b99b.svg'
AUTHOR = 'gpt-6'


class Layout15Variant2(Solo48):
    icon_id = 'layout-15-v2'
    variant_of = 'layout-15'
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
