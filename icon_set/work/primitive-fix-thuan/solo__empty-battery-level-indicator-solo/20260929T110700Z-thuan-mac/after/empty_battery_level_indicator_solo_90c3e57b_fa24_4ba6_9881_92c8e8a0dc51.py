'Replaced the square inset with a wider rectangular level window and regularized the outer corners.\nOriginal/current comparison: The rejected level window is square and small; the original has a wide empty rectangular window.\nPlan: HRECT_L, bounds (2, 6, 46, 42); shared circles, mirrored pairs and explicit joined nodes.\nReference: Lucide battery original and atomic-debug: shared corner radii and terminal layout; original wide empty inset retained.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '90c3e57b-fa24-4ba6-9881-92c8e8a0dc51'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__empty-battery-level-indicator-solo/20260929T110700Z-thuan-mac/reference/battery empty_90c3e57b-fa24-4ba6-9881-92c8e8a0dc51.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'empty-battery-level-indicator-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('empty', 'battery', 'level', 'indicator', 'solo')

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def poly(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def con(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):arc(n+str(j),a,b,r)
            con(n,*(n+str(j) for j in range(4)),closed=True)
        def path(n,start,steps,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{i}';members.append(m)
                if kind=='L': line(m,here,end)
                elif kind=='A': arc(m,here,end,*args)
                elif kind=='C': bez(m,here,(args[0],args[1],end))
                here=end
            con(n,*members,closed=closed)
        def rect(n,l,t,r,b,rad=4):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad),('L',(r,b-rad)),('A',(r-rad,b),rad),('L',(l+rad,b)),('A',(l,b-rad),rad),('L',(l,t+rad)),('A',(l+rad,t),rad)],True)

        path('battery',(8,8),[('L',(32,8)),('A',(36,12),4),('L',(36,16)),('L',(36,32)),('L',(36,36)),('A',(32,40),4),('L',(8,40)),('A',(4,36),4),('L',(4,12)),('A',(8,8),4)],True)
        poly('terminal',(36,16),(44,16),(44,32),(36,32));join('terminal','battery')
        poly('level',(13,20),(27,20),(27,28),(13,28),closed=True)
