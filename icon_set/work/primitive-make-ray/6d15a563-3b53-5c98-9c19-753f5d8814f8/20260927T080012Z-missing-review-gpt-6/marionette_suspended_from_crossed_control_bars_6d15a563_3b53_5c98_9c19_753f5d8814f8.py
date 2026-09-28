"""Revision of marionette-suspended-from-crossed-control-bars. Replaced the rejected boxlike puppet with angled suspension strings, a larger open head, an articulated arm span, and splayed legs.
Symbol plan: redraw the original subject with one coherent SOLO48 construction.
"""
"""Marionette Puppet with Control Strings.
Symbol plan: Marionette suspended from crossed controls. VRECT_L (8,4)-(40,44) gives strings height. human_ref/full_body_ref.png circular head and spare limbs; radius3 head (24,21), torso junction (24,32), exactly8 centerline/4 ink gap. No useful exact Lucide match. Preserve crossbars, two strings and splayed pose; omit clothing and joint detail.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6d15a563-3b53-5c98-9c19-753f5d8814f8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__marionette-suspended-from-crossed-control-bars/20260927T074149Z-thuan-mac-1/reference/puppet_6d15a563-3b53-5c98-9c19-753f5d8814f8.svg'
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
        self.add_polyline('bar-one',(8,4),(24,6),(40,10))
        self.add_polyline('bar-two',(8,10),(24,6),(40,4))
        self.relate('connect','bar-one','bar-two')
        self.circle('head',24,20,4)
        self.add_polyline('arms',(10,34),(16,32),(24,32),(32,30),(40,30))
        self.add_line('torso',(24,32),(24,36))
        self.relate('connect','torso','arms')
        self.add_polyline('legs',(12,44),(24,36),(36,44))
        self.relate('connect','legs','torso')
        self.add_line('left-string',(8,10),(10,34))
        self.relate('connect','left-string','bar-two')
        self.relate('connect','left-string','arms')
        self.add_line('right-string',(40,10),(40,30))
        self.relate('connect','right-string','bar-one')
        self.relate('connect','right-string','arms')
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
