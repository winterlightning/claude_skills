"""Single-line G Pay wordmark, with a circular G, rounded P, open single-storey a and descending y.
Keyshape: HRECT_M. Uniform 4px SOLO48 stroke.
Construction: No useful exact Lucide brand match; shared geometric construction.
Revision: Restored the horizontal G Pay arrangement and curved letterforms; retained the compact wordmark envelope.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '28593949-3ff4-5bcc-baac-eb689999be7d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-pay-logo/20260928T173050Z-thuan-mac/reference/google pay_28593949-3ff4-5bcc-baac-eb689999be7d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'google-pay-logo'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('google', 'pay', 'logo')

    def build(self):
        self.path('g',(13,19),(9,17,12,17,10,17),(4,24,5,17,4,20),
                  (9,31,4,28,5,31),(14,25,12,31,14,29),(10,25))
        self.path('p',(21,31),(21,17),(25,17),(25,25,30,17,30,25),(21,25))
        self.ring('a',33,27,3,4)
        self.path('a-stem',(36,23),(36,27),(36,31))
        self.relate('connect','a','a-stem')
        self.path('y',(40,23),(43,30),(46,23))
        self.path('y-tail',(43,30),(40,36))
        self.relate('connect','y','y-tail')

    def path(self, name, start, *steps, closed=False):
        members=[]; here=start
        for j,step in enumerate(steps):
            member=f'{name}-{j}'
            if len(step)==2:
                self.add_line(member,here,step); end=step
            elif len(step)==5:
                x,y,rx,ry,sweep=step;end=(x,y)
                self.add_arc(member,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
            else:
                x,y,c1x,c1y,c2x,c2y=step;end=(x,y)
                self.add_bezier(member,here,((c1x,c1y),(c2x,c2y),end))
            members.append(member);here=end
        self.add_contour(name,*members,closed=closed)

    def ring(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.path(name,(x-rx,y),(x,y-ry,rx,ry,True),(x+rx,y,rx,ry,True),
                  (x,y+ry,rx,ry,True),(x-rx,y,rx,ry,True),closed=True)

    def rect(self,name,x,y,w,h,r=3):
        self.path(name,(x+r,y),(x+w-r,y),(x+w,y+r,r,r,True),(x+w,y+h-r),
                  (x+w-r,y+h,r,r,True),(x+r,y+h),(x,y+h-r,r,r,True),
                  (x,y+r),(x+r,y,r,r,True),closed=True)

    def cups(self,top=24,bottom=44):
        # Mirrored open wrists, curved outside palms and rounded thumb pads.
        # Only hands are present: no detached head/body spacing applies.
        for side,s in [('left',1),('right',-1)]:
            def p(x,y):return (24+s*(x-24),y)
            def c(x,y,a,b,d,e):return (*p(x,y),*p(a,b),*p(d,e))
            def a(x,y,rx,ry,sweep):return (*p(x,y),rx,ry,sweep if s==1 else not sweep)
            self.path(side+'-outer',p(11,bottom),c(4,top+10,11,bottom-5,4,top+15),p(4,top),
                      a(10,top,3,3,True),p(10,top+7))
            self.path(side+'-thumb',p(13,top+12),p(10,top+8),
                      c(14,top+4,6,top+4,11,top+1),p(19,top+10),
                      c(20,bottom-5,20,top+12,20,bottom-8),p(20,bottom))
            self.relate('connect',side+'-outer',side+'-thumb')
