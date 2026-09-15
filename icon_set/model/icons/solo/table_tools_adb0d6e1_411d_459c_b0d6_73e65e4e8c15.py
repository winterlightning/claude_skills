'table-tools: independent smooth-curve repair.\n\nConstruction: Rounded panel grid; all dividers share exact edge nodes and evenly spaced repeated columns.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'adb0d6e1-411d-459c-b0d6-73e65e4e8c15'
SOURCE_PATH = 'pictographic-primitives/interface-essential/table tools_adb0d6e1-411d-459c-b0d6-73e65e4e8c15.svg'
AUTHOR = 'gpt-6'


class TableTools(Solo48):
    icon_id = 'table-tools'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('table', 'tools', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(18,24,30),ys=(18,24,30))
        for x in (18,30): line(self,f"column-{x}",(x,6),(x,42))
        for y in (18,30): line(self,f"row-{y}",(6,y),(42,y))
        contacts(self)
