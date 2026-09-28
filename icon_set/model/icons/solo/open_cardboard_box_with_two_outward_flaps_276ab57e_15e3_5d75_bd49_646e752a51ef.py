"""Open Cardboard Box.
Symbol plan: Open box in symmetric perspective with two broad outward flaps. HRECT_L (4,8)-(44,40) gives flaps breadth. Lucide package-open: coherent folds and shared corner junctions. Drop minor corner rounding.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '276ab57e-15e3-5d75-bd49-646e752a51ef'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/emails/open_276ab57e-15e3-5d75-bd49-646e752a51ef.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-cardboard-box-with-two-outward-flaps'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "emails"
    categories = ("emails", "primitives")
    aliases = ()
    keywords = ('open', 'cardboard', 'box')

    def build(self):
        self.add_polyline('back-rim',(12,12),(24,8),(36,12))
        self.add_polyline('front-rim',(12,12),(24,18),(36,12));self.relate('connect','back-rim','front-rim')
        for side,sgn in [('left',-1),('right',1)]:
         p=lambda x,y:(24+sgn*x,y)
         self.add_polyline(side+'-flap',p(12,12),p(20,20),p(16,22),p(8,26),(24,18))
         self.relate('connect',side+'-flap','front-rim');self.relate('connect',side+'-flap','back-rim')
        self.relate('connect','left-flap','right-flap')
        self.add_polyline('walls',(8,22),(8,32),(24,40),(40,32),(40,22))
        for side in ('left','right'):self.relate('connect','walls',side+'-flap')
        self.add_line('corner',(24,18),(24,40));self.relate('connect','corner','front-rim');self.relate('connect','corner','walls')
        for side in ('left','right'):self.relate('connect','corner',side+'-flap')

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
