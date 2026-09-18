"""Pie Chart and Growth Arrow.
Symbol plan: Open pie circle and ascending arrow. Deliberate directional asymmetry.
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

SOURCE_ICON_ID = 'f82a9a59-0712-48ad-b67b-ef47e7c946ad'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/f82a9a59-0712-48ad-b67b-ef47e7c946ad.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'pie-chart-growth-content'
    keyshape = Keyshape.SQUARE
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('pie chart and growth arrow',)
    def build(self):
        path(self,'pie',(24,6),('A',(6,24),18,18,False),('A',(24,42),18,18,False),('L',(24,24)),('L',(24,6)))
        self.add_polyline('growth',(33,34),(42,20),(42,30))
        self.add_line('arrow',(33,20),(42,20))
        contacts(self)
