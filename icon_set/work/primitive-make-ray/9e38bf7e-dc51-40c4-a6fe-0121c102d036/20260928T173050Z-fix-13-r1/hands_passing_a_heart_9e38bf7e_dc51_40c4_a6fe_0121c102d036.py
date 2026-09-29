"""Heart between upper giving hand and lower open palm, with intentional diagonal movement.
Keyshape: SQUARE. Uniform 4px SOLO48 stroke.
Construction: Lucide hand-heart original and atomic-debug: open palm, rounded thumb and legible heart.
Revision: Redrew both hands as continuous open palms and placed a clear heart between them.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9e38bf7e-dc51-40c4-a6fe-0121c102d036'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-passing-a-heart/20260928T173050Z-thuan-mac/reference/donation charity hand give heart_9e38bf7e-dc51-40c4-a6fe-0121c102d036.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hands-passing-a-heart'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('hands', 'passing', 'a', 'heart')

    def build(self):
        self.path('heart',(23,21),(16,21,20,17,16,17),(23,29,14,23,18,26),
                  (30,21,28,26,32,23),(23,21,30,17,26,17),closed=True)
        self.path('lower',(4,33),(13,33),(20,38,17,33,19,36),(29,38),
                  (37,44,34,38,36,41),(4,44))
        self.add_line('palm',(15,38),(20,38));self.relate('connect','lower','palm')
        self.path('upper',(44,4),(32,4),(24,10,28,4,25,7))
        self.path('upper-thumb',(44,14),(39,14),(34,20),
                  (29,16,30,24,26,19),(32,12),(28,10,31,9,30,9))

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
