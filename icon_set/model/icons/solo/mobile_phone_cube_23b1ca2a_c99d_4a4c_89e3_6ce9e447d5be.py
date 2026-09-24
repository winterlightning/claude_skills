from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23b1ca2a-c99d-4a4c-89e3-6ce9e447d5be'
SOURCE_PATH = 'icon_set/work/todo-references/Mobile Phone Cube_23b1ca2a-c99d-4a4c-89e3-6ce9e447d5be.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mobile-phone-cube'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('Mobile Phone Cube',)

    def build(self):
        # One rounded enclosure; shared corner radius preserves tangent joins.
        l,t,r,b,rad = (8,4,40,44,6)
        self.add_line('frame-top',(l+rad,t),(r-rad,t))
        self.add_arc('frame-tr',(r-rad,t),(r,t+rad),radius_x=rad)
        self.add_line('frame-right',(r,t+rad),(r,b-rad))
        self.add_arc('frame-br',(r,b-rad),(r-rad,b),radius_x=rad)
        self.add_line('frame-bottom',(r-rad,b),(l+rad,b))
        self.add_arc('frame-bl',(l+rad,b),(l,b-rad),radius_x=rad)
        self.add_line('frame-left',(l,b-rad),(l,t+rad))
        self.add_arc('frame-tl',(l,t+rad),(l+rad,t),radius_x=rad)
        self.add_contour('frame','frame-top','frame-tr','frame-right','frame-br','frame-bottom','frame-bl','frame-left','frame-tl',closed=True)
        # Phone footer and a centered perspective cube; common vertices own all seams.
        self.add_line('footer',(8,36),(40,36))
        self.relate('connect','footer','frame')
        top=(24,13); left=(17,17); right=(31,17); mid=(24,21); bottom=(24,29)
        self.add_polyline('cube',top,right,(31,25),bottom,(17,25),left,closed=True)
        self.add_polyline('cube-top-seam',left,mid,right)
        self.add_line('cube-front-seam',mid,bottom)
        self.relate('connect','cube','cube-top-seam')
        self.relate('connect','cube','cube-front-seam')
        self.relate('connect','cube-top-seam','cube-front-seam')
