"""Type B Electrical Socket.
Symbol plan: Type B recess, paired slots and arched ground. VRECT_L (8,4)-(40,44) gives the grounding arch room; omit secondary outer plate. Lucide square informs symmetric enclosure.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5b5a5348-95e6-489c-abb3-fe356243022b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__type-b-outlet-with-two-slots-and-ground-hole/20260927T101610Z-thuan-mac-1/reference/power outlet type b_5b5a5348-95e6-489c-abb3-fe356243022b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'type-b-outlet-with-two-slots-and-ground-hole'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "electronics"
    categories = ("electronics", "primitives")
    aliases = ()
    keywords = ('type', 'b', 'electrical', 'socket')

    def build(self):
        # The rejected recess read as a face. Frame the two slots and ground as a wall plate.
        self.rounded('wall-plate',6,6,42,42,6)
        for x in (18,30):
            self.add_line(f'slot-{x}',(x,15),(x,20))
        self.add_arc('ground-upper',(22,31),(26,31),radius_x=2)
        self.add_arc('ground-lower',(26,31),(22,31),radius_x=2)
        self.add_contour('ground','ground-upper','ground-lower',closed=True)

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
