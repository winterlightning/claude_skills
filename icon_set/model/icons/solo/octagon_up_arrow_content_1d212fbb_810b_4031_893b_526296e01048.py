"""Octagon with Upward Arrow.
Symbol plan: Octagon below a separate upward arrow; source layout preserved.
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

SOURCE_ICON_ID = '1d212fbb-810b-4031-893b-526296e01048'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/1d212fbb-810b-4031-893b-526296e01048.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'octagon-up-arrow-content'
    keyshape = Keyshape.VRECT_L
    category = 'symbol'
    categories = ('symbol',)
    tags = ('sub icon',)
    keywords = ('octagon with upward arrow',)
    def build(self):
        self.add_polyline('octagon',(16,24),(32,24),(40,32),(40,36),(32,44),(16,44),(8,36),(8,32),closed=True)
        self.add_polyline('arrow',(16,12),(24,4),(32,12))
        self.add_line('stem',(24,4),(24,16))
        contacts(self)
