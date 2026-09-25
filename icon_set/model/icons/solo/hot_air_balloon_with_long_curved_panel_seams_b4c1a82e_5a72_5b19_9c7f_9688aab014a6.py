"""Simple Hot Air Balloon.
Symbol plan: Hot-air balloon with paired panel seams and basket. VRECT_L (8,4)-(40,44) gives the envelope height. No useful exact Lucide hot-air match; balloon reference informs smooth taper only. Mirror envelope and panel curves. Omit short connector band; basket directly attaches below envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4c1a82e-5a72-5b19-9c7f-9688aab014a6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/hot air balloon_b4c1a82e-5a72-5b19-9c7f-9688aab014a6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hot-air-balloon-with-long-curved-panel-seams'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    aliases = ()
    keywords = ('simple', 'hot', 'air', 'balloon')

    def build(self):
        self.add_arc('upper-left',(8,20),(24,4),radius_x=16)
        self.add_arc('upper-right',(24,4),(40,20),radius_x=16)
        self.add_bezier('lower-right',(40,20),((40,26),(32,30),(30,34)))
        self.add_line('opening',(30,34),(18,34))
        self.add_bezier('lower-left',(18,34),((16,30),(8,26),(8,20)))
        self.add_contour('envelope','upper-left','upper-right','lower-right','opening','lower-left',closed=True)
        self.add_bezier('panel-left',(24,4),((14,10),(16,24),(18,34)))
        self.add_bezier('panel-right',(24,4),((34,10),(32,24),(30,34)))
        for p in ('panel-left','panel-right'):self.relate('connect',p,'envelope')
        self.relate('connect','panel-left','panel-right')
        self.add_line('basket-left',(18,34),(18,40));self.add_arc('basket-lower-left',(18,40),(22,44),radius_x=4,sweep=False)
        self.add_line('basket-bottom',(22,44),(26,44));self.add_arc('basket-lower-right',(26,44),(30,40),radius_x=4,sweep=False)
        self.add_line('basket-right',(30,40),(30,34));self.add_contour('basket','basket-left','basket-lower-left','basket-bottom','basket-lower-right','basket-right');self.relate('connect','basket','envelope')

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
