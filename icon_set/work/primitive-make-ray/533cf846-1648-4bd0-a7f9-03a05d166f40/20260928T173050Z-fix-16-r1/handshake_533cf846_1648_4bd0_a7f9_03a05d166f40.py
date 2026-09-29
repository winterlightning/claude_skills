"""Two overlapping palms with a rounded thumb, two finger turns and paired short cuffs.
Keyshape: HRECT_M. Uniform 4px SOLO48 stroke.
Construction: Lucide handshake original and atomic-debug: overlapping thumb, tangent finger curls and paired cuffs.
Revision: Rebuilt a natural overlapping thumb and smooth joined fingers with matched short cuffs.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '533cf846-1648-4bd0-a7f9-03a05d166f40'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__handshake/20260928T173050Z-thuan-mac/reference/handshake_533cf846-1648-4bd0-a7f9-03a05d166f40.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'handshake'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('handshake',)

    def build(self):
        self.path('left-cuff',(4,12),(9,12),(9,17),(9,29),(9,32),(4,32))
        self.path('right-cuff',(44,12),(39,12),(39,17),(39,29),(39,32),(44,32))
        self.path('left-top',(9,17),(18,13,12,17,15,13),(23,14,20,13,21,13))
        self.path('thumb',(39,17),(28,12),(23,14,26,11,25,12),(18,18),
                  (21,24,13,22,17,27),(27,21))
        self.path('fingers',(27,21),(35,29),(31,34,38,32,34,36),(27,30),
                  (23,37,31,35,27,41),(19,33),
                  (15,36,20,37,18,39),(9,29))
        self.path('right-palm',(39,29),(35,29))
        for a,b in [('left-cuff','left-top'),('left-top','thumb'),('thumb','right-cuff'),('thumb','fingers'),
                    ('fingers','left-cuff'),('fingers','right-palm'),('right-palm','right-cuff')]:self.relate('connect',a,b)

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
