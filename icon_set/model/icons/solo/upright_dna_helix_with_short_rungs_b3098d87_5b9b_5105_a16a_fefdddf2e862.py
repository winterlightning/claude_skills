"""Upright DNA Helix with Short Rungs.

Symbol plan: Mirrored smooth strands form an upright helix with a wide middle loop. Three short rungs alternate sides; small crowded rung fragments are omitted.
Lucide: dna; original and atomic-debug geometry inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3098d87-5b9b-5105-a16a-fefdddf2e862'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/dna_b3098d87-5b9b-5105-a16a-fefdddf2e862.svg'
AUTHOR = 'gpt-6'


class UprightDnaHelixWithShortRungs(Solo48):
    icon_id = 'upright-dna-helix-with-short-rungs'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    aliases = ()
    keywords = ('dna', 'helix', 'genetics', 'biology', 'chromosome', 'molecule', 'science', 'heredity')

    def build(self):
        axis=24
        for n,mirror in [('a',False),('b',True)]:
            def p(x,y):return (2*axis-x if mirror else x,y)
            def bez(end,c1,c2):return (*p(*end),*p(*c1),*p(*c2))
            self.path('strand-'+n,p(8,4),bez((24,14),(8,10),(16,10)),bez((40,24),(32,18),(40,18)),bez((24,34),(40,30),(32,30)),bez((8,44),(16,38),(8,38)))
        self.relate('connect','strand-a','strand-b')
        for n,a,z in [('top',(8,4),(18,4)),('middle',(40,24),(28,24)),('bottom',(8,44),(18,44))]:
            self.add_line(n+'-rung',a,z);self.relate('connect',n+'-rung','strand-a')

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
