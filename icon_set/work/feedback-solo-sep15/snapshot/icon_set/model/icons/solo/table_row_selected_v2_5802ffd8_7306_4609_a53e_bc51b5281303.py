'table-row-selected: independent smooth-curve repair.\n\nConstruction: Rounded panel grid; all dividers share exact edge nodes and evenly spaced repeated columns.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '5802ffd8-7306-4609-a53e-bc51b5281303'
SOURCE_PATH = 'pictographic-primitives/interface-essential/table row selected_5802ffd8-7306-4609-a53e-bc51b5281303.svg'
AUTHOR = 'gpt-6'


class TableRowSelectedVariant2(Solo48):
    icon_id = 'table-row-selected-v2'
    variant_of = 'table-row-selected'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('table', 'row', 'selected', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(18,24,30),ys=(18,24,30))
        line(self,"row",(6,24),(42,24))
        line(self,"column",(24,6),(24,42))
        contacts(self)
