"""Support Agent with Headphones — batch 50."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a43a1b34-ba30-51e2-8567-7e92fc1abc1c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/headphones customer support human_a43a1b34-ba30-51e2-8567-7e92fc1abc1c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'support-agent-with-headphones'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('support', 'agent', 'with', 'headphones')
    human_construction = "bust"

    def build(self):
        # Plan: concentric circular face, broad arch, paired ear returns.
        # Human user.svg supplies circular face and broad shoulder proportions.
        # Lucide headset informs headband and microphone lead construction.
        # VRECT_L centerline extrema (8,4)-(40,44). Tiny facial marks omitted.
        self.add_arc('headband',(8,20),(40,20),radius_x=16)
        self.add_arc('crown',(16,24),(32,24),radius_x=8)
        self.add_arc('face',(32,24),(16,24),radius_x=8)
        self.add_contour('head','crown','face',closed=True)
        for side,sign in [('left',-1),('right',1)]:
            self.add_polyline('ear-'+side,(24+sign*16,20),(24+sign*16,24),(24+sign*8,24))
            self.relate('connect','ear-'+side,'headband')
            self.relate('connect','ear-'+side,'head')
        # Jaw bottom32 / shoulder top36 => 4 centerline, zero visible bust gap.
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(18,36),radius_x=10,radius_y=6)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top',(18,36),(24,36))
        self.add_line('body-top-right',(24,36),(30,36))
        self.add_arc('body-right-shoulder',(30,36),(40,42),radius_x=10,radius_y=6)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        for a,z in (('body-left','body-top'),('body-top','body-top-right'),('body-top-right','body-right'),('head','body-top'),('head','body-top-right')):self.relate('connect',a,z)

    def circle(self,n,x,y,r):
        pts=[(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        for j in range(4): self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%4],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(4)],closed=True)

    def box(self,n,x,y,w,h,attachments=()):
        corners=[(x,y),(x+w,y),(x+w,y+h),(x,y+h)];nodes=[]
        for a,z in zip(corners,corners[1:]+corners[:1]):
            dx,dy=z[0]-a[0],z[1]-a[1]
            inside=[p for p in attachments if (p[0]-a[0])*dy==(p[1]-a[1])*dx and 0<(p[0]-a[0])*dx+(p[1]-a[1])*dy<dx*dx+dy*dy]
            inside.sort(key=lambda p:(p[0]-a[0])*dx+(p[1]-a[1])*dy);nodes.extend([a]+inside)
        self.add_polyline(n,*nodes,closed=True)

