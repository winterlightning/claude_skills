"""Movie Theater Audience.
Symbol plan: Two seated cinema viewers below a triangular projection. SQUARE (6,6)-(42,42) spans the staggered scene. human_ref/full_body_ref.png informs round heads and simple seated limbs. Both radius3 heads have torso junctions exactly8 below their lower outlines. No useful exact Lucide scene match. Omit separate chair outlines to preserve two distinct seated poses.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '789e653d-66aa-4eb4-b270-e57d68cf2362'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/movie audience_789e653d-66aa-4eb4-b270-e57d68cf2362.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-seated-viewers-beneath-triangular-projection'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('movie', 'theater', 'audience')

    def build(self):
        self.add_polyline('projection',(6,6),(42,6),(42,16),closed=True)
        for n,cx,cy,jy,hy,kx in [('left',12,20,31,37,22),('right',30,25,36,39,40)]:
         self.circle(n+'-head',cx,cy,3)
         self.add_line(n+'-torso',(cx,jy),(cx,hy))
         self.add_polyline(n+'-legs',(cx,hy),(kx,hy),(kx,42));self.relate('connect',n+'-torso',n+'-legs')
         self.mark_human_figure(n,head=n+'-head',torso=n+'-torso',torso_junction='start')

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
