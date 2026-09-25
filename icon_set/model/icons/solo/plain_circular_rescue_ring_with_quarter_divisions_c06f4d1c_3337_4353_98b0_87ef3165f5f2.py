"""Simple Circular Life Buoy.
Symbol plan: Circular rescue ring with four cardinal divisions. CIRCLE radius20 about (24,24) directly matches round subject. Lucide life-buoy informs concentric rings and attached radial seams. Preserve all features, radius10 inner opening and four shared division nodes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c06f4d1c-3337-4353-98b0-87ef3165f5f2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/casino chip_c06f4d1c-3337-4353-98b0-87ef3165f5f2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plain-circular-rescue-ring-with-quarter-divisions'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    categories = ("entertainment", "state")
    aliases = ()
    keywords = ('simple', 'circular', 'life', 'buoy')

    def build(self):
        for name,r in [('outer',20),('inner',10)]:
         points=[(24,24-r),(24+r,24),(24,24+r),(24-r,24)]
         for i,p in enumerate(points):self.add_arc(f'{name}-{i}',p,points[(i+1)%4],radius_x=r)
         self.add_contour(name,*[f'{name}-{i}' for i in range(4)],closed=True)
        for i,(a,z) in enumerate([((24,4),(24,14)),((44,24),(34,24)),((24,44),(24,34)),((4,24),(14,24))]):
         self.add_line(f'band-{i}',a,z)
         for ring in ('outer','inner'):self.relate('connect',f'band-{i}',ring)

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
