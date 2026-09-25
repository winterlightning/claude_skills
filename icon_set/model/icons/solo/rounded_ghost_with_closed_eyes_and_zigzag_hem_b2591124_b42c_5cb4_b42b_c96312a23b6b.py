"""Ghost Icon with Closed Eyes.
Symbol plan: Domed ghost with closed eyes and angular hem. VRECT_L (8,4)-(40,44) suits the upright silhouette. Lucide ghost informs radius16 cap and simple continuous outline. Mirrored eye curves and hem; reduce five jagged tips to three broad points to preserve negative space.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b2591124-b42c-5cb4-b42b-c96312a23b6b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/chewbacca wookiee_b2591124-b42c-5cb4-b42b-c96312a23b6b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-ghost-with-closed-eyes-and-zigzag-hem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    aliases = ()
    keywords = ('ghost', 'icon', 'with', 'closed', 'eyes')

    def build(self):
        self.add_arc('dome',(8,20),(40,20),radius_x=16)
        self.add_polyline('hem',(40,20),(40,40),(32,36),(24,44),(16,36),(8,40),(8,20))
        self.contours.clear();self.add_contour('ghost','dome',*[f'hem-{i}' for i in range(1,7)],closed=True)
        for x in (19,29):self.add_bezier(f'eye-{x}',(x-1,23),((x-1,22),(x+1,22),(x+1,23)))

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
