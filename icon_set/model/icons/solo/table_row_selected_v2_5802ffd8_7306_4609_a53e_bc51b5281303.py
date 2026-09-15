'table-row-selected: distinct review variant.\n\nConstruction: Table with a wide selected middle row and a centered selection dot; narrow outer rows make it distinct from a regular data grid.\nKeyshape: SQUARE; exact SOLO48 envelope.\nConstruction reference: layout-grid from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '5802ffd8-7306-4609-a53e-bc51b5281303'
SOURCE_PATH = 'pictographic-primitives/interface-essential/table row selected_5802ffd8-7306-4609-a53e-bc51b5281303.svg'
AUTHOR = 'gpt-6'


class TableRowSelectedVariant2(Solo48):
    icon_id = 'table-row-selected-v2'
    variant_of = 'table-row-selected'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('table', 'row', 'selected', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,ys=(16,32))
        line(self,'upper-row',(6,16),(42,16))
        line(self,'lower-row',(6,32),(42,32))
        self.add_dot('selection',(24,24))
        contacts(self)
