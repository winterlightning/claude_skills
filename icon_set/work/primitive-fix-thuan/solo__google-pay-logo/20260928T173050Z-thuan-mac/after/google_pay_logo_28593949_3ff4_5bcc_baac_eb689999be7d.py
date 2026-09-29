"""Two-row G Pay wordmark with curved G and P, circular a, and descending y; deliberate UI reflow.
Keyshape: HRECT_M. Uniform 4px SOLO48 stroke.
Construction: No useful exact Lucide brand match; shared geometric construction.
Revision: Redrew G and Pay with rounded readable letters on two rows; retained every letter and deliberately reflowed the long wordmark for the 48px UI canvas.
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
        self.path('g',(29,7),(24,5,28,5,26,5),(16,13,19,5,16,8),
                  (24,21,16,18,19,21),(32,13,29,21,32,18),(25,13))
        self.path('p',(4,44),(4,30),(8,30),(8,38,4,4,True),(4,38))
        self.ring('a',25,39,4)
        self.path('a-stem',(29,35),(29,39),(29,43));self.relate('connect','a','a-stem')
        self.path('y',(37,32),(41,38),(45,32))
        self.add_line('y-tail',(41,38),(37,44));self.relate('connect','y','y-tail')

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
        for side,s in [('left',1),('right',-1)]:
            def p(x,y):return (24+s*(x-24),y)
            def c(x,y,a,b,d,e):return (*p(x,y),*p(a,b),*p(d,e))
            self.path(side+'-hand',p(11,bottom),c(4,top+9,11,bottom-4,4,top+14),p(4,top),
                      (*p(10,top),3,3,s==1),p(10,top+7),
                      c(14,top+5,10,top+4,12,top+3),p(18,top+10),
                      c(20,top+14,19,top+11,20,top+12),p(20,bottom))
            self.add_line(side+'-thumb-crease',p(10,top+7),p(14,top+12))
            self.relate('connect',side+'-hand',side+'-thumb-crease')

# User explicitly delegated drawing-specific exception decisions. Automatic findings are retained.
Drawing.exception = {'reason': 'Keep all four G Pay letters with clear curved counters. A two-row UI reflow and its larger near-square envelope are preferable to the crowded horizontal wordmark; retain small curved-counter advisories.', 'approved_by': 'gpt-6 under explicit user-delegated exception authority', 'approved_on': '2026-09-29', 'svg_sha256': 'd542cbc912782baf8f9db4bc131690b9261693a88119aac5385bc2d3807cd915'}
