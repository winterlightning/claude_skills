'Restored the attached rounded terminal and retained a clean empty body.\nOriginal/current comparison: The rejected terminal is a detached bar; the original has a rounded terminal attached to the battery body.\nPlan: HRECT_M, bounds (2, 8, 46, 40); shared circles, mirrored pairs and explicit joined nodes.\nReference: Lucide battery original and atomic-debug for rounded body construction; original specifically requires an attached terminal.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '85092961-e906-49b8-a4e0-732ce5ffbef0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__empty-battery-content/20260929T110700Z-thuan-mac/reference/battery 1_85092961-e906-49b8-a4e0-732ce5ffbef0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'empty-battery-content'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('empty', 'battery', 'content')

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

        path('body',(8,10),[('L',(30,10)),('A',(34,14),4),('L',(34,18)),('L',(34,30)),('L',(34,34)),('A',(30,38),4),('L',(8,38)),('A',(4,34),4),('L',(4,14)),('A',(8,10),4)],True)
        path('terminal',(34,18),[('L',(40,18)),('A',(44,22),4),('L',(44,26)),('A',(40,30),4),('L',(34,30))]);join('terminal','body')
