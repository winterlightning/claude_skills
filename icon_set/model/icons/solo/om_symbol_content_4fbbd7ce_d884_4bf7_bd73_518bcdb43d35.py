"""Hindu Om Symbol.
Symbol plan: Om symbol with double-lobed main sweep, lower-right tail, upper crescent and dot; supplied religious-symbol reference.
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

SOURCE_ICON_ID = '4fbbd7ce-d884-4bf7-bd73-518bcdb43d35'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/4fbbd7ce-d884-4bf7-bd73-518bcdb43d35.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'om-symbol-content'
    keyshape = Keyshape.SQUARE
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('hindu om symbol',)
    def build(self):
        path(self,'three',(6,14),('A',(26,18),10,8,True),('L',(18,25)),('A',(26,34),8,8,True),('A',(6,34),10,8,True))
        self.add_bezier('tail',(18,25),((32,23),(42,24),(42,32)))
        self.add_line('tail-tip',(42,32),(38,38))
        self.relate('connect','tail','tail-tip')
        self.relate('connect','three','tail')
        self.add_arc('crescent',(35,16),(42,12),radius_x=8,radius_y=6,sweep=False)
        self.add_dot('dot',(34,6))
        contacts(self)
