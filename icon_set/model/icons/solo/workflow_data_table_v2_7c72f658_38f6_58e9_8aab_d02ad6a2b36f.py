'workflow-data-table: distinct review variant.\n\nConstruction: Data table with a merged header above a two-by-two data region.\nKeyshape: SQUARE; exact SOLO48 envelope.\nConstruction reference: layout-grid from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '7c72f658-38f6-58e9-8aab-d02ad6a2b36f'
SOURCE_PATH = 'pictographic-primitives/business/workflow data table_7c72f658-38f6-58e9-8aab-d02ad6a2b36f.svg'
AUTHOR = 'gpt-6'


class WorkflowDataTableVariant2(Solo48):
    icon_id = 'workflow-data-table-v2'
    variant_of = 'workflow-data-table'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('workflow', 'data', 'table', 'business')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(24,),ys=(18,30))
        for y in (18,30):line(self,f'row-{y}',(6,y),(42,y))
        line(self,'column',(24,18),(24,42))
        contacts(self)
