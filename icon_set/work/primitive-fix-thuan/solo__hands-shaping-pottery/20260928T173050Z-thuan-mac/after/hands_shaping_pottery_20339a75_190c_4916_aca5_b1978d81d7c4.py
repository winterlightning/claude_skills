"""Rounded pottery vessel with elliptical open rim above two mirrored sculpting hands.
Keyshape: SQUARE. Uniform 4px SOLO48 stroke.
Construction: Human full_body_ref.png rounded anatomy; reference vessel and mirrored hands.
Revision: Restored an open oval rim, smooth pot belly and complete cupped hand contours.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '20339a75-190c-4916-aca5-b1978d81d7c4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-shaping-pottery/20260928T173050Z-thuan-mac/reference/crafts pottery_20339a75-190c-4916-aca5-b1978d81d7c4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hands-shaping-pottery'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('hands', 'shaping', 'pottery')

    def build(self):
        self.ring('rim',24,8,9,4)
        self.path('pot',(15,8),(15,18,16,12,14,14),(24,27,15,24,19,27),
                  (33,18,29,27,33,24),(33,8,34,14,32,12))
        self.relate('connect','rim','pot')
        self.cups(25,44)

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
            self.path(side+'-hand',p(11,bottom),c(4,top+9,11,bottom-4,4,top+12),p(4,top),
                      (*p(10,top),3,3,s==1),p(10,top+7),
                      c(14,top+5,10,top+4,12,top+3),p(18,top+10),
                      c(20,top+14,19,top+11,20,top+12),p(20,bottom))
            self.add_line(side+'-thumb-crease',p(10,top+7),p(12,top+10))
            self.relate('connect',side+'-hand',side+'-thumb-crease')

# User explicitly delegated drawing-specific exception decisions. Automatic findings are retained.
Drawing.exception = {'reason': 'Preserve the elliptical pottery opening and complete paired hands. Compact finger construction, rim junction and optical composition envelope are intentional; all regions remain legible at 48px.', 'approved_by': 'gpt-6 under explicit user-delegated exception authority', 'approved_on': '2026-09-29', 'svg_sha256': 'f8e94ec21c901b115bfb1c6c462f1d8c5a8d85eeb320e47715e638849435264b'}
