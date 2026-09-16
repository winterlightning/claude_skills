"""Diagonal DNA Helix with End Rungs.

Symbol plan: Two tangent cubic strands cross at shared nodes along a diagonal. Two end rungs and a broad central opening preserve the double helix.
Lucide: dna; original and atomic-debug geometry inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f8bad55-2188-449b-86bc-2964af338a2e'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/dna_0f8bad55-2188-449b-86bc-2964af338a2e.svg'
AUTHOR = 'gpt-6'


class DiagonalDnaHelixWithEndRungs(Solo48):
    icon_id = 'diagonal-dna-helix-with-end-rungs'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('dna', 'helix', 'genetics', 'biology', 'chromosome', 'molecule', 'science', 'heredity')

    def build(self):
        # Reflect one strand across x+y=48; knots and tangents remain shared.
        steps=((18,30,10,26,14,26),(30,30,22,34,27,33),(30,18,33,27,34,22),(30,6,26,14,26,10))
        for n,mirror in [('a',False),('b',True)]:
            def p(x,y):return (48-y,48-x) if mirror else (x,y)
            reflected=[(*p(s[0],s[1]),*p(s[2],s[3]),*p(s[4],s[5])) for s in steps]
            self.path('strand-'+n,p(6,30),*reflected)
        self.relate('connect','strand-a','strand-b')
        for n,a,z in [('bottom',(6,30),(18,42)),('top',(30,6),(42,18))]:
            self.add_line(n+'-rung',a,z)
            self.relate('connect',n+'-rung','strand-a');self.relate('connect',n+'-rung','strand-b')

    def path(self, name, start, *steps, closed=False):
        members=[]
        point=start
        for index, step in enumerate(steps):
            member=f"{name}-{index+1}"
            if len(step)==2:
                self.add_line(member,point,step)
                point=step
            elif len(step)==5:
                x,y,rx,ry,sweep=step
                self.add_arc(member,point,(x,y),radius_x=rx,radius_y=ry,sweep=sweep)
                point=(x,y)
            else:
                x,y,cx1,cy1,cx2,cy2=step
                self.add_bezier(member,point,((cx1,cy1),(cx2,cy2),(x,y)))
                point=(x,y)
            members.append(member)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x,y-r),(x+r,y,r,r,True),(x,y+r,r,r,True),
                  (x-r,y,r,r,True),(x,y-r,r,r,True),closed=True)

    def rect(self,name,x,y,w,h,r=2):
        self.path(name,(x+r,y),(x+w-r,y),(x+w,y+r,r,r,True),
                  (x+w,y+h-r),(x+w-r,y+h,r,r,True),(x+r,y+h),
                  (x,y+h-r,r,r,True),(x,y+r),(x+r,y,r,r,True),closed=True)
