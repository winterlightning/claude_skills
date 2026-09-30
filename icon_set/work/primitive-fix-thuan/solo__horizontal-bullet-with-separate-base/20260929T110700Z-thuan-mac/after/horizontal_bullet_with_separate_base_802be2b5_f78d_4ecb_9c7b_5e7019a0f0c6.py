'Rebuilt a tapered curved nose and rounded the separate rear bracket while retaining its clear gap.\nOriginal/current comparison: The rejected projectile ends in a semicircular D instead of the tapered nose in the original; the separate base has square corners.\nPlan: HRECT_M, bounds (2, 8, 46, 40); shared circles, mirrored pairs and explicit joined nodes.\nReference: No useful subject-specific Lucide match; supplied reference defines the subject.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '802be2b5-f78d-4ecb-9c7b-5e7019a0f0c6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horizontal-bullet-with-separate-base/20260929T110700Z-thuan-mac/reference/bullet_802be2b5-f78d-4ecb-9c7b-5e7019a0f0c6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horizontal-bullet-with-separate-base'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('horizontal', 'bullet', 'with', 'separate', 'base')

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

        path('base',(8,10),[('L',(6,10)),('A',(4,12),2,2,False),('L',(4,36)),('A',(6,38),2,2,False),('L',(8,38))])
        path('bullet',(17,10),[('L',(28,10)),('C',(44,24),(36,10),(42,18)),('C',(28,38),(42,30),(36,38)),('L',(17,38)),('L',(17,10))],True)
