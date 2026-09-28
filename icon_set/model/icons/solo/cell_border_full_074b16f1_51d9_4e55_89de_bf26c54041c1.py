'cell-border-full: independent smooth-curve repair.\n\nConstruction: A regular rounded square; its panel structure uses shared centerlines and four equal corners.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '074b16f1-51d9-4e55-89de-bf26c54041c1'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cell border full_074b16f1-51d9-4e55-89de-bf26c54041c1.svg'
AUTHOR = 'gpt-6'


class CellBorderFull(Solo48):
    icon_id = 'cell-border-full'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('cell', 'border', 'full', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(24,),ys=(24,))
        line(self,"vertical",(24,6),(24,42))
        line(self,"horizontal",(6,24),(42,24))
        contacts(self)
