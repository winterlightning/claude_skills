"""Variable Capacitor Symbol.
Symbol plan: Variable capacitor with adjustment arrow interrupted at the plates as in reference. SQUARE (6,6)-(42,42) balances leads and diagonal. No useful exact Lucide match. Preserve two plates, two leads, and arrow.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '905a48d0-c85b-49ef-816e-822449f42ce6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/variable capacitor_905a48d0-c85b-49ef-816e-822449f42ce6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'capacitor-plates-crossed-by-diagonal-adjustment-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "electronics"
    categories = ("electronics", "primitives")
    aliases = ()
    keywords = ('variable', 'capacitor', 'symbol')

    def build(self):
        self.add_polyline('upper-plate',(6,22),(22,22),(24,22),(42,22))
        self.add_polyline('lower-plate',(6,30),(24,30),(30,30),(42,30))
        for name,y,end in [('upper',22,6),('lower',30,42)]:
         self.add_line(name+'-lead',(24,y),(24,end));self.relate('connect',name+'-lead',name+'-plate')
        self.add_line('arrow-upper',(22,22),(6,6));self.relate('connect','arrow-upper','upper-plate')
        self.add_polyline('arrowhead',(6,14),(6,6),(14,6));self.relate('connect','arrowhead','arrow-upper')
        self.add_line('arrow-lower',(30,30),(42,42));self.relate('connect','arrow-lower','lower-plate')

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
