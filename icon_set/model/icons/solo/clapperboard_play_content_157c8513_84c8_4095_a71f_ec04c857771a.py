"""Movie Play Clapperboard.
Symbol plan: Clapperboard with diagonal slate mark and play triangle; all silhouette and essential controls retained.
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

SOURCE_ICON_ID = '157c8513-84c8-4095-a71f-ec04c857771a'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/157c8513-84c8-4095-a71f-ec04c857771a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'clapperboard-play-content'
    keyshape = Keyshape.VRECT_L
    category = 'symbol'
    categories = ('symbol',)
    tags = ('sub icon',)
    keywords = ('movie play clapperboard',)
    def build(self):
        rounded_rect(self,'body',8,4,40,44,4)
        self.add_line('hinge',(8,12),(40,12))
        self.relate('connect','body','hinge')
        self.add_line('slate',(24,4),(16,12))
        self.relate('connect','body','slate')
        self.relate('connect','hinge','slate')
        self.add_polyline('play',(17,21),(17,35),(31,28),closed=True)
        contacts(self)
