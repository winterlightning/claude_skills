'layout-4: independent smooth-curve repair.\n\nConstruction: Rounded panel grid; all dividers share exact edge nodes and evenly spaced repeated columns.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '646e9ce1-ff45-48de-b79d-27a80798b106'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout 4_646e9ce1-ff45-48de-b79d-27a80798b106.svg'
AUTHOR = 'gpt-6'


class Layout4(Solo48):
    icon_id = 'layout-4'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('layout', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(18,24,30),ys=(18,24,30))
        line(self,"top-row",(6,18),(42,18))
        line(self,"bottom-row",(6,30),(42,30))
        line(self,"col-a",(18,18),(18,30))
        line(self,"col-b",(30,18),(30,30))
        contacts(self)
