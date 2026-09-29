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
        self.path('car',(11,15),(15,5),(33,5),(37,15),(37,23),(34,26,3,3,True),
                  (14,26),(11,23,3,3,True),(11,15),closed=True)
        self.path('windshield',(11,15),(37,15));self.relate('connect','car','windshield')
        for name,x in [('left',15),('right',29)]:
            self.path(name+'-wheel',(x,26),(x,29),(x+4,29,2,2,False),(x+4,26))
            self.relate('connect','car',name+'-wheel')
            self.add_line(name+'-lamp',(x,21),(x+4,21))
        self.cups(33,44)

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
