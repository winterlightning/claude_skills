'workflow-data-table: independent smooth-curve repair.\n\nConstruction: Rounded panel grid; all dividers share exact edge nodes and evenly spaced repeated columns.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '7c72f658-38f6-58e9-8aab-d02ad6a2b36f'
SOURCE_PATH = 'pictographic-primitives/business/workflow data table_7c72f658-38f6-58e9-8aab-d02ad6a2b36f.svg'
AUTHOR = 'gpt-6'


class WorkflowDataTable(Solo48):
    icon_id = 'workflow-data-table'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('workflow', 'data', 'table', 'business')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(18,24,30),ys=(18,24,30))
        for x in (18,30): line(self,f"column-{x}",(x,6),(x,42))
        for y in (18,30): line(self,f"row-{y}",(6,y),(42,y))
        contacts(self)
