"""Heartbeat Pulse Activity Circle.
Symbol plan: Circular monitor badge with asymmetric heartbeat pulse.
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

SOURCE_ICON_ID = 'e2fc54fd-f508-44e9-8bfb-11dee5fb3a31'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/e2fc54fd-f508-44e9-8bfb-11dee5fb3a31.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'circle-heartbeat-content'
    keyshape = Keyshape.CIRCLE
    category = 'symbol'
    tags = ('sub icon',)
    keywords = ('heartbeat pulse activity circle',)
    def build(self):
        circle(self,'circle',24,24,20)
        self.add_polyline('pulse',(13,24),(18,24),(22,15),(27,33),(31,24),(35,24))
        contacts(self)
