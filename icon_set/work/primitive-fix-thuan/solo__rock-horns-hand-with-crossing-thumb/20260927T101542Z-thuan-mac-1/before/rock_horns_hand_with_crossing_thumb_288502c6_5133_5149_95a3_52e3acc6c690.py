"""Rock On Hand Gesture.
Symbol plan: Rock horns with two raised fingers and crossing thumb. VRECT_L (8,4)-(40,44) gives fingers height. human_ref/full_body_ref.png informs simplified human part; Lucide hand informs round finger tips and continuous palm. Shared radius4 fingers; shorter little finger intentionally asymmetric. Omit middle-finger divisions and short palm crease.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '288502c6-5133-5149-95a3-52e3acc6c690'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/concert rock_288502c6-5133-5149-95a3-52e3acc6c690.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rock-horns-hand-with-crossing-thumb'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    categories = ("entertainment", "primitives")
    aliases = ()
    keywords = ('rock', 'on', 'hand', 'gesture')

    def build(self):
        self.add_arc('index-tip',(8,8),(16,8),radius_x=4)
        self.add_polyline('knuckles',(16,8),(16,24),(32,24),(32,16))
        self.add_arc('little-tip',(32,16),(40,16),radius_x=4)
        self.add_line('right-palm',(40,16),(40,32));self.add_arc('palm-bottom',(40,32),(28,44),radius_x=12)
        self.add_bezier('left-palm',(28,44),((16,44),(8,42),(8,32)))
        self.add_line('left-wall',(8,32),(8,8))
        parts=['index-tip','knuckles','little-tip','right-palm','palm-bottom','left-palm','left-wall']
        for a,b in zip(parts,parts[1:]+parts[:1]):self.relate('connect',a,b)
        self.add_polyline('thumb',(8,32),(20,32),(22,34))
        self.relate('connect','thumb','left-palm');self.relate('connect','thumb','left-wall')

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
