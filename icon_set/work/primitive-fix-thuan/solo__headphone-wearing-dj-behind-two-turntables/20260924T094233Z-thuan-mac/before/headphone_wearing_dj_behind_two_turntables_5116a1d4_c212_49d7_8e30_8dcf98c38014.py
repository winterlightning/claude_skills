"""DJ with Headphones and Turntables.
Symbol plan: DJ with headphones behind a two-platter deck. VRECT_L (8,4)-(40,44) budgets height for head and console. human_ref/user.svg informs circular head radius6 centered (24,10), head bottom16 and broad shoulder/deck top24: exactly8 centerline /4 ink gap, analytically verified. Full_body_ref.png informs simple human outline. Lucide headphones informs arched upper headband and attached earpieces. Omit separate shoulder outline, consolidate it into broad console top, and simplify trapezoidal deck to rounded rectangle with two circular platter marks. Split tangent deck walls into connected exact primitives to certify the 8-unit platter inset without changing geometry or thresholds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5116a1d4-c212-49d7-8e30-8dcf98c38014'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/concert dj_5116a1d4-c212-49d7-8e30-8dcf98c38014.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'headphone-wearing-dj-behind-two-turntables'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('dj', 'with', 'headphones', 'and', 'turntables')

    def build(self):
        self.add_arc('head-top',(18,10),(30,10),radius_x=6)
        self.add_arc('head-bottom',(30,10),(18,10),radius_x=6)
        self.add_contour('head','head-top','head-bottom',closed=True)
        for side,x,z in [('left',18,10),('right',30,38)]:
         self.add_polyline('ear-'+side,(x,10),(z,10),(z,14));self.relate('connect','ear-'+side,'head')
        # The broad upper edge also describes the seated DJ shoulders.
        self.rounded('deck',8,24,40,44,4)
        # Separate tangent arcs and straight walls permit exact circle-line
        # clearance certification at the 8-unit contact-disc inset.
        self.contours=[c for c in self.contours if c.contour_id!='deck']
        walls=[f'deck-{i}' if i%2 else f'deck-{i}-0' for i in range(8)]
        for a,b in zip(walls,walls[1:]+walls[:1]):self.relate('connect',a,b)
        for x in (18,30):self.circle(f'disc-{x}',x,34,2)

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
