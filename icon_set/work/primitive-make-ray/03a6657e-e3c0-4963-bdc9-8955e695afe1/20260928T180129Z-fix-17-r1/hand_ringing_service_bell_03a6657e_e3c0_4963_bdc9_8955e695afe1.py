"""reception bell call.
Plan: Redrew a downward pointing bent finger over a separate plunger and domed service bell.
Construction: hand-grab: smooth fingertip; source downward pressing gesture retained.
Keyshape: SQUARE; semantic arrangement prioritized within 48px.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '03a6657e-e3c0-4963-bdc9-8955e695afe1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-ringing-service-bell/20260928T180129Z-thuan-mac/reference/reception bell call_03a6657e-e3c0-4963-bdc9-8955e695afe1.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'hand-ringing-service-bell'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('reception', 'bell', 'call')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def rect(self,n,x,y,w,h,r=3):
        self.add_line(n+'t',(x+r,y),(x+w-r,y))
        self.add_arc(n+'tr',(x+w-r,y),(x+w,y+r),radius_x=r)
        self.add_line(n+'r',(x+w,y+r),(x+w,y+h-r))
        self.add_arc(n+'br',(x+w,y+h-r),(x+w-r,y+h),radius_x=r)
        self.add_line(n+'b',(x+w-r,y+h),(x+r,y+h))
        self.add_arc(n+'bl',(x+r,y+h),(x,y+h-r),radius_x=r)
        self.add_line(n+'l',(x,y+h-r),(x,y+r))
        self.add_arc(n+'tl',(x,y+r),(x+r,y),radius_x=r)
        self.add_contour(n,*[n+s for s in ['t','tr','r','br','b','bl','l','tl']],closed=True)

    def build(self):

        self.add_bezier('finger',(19,6),((21,9),(24,12),(25,14)),((23,17),(20,21),(20,22)),((19,26),(23,27),(25,24)),((29,20),(32,16),(34,13)),((34,17),(34,19),(37,19)),((40,19),(39,12),(40,6)))
        self.add_line('button',(21,29),(29,29));self.add_line('plunger',(25,29),(25,33));self.relate('connect','button','plunger')
        self.add_bezier('dome',(6,42),((6,30),(42,30),(42,42)))
        self.add_line('base',(6,42),(42,42));self.relate('connect','base','dome')
