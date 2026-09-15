'layout-right: independent smooth-curve repair.\n\nConstruction: Rounded panel grid; all dividers share exact edge nodes and evenly spaced repeated columns.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '29ad656c-72e5-47fe-9a76-8b377da539c2'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout right_29ad656c-72e5-47fe-9a76-8b377da539c2.svg'
AUTHOR = 'gpt-6'


class LayoutRightVariant2(Solo48):
    icon_id = 'layout-right-v2'
    variant_of = 'layout-right'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'right', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(18,24,30),ys=(18,24,30))
        line(self,"sidebar",(30,6),(30,42))
        contacts(self)
