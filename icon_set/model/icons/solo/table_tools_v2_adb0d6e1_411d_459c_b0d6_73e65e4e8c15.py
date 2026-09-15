'table-tools: distinct review variant.\n\nConstruction: Table tools shown as a two-column, three-row table with a narrow left label column.\nKeyshape: SQUARE; exact SOLO48 envelope.\nConstruction reference: layout-grid from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'adb0d6e1-411d-459c-b0d6-73e65e4e8c15'
SOURCE_PATH = 'pictographic-primitives/interface-essential/table tools_adb0d6e1-411d-459c-b0d6-73e65e4e8c15.svg'
AUTHOR = 'gpt-6'


class TableToolsVariant2(Solo48):
    icon_id = 'table-tools-v2'
    variant_of = 'table-tools'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('table', 'tools', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(18,),ys=(18,30))
        line(self,'column',(18,6),(18,42))
        for y in (18,30):line(self,f'row-{y}',(6,y),(42,y))
        contacts(self)
