"""Type B Electrical Socket.
Symbol plan: Type B recess, paired slots and arched ground. VRECT_L (8,4)-(40,44) gives the grounding arch room; omit secondary outer plate. Lucide square informs symmetric enclosure.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b5a5348-95e6-489c-abb3-fe356243022b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/power outlet type b_5b5a5348-95e6-489c-abb3-fe356243022b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'type-b-outlet-with-two-slots-and-ground-hole'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "electronics"
    aliases = ()
    keywords = ('type', 'b', 'electrical', 'socket')

    def build(self):
        self.rounded('recess',8,4,40,44,12)
        for x in (17,31):self.add_line(f'slot-{x}',(x,15),(x,18))
        self.add_arc('ground-top',(18,31),(30,31),radius_x=6)
        self.add_polyline('ground-bottom',(30,31),(30,35),(18,35),(18,31))
        self.contours=[c for c in self.contours if c.contour_id!='ground-bottom']
        self.add_contour('ground','ground-top','ground-bottom-1','ground-bottom-2','ground-bottom-3',closed=True)

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
