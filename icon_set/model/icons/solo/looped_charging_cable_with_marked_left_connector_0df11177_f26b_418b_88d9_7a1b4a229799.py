"""Thunderbolt Charging Power Cable.
Symbol plan: Cable with deep U and tall arch, two opposing connector housings. SQUARE extremes (6,6)-(42,42). Lucide cable: tangent semicircles. Drop tiny connector marking and stacked tip divisions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0df11177-f26b-418b-88d9-7a1b4a229799'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/thunderbolt cable_0df11177-f26b-418b-88d9-7a1b4a229799.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'looped-charging-cable-with-marked-left-connector'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "electronics"
    categories = ("electronics", "primitives")
    aliases = ()
    keywords = ('thunderbolt', 'charging', 'power', 'cable')

    def build(self):
        self.rounded('left-plug',6,6,14,22,2,nodes=((10,22),))
        self.rounded('right-plug',34,26,42,42,2,nodes=((38,26),))
        self.add_line('left-wire',(10,22),(10,35))
        self.add_arc('u',(10,35),(24,35),radius_x=7,sweep=False)
        self.add_line('middle-wire',(24,35),(24,13))
        self.add_arc('arch',(24,13),(38,13),radius_x=7,sweep=True)
        self.add_line('right-wire',(38,13),(38,26))
        self.add_contour('cable','left-wire','u','middle-wire','arch','right-wire')
        self.relate('connect','cable','left-plug');self.relate('connect','cable','right-plug')

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
