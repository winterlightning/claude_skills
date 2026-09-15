'layout-8: independent smooth-curve repair.\n\nConstruction: Rounded panel grid; all dividers share exact edge nodes and evenly spaced repeated columns.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '968ebc82-99c6-4e6a-8713-e6c0ea0278cd'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout 8_968ebc82-99c6-4e6a-8713-e6c0ea0278cd.svg'
AUTHOR = 'gpt-6'


class Layout8(Solo48):
    icon_id = 'layout-8'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(18,24,30),ys=(18,24,30))
        for x in (18,30): line(self,f"column-{x}",(x,6),(x,42))
        for y in (18,30): line(self,f"row-{y}",(6,y),(42,y))
        contacts(self)
