"""Person Celebrating with Bottle.
Symbol plan: Celebrating figure raises diagonal bottle. SQUARE (6,6)-(42,42) spans the gesture. human_ref/full_body_ref.png informs circular head and bent limbs: radius4 head (14,12), vertical torso tangent at (14,24), exactly8 centerline/4 ink gap. No useful exact Lucide match. Preserve raised bottle and splayed legs; reduce bottle neck to a stroke and omit clothing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8d49ce4-e7f0-58f5-b0a4-b166e1534148'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/party dance_e8d49ce4-e7f0-58f5-b0a4-b166e1534148.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-raising-bottle-in-outstretched-hand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('person', 'celebrating', 'with', 'bottle')

    def build(self):
        self.circle('head',14,12,4)
        self.add_bezier('torso',(14,24),((14,28),(14,32),(16,34)))
        self.add_polyline('left-arm',(14,24),(6,34));self.relate('connect','left-arm','torso')
        self.add_polyline('right-arm',(14,24),(24,26),(30,18));self.relate('connect','right-arm','torso');self.relate('connect','right-arm','left-arm')
        self.add_polyline('legs',(12,42),(16,34),(28,42));self.relate('connect','legs','torso')
        self.add_polyline('bottle',(32,8),(26,14),(30,18),(34,22),(40,16),(36,12),closed=True)
        self.relate('connect','bottle','right-arm')
        self.add_line('neck',(36,12),(42,6));self.relate('connect','neck','bottle')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

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
