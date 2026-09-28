# Variant of disabled-battery-content; parent file remains unchanged.
"""Disabled Battery Symbol.
Symbol plan: Battery and diagonal disable stroke. Interrupted enclosure avoids cramped wedges.
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
SOURCE_ICON_ID = '49cd19ff-6293-48fa-8d62-d508a17a80ae'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/49cd19ff-6293-48fa-8d62-d508a17a80ae.svg'
AUTHOR = 'gpt-6'

class DrawingVariant2(Solo48):
    icon_id = 'disabled-battery-content-v2'
    variant_of = 'disabled-battery-content'
    variant_label = 'Complete disabled battery'
    keyshape = Keyshape.HRECT_M
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('disabled battery symbol',)

    def build(self):
        self.add_polyline('body',(4,38),(4,10),(36,10),(36,38),closed=True)
        self.add_line('terminal',(44,20),(44,28))
        self.add_line('slash',(4,38),(36,10))
        self.relate('connect','body','slash')
