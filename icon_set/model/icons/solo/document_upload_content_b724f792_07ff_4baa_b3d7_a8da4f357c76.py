"""Document Upload Arrow.
Symbol plan: Fold-free document with central upload arrow and clipped bottom corner.
User explicitly requested the complete combined subject on SOLO48.
References: supplied source render; local Lucide original and atomic geometry sheet
(triangle-alert, user-round-plus, file-up, battery-charging, plug-zap, scan-face,
clapperboard, badge-check, paw-print, car, wrench, shirt, chart-pie, delete).
Human subjects follow icon_set/references/human_ref/user.svg.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
from ._container_content_batch import path, cross, contacts, bust, car, bolt

SOURCE_ICON_ID = 'b724f792-07ff-4baa-b3d7-a8da4f357c76'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/b724f792-07ff-4baa-b3d7-a8da4f357c76.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'document-upload-content'
    keyshape = Keyshape.VRECT_L
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('document upload arrow',)
    def build(self):
        path(self,'page',(12,4),('L',(36,4)),('A',(40,8),4,4,True),('L',(40,34)),('L',(30,44)),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,8)),('A',(12,4),4,4,True),closed=True)
        self.add_polyline('arrow',(17,23),(24,15),(31,23))
        self.add_line('shaft',(24,15),(24,33))
        contacts(self)
