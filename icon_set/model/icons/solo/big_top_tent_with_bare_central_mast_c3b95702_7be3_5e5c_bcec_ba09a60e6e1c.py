"""Big Top Circus Tent.
Symbol plan: Big-top tent with bare mast, curved roof and arched entrance. SQUARE (6,6)-(42,42) balances roof and skirt. Lucide tent informs mirrored structural layout; source owns curved circus roof. Shared mirrored controls and radius6 doorway.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3b95702-7be3-5e5c-bcec-ba09a60e6e1c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/circus tent_c3b95702-7be3-5e5c-bcec-ba09a60e6e1c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'big-top-tent-with-bare-central-mast'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('big', 'top', 'circus', 'tent')

    def build(self):
        self.add_bezier('roof-left',(8,24),((14,22),(20,18),(24,12)))
        self.add_bezier('roof-right',(24,12),((28,18),(34,22),(40,24)))
        self.add_polyline('right-wall',(40,24),(42,42),(30,42),(30,38))
        self.add_arc('door-right',(30,38),(24,32),radius_x=6,sweep=False)
        self.add_arc('door-left',(24,32),(18,38),radius_x=6,sweep=False)
        self.add_polyline('left-wall',(18,38),(18,42),(6,42),(8,24))
        self.contours.clear()
        self.add_contour('tent','roof-left','roof-right',*[f'right-wall-{i}' for i in range(1,4)],'door-right','door-left',*[f'left-wall-{i}' for i in range(1,4)],closed=True)
        self.add_line('eave',(8,24),(40,24));self.relate('connect','eave','tent')
        self.add_line('mast',(24,6),(24,12));self.relate('connect','mast','tent')

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
