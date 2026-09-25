"""Verified Quality Award Badge.
Symbol plan: Round award medal with check and two ribbons; mirror ribbon placement.
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

SOURCE_ICON_ID = '53ec706a-5a03-4fa7-959b-501626056c10'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/53ec706a-5a03-4fa7-959b-501626056c10.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'quality-award-check-content'
    keyshape = Keyshape.VRECT_L
    category = 'symbol'
    tags = ('sub icon',)
    keywords = ('verified quality award badge',)
    def build(self):
        circle(self,'medal',24,20,16)
        self.add_polyline('check',(17,20),(22,25),(30,17))
        self.add_polyline('ribbon-left',(13,32),(8,44),(20,39))
        self.add_polyline('ribbon-right',(35,32),(40,44),(28,39))
        self.relate('connect','medal','ribbon-left')
        self.relate('connect','medal','ribbon-right')
        contacts(self)
