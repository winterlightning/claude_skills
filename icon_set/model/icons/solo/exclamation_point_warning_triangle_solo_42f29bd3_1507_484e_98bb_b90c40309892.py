"""Exclamation Point Warning Triangle.
Symbol plan: Triangular warning outline with centered stem and detached dot. Bounds (2,6)-(46,42).
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

SOURCE_ICON_ID = '42f29bd3-1507-484e-98bb-b90c40309892'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/42f29bd3-1507-484e-98bb-b90c40309892.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'exclamation-point-warning-triangle-solo'
    keyshape = Keyshape.VRECT_L
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('exclamation point warning triangle',)
    def build(self):
        self.add_polyline('triangle',(24,4),(40,44),(8,44),closed=True)
        self.add_line('warning',(24,26),(24,28))
        self.add_dot('dot',(24,36))
        contacts(self)
