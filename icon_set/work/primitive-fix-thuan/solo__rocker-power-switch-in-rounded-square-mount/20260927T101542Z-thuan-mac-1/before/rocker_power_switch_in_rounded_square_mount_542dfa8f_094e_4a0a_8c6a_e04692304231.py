"""Rocker Power Switch.
Symbol plan: Rocker switch with slanted upper face and lower face. SQUARE extremes (6,6)-(42,42). Omit secondary plate; Lucide square informs tangent bottom corners.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '542dfa8f-094e-4a0a-8c6a-e04692304231'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/rocker switch_542dfa8f-094e-4a0a-8c6a-e04692304231.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rocker-power-switch-in-rounded-square-mount'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "electronics"
    categories = ("electronics", "primitives")
    aliases = ()
    keywords = ('rocker', 'power', 'switch')

    def build(self):
        self.add_polyline('upper',(6,26),(14,6),(42,6),(34,26),(6,26))
        self.add_line('right',(34,26),(34,38));self.add_arc('br',(34,38),(30,42),radius_x=4)
        self.add_line('bottom',(30,42),(10,42));self.add_arc('bl',(10,42),(6,38),radius_x=4)
        self.add_line('left',(6,38),(6,26));self.add_contour('lower','right','br','bottom','bl','left')
        self.relate('connect','upper','lower')

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
