"""Clown With Hat and Bowtie.
Symbol plan: Blank clown with circular jaw, rounded cap, pompom, side hair and broad bowtie. VRECT_L (8,4)-(40,44) accommodates the upright portrait. human_ref/user.svg informs radius10 circular head/jaw, full_body_ref.png informs spare human contours. No torso is drawn; bowtie is an accessory. No useful exact Lucide clown match. Shared mirrored hair and bowtie coordinates; omit knot and facial features as the reference face is blank.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7bd5382-1c27-528e-8b47-70ed1ee9ccd7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/circus clown_b7bd5382-1c27-528e-8b47-70ed1ee9ccd7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'blank-faced-clown-with-pompom-cap-and-bowtie'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('clown', 'with', 'hat', 'and', 'bowtie')

    def build(self):
        self.add_arc('cap-left',(14,19),(24,9),radius_x=10)
        self.add_arc('cap-right',(24,9),(34,19),radius_x=10)
        self.add_arc('jaw-right',(34,19),(24,29),radius_x=10)
        self.add_arc('jaw-left',(24,29),(14,19),radius_x=10)
        self.add_contour('head','cap-left','cap-right','jaw-right','jaw-left',closed=True)
        self.add_line('brim',(14,19),(34,19));self.relate('connect','brim','head')
        self.circle('pompom',24,6,2)
        self.add_line('cap-tip',(24,8),(24,9));self.relate('connect','cap-tip','pompom');self.relate('connect','cap-tip','head')
        self.add_bezier('hair-left',(14,11),((6,9),(6,19),(14,19)))
        self.add_bezier('hair-right',(34,11),((42,9),(42,19),(34,19)))
        self.relate('connect','hair-left','head');self.relate('connect','hair-right','head')
        self.add_polyline('bow-left',(24,40),(8,32),(8,44),closed=True)
        self.add_polyline('bow-right',(24,40),(40,32),(40,44),closed=True)
        self.relate('connect','bow-left','bow-right')

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
