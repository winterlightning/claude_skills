"""A left-facing head profile has three curved connections branching from its open upper-right section. Each branch ends in a small circle, while the face retains a nose, chin and short neck.
Symbol plan: Left-facing human head silhouette with three circular neural terminals on the open back. Three branches share root (26,24); smooth quarter-circle turns and radius-2 nodes preserve the circuit topology. No detached body.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: git-branch; local original and atomic geometry inspected for Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b629a3fa-3ca7-4b1e-97fa-bddfb9e31f58'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/head ai neurolink_b629a3fa-3ca7-4b1e-97fa-bddfb9e31f58.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'neural-head-profile-with-branching-nodes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('neural', 'head', 'profile', 'with', 'branching', 'nodes')

    def build(self):

        def segments(name,*points):
            for j,(a,b) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{j}',a,b)

        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def rect(name,l,t,r,b,q=0):
            if not q:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
                return
            points=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
            ids=[]
            for j,(a,z) in enumerate(zip(points,points[1:])):
                if a==z:continue
                n=f'{name}-{j}'
                if j%2:self.add_arc(n,a,z,radius_x=q)
                else:self.add_line(n,a,z)
                ids.append(n)
            self.add_contour(name,*ids,closed=True)

        self.add_arc('cranium',(20,6),(8,18),radius_x=12,sweep=False)
        segments('face',(8,18),(8,22),(6,30),(10,30),(10,32))
        self.add_arc('chin',(10,32),(14,36),radius_x=4,sweep=False)
        segments('neck',(14,36),(18,36),(18,42))
        self.add_contour('profile','cranium','face-1','face-2','face-3','face-4','chin','neck-1','neck-2')
        self.add_line('upper-stem',(26,24),(26,16))
        self.add_arc('upper-turn',(26,16),(34,8),radius_x=8)
        self.add_line('upper-end',(34,8),(36,8))
        self.add_contour('upper','upper-stem','upper-turn','upper-end')
        self.add_line('middle',(26,24),(38,24))
        self.add_line('lower-stem',(26,24),(26,30))
        self.add_arc('lower-turn',(26,30),(34,38),radius_x=8,sweep=False)
        self.add_line('lower-end',(34,38),(36,38))
        self.add_contour('lower','lower-stem','lower-turn','lower-end')
        for a,b in [('upper','middle'),('upper','lower'),('middle','lower')]:self.relate('connect',a,b)
        for n,x,y,branch in [('top',38,8,'upper'),('mid',40,24,'middle'),('low',38,38,'lower')]:
         circle(n,x,y,2);self.relate('connect',n,branch)
        self.add_line('back-neck',(38,40),(38,42))
        self.relate('connect','back-neck','low')
