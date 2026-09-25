"""Document curved fold.

Construction reference: file.
Retains the attached fold; broad empty page below.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '9ac73c1e-c37d-4c37-82d8-4a7e2939738d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/file 3_9ac73c1e-c37d-4c37-82d8-4a7e2939738d.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'document-curved-fold-solo-9ac73c1e'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('container', 'other', 'primitives-generate')
    aliases = ('document-curved-fold',)
    keywords = ('document', 'curved', 'fold')

    def build(self):
        # Large upper-right fold retains a genuine rounded inward corner.
        path(self,'page',(12,4),[('L',(24,4)),('L',(40,20)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
        path(self,'fold',(24,4),[('L',(24,16)),('A',(28,20),4,4,False),('L',(40,20))])
        self.relate('connect','page','fold')
