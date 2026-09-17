"""Lucky Four Leaf Clover.
Symbol plan: Four heart leaves form a symmetric clover. SQUARE (6,6)-(42,42). Lucide clover informs one lobed outer contour with shared radial seams. Rotate one double-lobe symbol four times; omit stem as in source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b25e1910-2311-4e75-9f49-087d0602797a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/casino lucky clover_b25e1910-2311-4e75-9f49-087d0602797a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'four-heart-shaped-clover-leaves-meeting-at-center'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('lucky', 'four', 'leaf', 'clover')

    def build(self):
        # One symmetric heart-lobe pair, rotated about the shared central cross.
        for q in range(4):
         def p(x,y):
          for _ in range(q):x,y=48-y,x
          return (x,y)
         self.add_bezier(f'leaf-{q}',p(24,12),(p(24,8),p(27,6),p(30,6)),(p(34,6),p(38,10),p(35,13)),(p(38,10),p(42,14),p(42,18)),(p(42,21),p(40,24),p(36,24)))
        self.add_contour('leaves',*[f'leaf-{q}' for q in range(4)],closed=True)
        self.add_polyline('vertical',(24,12),(24,24),(24,36))
        self.add_polyline('horizontal',(12,24),(24,24),(36,24))
        self.relate('connect','vertical','leaves');self.relate('connect','horizontal','leaves');self.relate('connect','vertical','horizontal')

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
