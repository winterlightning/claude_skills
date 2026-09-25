"""Smiling Clown Face.
Symbol plan: Round smiling clown with crossed eyes and round nose. CIRCLE radius20 at (24,24) leaves room for the face. human_ref/user.svg circular face construction; no body is shown. No useful exact Lucide clown match. Reduce eye crosses to compact dots and omit outer hair tufts to preserve nose and smile at 48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c59046e8-6966-5ded-bac4-8a7f1eee68c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/circus clown_c59046e8-6966-5ded-bac4-8a7f1eee68c9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-smiling-clown-with-crossed-eyes-and-big-nose'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    aliases = ()
    keywords = ('smiling', 'clown', 'face')

    def build(self):
        self.circle('face',24,24,20)
        for x in (16,32):self.add_dot(f'eye-{x}',(x,16))
        self.circle('nose',24,23,2)
        self.add_arc('smile',(18,32),(30,32),radius_x=10,sweep=False)

    def rounded(self, name, l, t, r, b, radius, nodes=()):
        # One radius owns all tangent corners; split straight walls at real joins.
        pts=[(l+radius,t),(r-radius,t),(r,t+radius),(r,b-radius),
             (r-radius,b),(l+radius,b),(l,b-radius),(l,t+radius)]
        members=[]
        for i,a in enumerate(pts):
            z=pts[(i+1)%8]; part=f"{name}-{i}"
            if i%2:
                self.add_arc(part,a,z,radius_x=radius)
                members.append(part)
            else:
                on=[p for p in nodes if p!=a and p!=z and
                    (z[0]-a[0])*(p[1]-a[1])==(z[1]-a[1])*(p[0]-a[0]) and
                    min(a[0],z[0])<=p[0]<=max(a[0],z[0]) and min(a[1],z[1])<=p[1]<=max(a[1],z[1])]
                on.sort(key=lambda p:(p[0]-a[0])**2+(p[1]-a[1])**2)
                path=[a,*on,z]
                for j,(v,w) in enumerate(zip(path,path[1:])):
                    if v==w: continue
                    member=f"{part}-{j}";self.add_line(member,v,w);members.append(member)
        self.add_contour(name,*members,closed=True)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
