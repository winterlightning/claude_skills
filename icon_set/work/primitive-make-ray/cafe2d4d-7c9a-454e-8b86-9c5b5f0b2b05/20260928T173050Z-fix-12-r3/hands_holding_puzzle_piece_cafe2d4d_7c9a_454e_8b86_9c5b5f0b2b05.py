"""Diagonal puzzle piece above mirrored cupped hands, preserving its tab and inward socket.
Keyshape: SQUARE. Uniform 4px SOLO48 stroke.
Construction: Human round-ended limb vocabulary; source diagonal puzzle and hand arrangement.
Revision: Restored diagonal puzzle silhouette with a tab and socket, and redrew articulated cupped hands.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cafe2d4d-7c9a-454e-8b86-9c5b5f0b2b05'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-holding-puzzle-piece/20260928T173050Z-thuan-mac/reference/module hands puzzle_cafe2d4d-7c9a-454e-8b86-9c5b5f0b2b05.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hands-holding-puzzle-piece'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('hands', 'holding', 'puzzle', 'piece')

    def build(self):
        self.path('piece',(22,6),(27,11),
                  (35,10,28,4,35,4),(30,15,35,14,32,16),(35,20),(24,31),(11,18),(15,14),
                  (20,9,22,21,27,13),(22,6),closed=True)
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
            self.path(side+'-hand',p(11,bottom),c(4,top+9,11,bottom-4,4,top+14),p(4,top),
                      (*p(10,top),3,3,s==1),p(10,top+7),
                      c(14,top+5,10,top+4,12,top+3),p(18,top+10),
                      c(20,top+14,19,top+11,20,top+12),p(20,bottom))
            self.add_line(side+'-thumb-crease',p(10,top+7),p(14,top+12))
            self.relate('connect',side+'-hand',side+'-thumb-crease')
