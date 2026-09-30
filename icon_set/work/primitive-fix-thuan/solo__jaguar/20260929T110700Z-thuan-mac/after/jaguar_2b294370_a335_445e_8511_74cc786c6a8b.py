'Rounded the ear, chest, feet and tail corner while keeping a clear feline silhouette and body spot.\nOriginal/current comparison: The rejected jaguar has block-like legs, a triangular ear and an angular tail, unlike the rounded cat in the source.\nPlan: HRECT_L, bounds (2, 6, 46, 42); shared circles, mirrored pairs and explicit joined nodes.\nReference: No useful subject-specific Lucide match; supplied reference defines the subject.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2b294370-a335-445e-8511-74cc786c6a8b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__jaguar/20260929T110700Z-thuan-mac/reference/jaguar_2b294370-a335-445e-8511-74cc786c6a8b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'jaguar'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('jaguar',)

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

        path('cat',(4,20),[('C',(10,12),(8,17),(10,16)),('A',(16,12),3,4,True),('L',(20,12)),('L',(28,12)),('A',(36,20),8),('L',(36,38)),('A',(34,40),2),('L',(30,40)),('A',(28,38),2),('L',(28,30)),('L',(20,30)),('L',(20,38)),('A',(18,40),2),('L',(14,40)),('A',(12,38),2),('L',(12,27)),('C',(8,24),(12,25),(10,24)),('L',(4,24)),('L',(4,20))],True)
        path('tail',(36,20),[('L',(40,20)),('A',(44,24),4),('L',(44,34))]);join('tail','cat')
        self.add_dot('spot',(26,21))
