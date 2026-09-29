"""Front-facing car supported above mirrored cupped hands; even wheels and sloped windshield.
Keyshape: SQUARE. Uniform 4px SOLO48 stroke.
Construction: Supplied front-car proportions and human round-ended anatomy; original mirrored hands.
Revision: Opened the windshield, restored tire shapes and paired lamps, and drew longer cupped hands.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f7acffbb-95f3-4cdd-98e2-2243774f9339'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-supporting-front-facing-car/20260928T173050Z-thuan-mac/reference/car insurance hands_f7acffbb-95f3-4cdd-98e2-2243774f9339.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hands-supporting-front-facing-car'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('hands', 'supporting', 'front', 'facing', 'car')

    def build(self):
        self.path('car',(11,13),(15,5),(33,5),(37,13),(37,22),(34,25,3,3,True),
                  (14,25),(11,22,3,3,True),(11,13),closed=True)
        self.add_line('windshield',(11,13),(37,13));self.relate('connect','car','windshield')
        for name,x in [('left',16),('right',30)]:
            self.add_line(name+'-wheel',(x,25),(x,28));self.relate('connect','car',name+'-wheel')
            self.add_dot(name+'-lamp',(x,19))
        self.cups(27,44)

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
Drawing.exception = {'reason': 'Preserve front-car windshield, lamps, tires and supporting hands. Tight anatomical finger gaps and hand-to-car support read clearly at native size; accept local spacing and wider envelope findings.', 'approved_by': 'gpt-6 under explicit user-delegated exception authority', 'approved_on': '2026-09-29', 'svg_sha256': '988a6f2c59849309cc1b21e84346e3a3e0d408638e70a3a89ee25748642c972f'}
