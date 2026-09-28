"""Marionette Puppet with Control Strings.
Symbol plan: Marionette suspended from crossed controls. VRECT_L (8,4)-(40,44) gives strings height. human_ref/full_body_ref.png circular head and spare limbs; radius3 head (24,21), torso junction (24,32), exactly8 centerline/4 ink gap. No useful exact Lucide match. Preserve crossbars, two strings and splayed pose; omit clothing and joint detail.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6d15a563-3b53-5c98-9c19-753f5d8814f8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/puppet_6d15a563-3b53-5c98-9c19-753f5d8814f8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'marionette-suspended-from-crossed-control-bars'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    categories = ("entertainment", "primitives")
    aliases = ()
    keywords = ('marionette', 'puppet', 'with', 'control', 'strings')

    def build(self):
        self.add_polyline('bar-one',(8,4),(24,8),(40,12))
        self.add_polyline('bar-two',(8,12),(24,8),(40,4));self.relate('connect','bar-one','bar-two')
        self.circle('head',24,21,3)
        self.add_polyline('arms',(8,36),(16,32),(24,32),(32,32),(40,28))
        self.add_line('torso',(24,32),(24,36));self.relate('connect','torso','arms')
        self.add_polyline('legs',(12,44),(24,36),(34,44));self.relate('connect','legs','torso')
        self.add_line('left-string',(8,12),(8,36));self.relate('connect','left-string','bar-two');self.relate('connect','left-string','arms')
        self.add_line('right-string',(40,12),(40,28));self.relate('connect','right-string','bar-one');self.relate('connect','right-string','arms')
        self.mark_human_figure('puppet',head='head',torso='torso',torso_junction='start')

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
