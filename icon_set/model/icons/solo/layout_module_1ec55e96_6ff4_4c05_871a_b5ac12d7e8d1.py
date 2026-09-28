'layout-module: independent smooth-curve repair.\n\nConstruction: A regular rounded square; its panel structure uses shared centerlines and four equal corners.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '1ec55e96-6ff4-4c05-871a-b5ac12d7e8d1'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout module_1ec55e96-6ff4-4c05-871a-b5ac12d7e8d1.svg'
AUTHOR = 'gpt-6'


class LayoutModule(Solo48):
    icon_id = 'layout-module'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('layout', 'module', 'interface-essential')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'frame',4,8,44,40,4,xs=(24,),ys=(24,))
        line(self,'v',(24,8),(24,40))
        line(self,'h',(4,24),(44,24))
        contacts(self)
