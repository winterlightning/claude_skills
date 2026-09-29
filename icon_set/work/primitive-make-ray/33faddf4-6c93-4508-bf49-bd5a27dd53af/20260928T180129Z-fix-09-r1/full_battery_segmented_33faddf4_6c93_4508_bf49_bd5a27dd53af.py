"""charging battery full.
Plan: Made the case horizontal with three evenly spaced full-charge bars and a clear right terminal.
Construction: battery-full: rounded horizontal housing and repeated vertical charge bars.
Keyshape: HRECT_M; semantic arrangement prioritized within 48px.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '33faddf4-6c93-4508-bf49-bd5a27dd53af'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__full-battery-segmented/20260928T180129Z-thuan-mac/reference/charging battery full_33faddf4-6c93-4508-bf49-bd5a27dd53af.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'full-battery-segmented'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('charging', 'battery', 'full')

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

        self.rect('case',4,10,32,28,3)
        for i in range(3):self.add_line('charge'+str(i),(12+i*8,18),(12+i*8,30))
        self.add_line('terminal',(44,20),(44,28))
