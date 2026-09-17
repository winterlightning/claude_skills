"""Modern Video Game Controller.
Symbol plan: Rounded gamepad with cross control and diamond of four buttons. HRECT_L (4,8)-(44,40) gives controls room. Lucide gamepad-2 informs rounded grips and spare controls. Shared corner radii and symmetric shell; shallow central arch preserves button clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '540e6c7f-d9cf-5188-9e6f-b558f13e37e5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/console_540e6c7f-d9cf-5188-9e6f-b558f13e37e5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-gamepad-with-cross-control-and-four-buttons'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('modern', 'video', 'game', 'controller')

    def build(self):
        self.add_line('top',(12,8),(36,8));self.add_arc('upper-right',(36,8),(44,16),radius_x=8)
        self.add_line('right',(44,16),(44,30));self.add_arc('grip-right',(44,30),(34,40),radius_x=10)
        self.add_bezier('arch-right',(34,40),((30,40),(28,35),(24,35)))
        self.add_bezier('arch-left',(24,35),((20,35),(18,40),(14,40)))
        self.add_arc('grip-left',(14,40),(4,30),radius_x=10);self.add_line('left',(4,30),(4,16));self.add_arc('upper-left',(4,16),(12,8),radius_x=8)
        parts=['top','upper-right','right','grip-right','arch-right','arch-left','grip-left','left','upper-left']
        for a,b in zip(parts,parts[1:]+parts[:1]):self.relate('connect',a,b)
        self.add_polyline('cross-horizontal',(12,22),(14,22),(16,22))
        self.add_polyline('cross-vertical',(14,20),(14,22),(14,24));self.relate('connect','cross-horizontal','cross-vertical')
        for i,p in enumerate([(30,16),(36,22),(30,28),(24,22)]):self.add_dot(f'button-{i}',p)

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
