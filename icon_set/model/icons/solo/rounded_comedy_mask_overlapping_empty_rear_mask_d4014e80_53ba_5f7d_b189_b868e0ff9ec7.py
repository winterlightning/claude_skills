"""Happy Theater Comedy Masks.
Symbol plan: Overlapping theater masks with a rounded front chin. SQUARE (6,6)-(42,42) balances the pair. Lucide drama informs partial rear mask and spare expression. Straight parallel rims and short eyes replace crowded dipped rims and closed-eye arcs; retain smile and rounded chin, distinct from pointed companion. Intentional upper-left overlap follows reference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd4014e80-53ba-5f7d-b189-b868e0ff9ec7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/show theater mask happy_d4014e80-53ba-5f7d-b189-b868e0ff9ec7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-comedy-mask-overlapping-empty-rear-mask'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('happy', 'theater', 'comedy', 'masks')

    def build(self):
        self.add_line('rear-top',(6,6),(34,6))
        self.add_bezier('rear-left',(6,6),((6,18),(6,25),(12,28)))
        self.add_contour('rear','rear-top');self.relate('connect','rear-left','rear')
        self.add_line('front-top',(12,14),(42,14))
        self.add_line('front-right',(42,14),(42,28))
        self.add_bezier('chin-right',(42,28),((42,38),(35,42),(27,42)))
        self.add_bezier('chin-left',(27,42),((19,42),(12,38),(12,28)))
        self.add_line('front-left',(12,28),(12,14))
        self.add_contour('front','front-top','front-right','chin-right','chin-left','front-left',closed=True)
        self.relate('connect','rear-left','front')
        for x in (21,33):self.add_line(f'eye-{x}',(x,23),(x,24))
        self.add_bezier('smile',(24,32),((26,34),(28,34),(30,32)))

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
