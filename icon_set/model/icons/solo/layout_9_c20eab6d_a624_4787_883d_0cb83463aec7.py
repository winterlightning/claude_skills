'layout-9: independent smooth-curve repair.\n\nConstruction: Preserve the layout: one full-height left pane and two stacked right panes; rounded outer corners and exact shared divider junctions.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'c20eab6d-a624-4787-883d-0cb83463aec7'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout 9_c20eab6d-a624-4787-883d-0cb83463aec7.svg'
AUTHOR = 'gpt-6'


class Layout9(Solo48):
    icon_id = 'layout-9'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(24,),ys=(24,))
        line(self,'vertical',(24,6),(24,42))
        line(self,'right-divider',(24,24),(42,24))
        contacts(self)
