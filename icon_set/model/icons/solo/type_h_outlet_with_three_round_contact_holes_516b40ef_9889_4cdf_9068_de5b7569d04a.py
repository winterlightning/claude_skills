"""Type H Electrical Power Outlet.
Symbol plan: Type H round recess and downward triangular contacts. CIRCLE radius20 at (24,24); omit secondary plate. Preserve all three circles with one shared radius.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '516b40ef-9889-4cdf-9068-de5b7569d04a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/power outlet type h_516b40ef-9889-4cdf-9068-de5b7569d04a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'type-h-outlet-with-three-round-contact-holes'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/electronics"
    aliases = ()
    keywords = ('type', 'h', 'electrical', 'power', 'outlet')

    def build(self):
        self.circle('recess',24,24,20)
        for i,(x,y) in enumerate(((16,20),(32,20),(24,32))):self.circle(f'contact-{i}',x,y,2)

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
