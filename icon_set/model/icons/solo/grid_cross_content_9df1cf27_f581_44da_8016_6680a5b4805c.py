"""Grid with Cross Mark.
Symbol plan: Two-column grid beside an X; distinct dot rows maintain consistent spacing.
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

SOURCE_ICON_ID = '9df1cf27-f581-44da-8016-6680a5b4805c'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/9df1cf27-f581-44da-8016-6680a5b4805c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'grid-cross-content'
    keyshape = Keyshape.HRECT_L
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('grid with cross mark',)
    def build(self):
        for i,(x,y) in enumerate(((4,8),(4,24),(4,40),(20,8),(20,24),(20,40))):self.add_dot(f'dot-{i}',(x,y))
        self.add_polyline('cross-a',(32,18),(38,24),(44,30))
        self.add_polyline('cross-b',(32,30),(38,24),(44,18))
        contacts(self)
