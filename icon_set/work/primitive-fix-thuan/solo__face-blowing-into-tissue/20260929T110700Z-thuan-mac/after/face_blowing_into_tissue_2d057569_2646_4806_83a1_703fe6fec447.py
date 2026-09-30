'Rebuilt the tissue with a gathered top and draped lower edge, retaining the round face and closed eyes.\nOriginal/current comparison: The rejected zigzag tissue looks like a face mask; the original has a soft cloth gathered at the nose and hanging below.\nPlan: SQUARE, bounds (4, 4, 44, 44); shared circles, mirrored pairs and explicit joined nodes.\nReference: Shared human_ref/user.svg circular face vocabulary; supplied original defines closed eyes and gathered tissue. Fine folds omitted.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2d057569-2646-4806-83a1-703fe6fec447'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__face-blowing-into-tissue/20260929T110700Z-thuan-mac/reference/face tissue_2d057569-2646-4806-83a1-703fe6fec447.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'face-blowing-into-tissue'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('face', 'blowing', 'into', 'tissue')

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

        path('face',(10,34),[('A',(6,24),18),('A',(42,24),18),('A',(38,34),18)])
        for j,x in enumerate((18,30)):bez(f'eye-{j}',(x-2,19),((x-1,20),(x+1,20),(x+2,19)))
        path('tissue',(10,34),[('L',(20,28)),('C',(28,28),(22,27),(26,27)),('L',(38,34)),('L',(33,39)),('C',(24,42),(29,39),(29,42)),('C',(15,39),(19,42),(19,39)),('L',(10,34))],True)
        join('face','tissue')
        line('cloth-fold',(24,36),(24,42));join('cloth-fold','tissue')
