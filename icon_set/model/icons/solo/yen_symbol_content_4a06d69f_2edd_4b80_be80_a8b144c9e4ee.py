"""Japanese Yen Currency Symbol.
Symbol plan: Source yen/yuan currency form: forked top, one crossbar, central stem. Explicitly requested missing symbol artwork.
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

SOURCE_ICON_ID = '4a06d69f-2edd-4b80-be80-a8b144c9e4ee'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/4a06d69f-2edd-4b80-be80-a8b144c9e4ee.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'yen-symbol-content'
    keyshape = Keyshape.VRECT_L
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('japanese yen currency symbol',)
    def build(self):
        self.add_polyline('fork',(8,4),(24,24),(40,4))
        self.add_line('stem',(24,24),(24,44))
        self.add_polyline('bar',(12,28),(24,28),(36,28))
        self.relate('connect','stem','bar')
        contacts(self)
