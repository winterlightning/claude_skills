"""Facial Recognition Scan.
Symbol plan: Four scan corners around a face capsule, preserving source two eye marks.
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

SOURCE_ICON_ID = '71a35cad-2876-4712-8cbd-ead7a0c2fa1c'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/71a35cad-2876-4712-8cbd-ead7a0c2fa1c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'face-scan-content'
    keyshape = Keyshape.SQUARE
    category = 'symbol'
    tags = ('sub icon',)
    keywords = ('facial recognition scan',)
    def build(self):
        for i,(x,y,sx,sy) in enumerate(((6,6,1,1),(42,6,-1,1),(6,42,1,-1),(42,42,-1,-1))):
            self.add_polyline(f'corner-{i}',(x+6*sx,y),(x,y),(x,y+6*sy))
        self.add_dot('eye-left',(18,21))
        self.add_dot('eye-right',(30,21))
        self.add_arc('smile',(18,30),(30,30),radius_x=8,radius_y=8,sweep=False)
        contacts(self)
