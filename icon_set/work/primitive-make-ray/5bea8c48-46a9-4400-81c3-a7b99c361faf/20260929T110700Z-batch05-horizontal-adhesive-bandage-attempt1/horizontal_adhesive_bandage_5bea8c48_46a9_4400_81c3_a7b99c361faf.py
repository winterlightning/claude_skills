'Reduced the outer corner radius and restored two matched curved pad boundaries.\nOriginal/current comparison: The rejected capsule has exaggerated semicircular ends and straight pad dividers; the source is a rounded strip with gently bowed dividers.\nPlan: HRECT_M, bounds (2, 8, 46, 40); shared circles, mirrored pairs and explicit joined nodes.\nReference: Lucide bandage original and atomic-debug: rounded rectangular strip with structural pad divisions; source supplies curved dividers.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5bea8c48-46a9-4400-81c3-a7b99c361faf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horizontal-adhesive-bandage/20260929T110700Z-thuan-mac/reference/fascia_5bea8c48-46a9-4400-81c3-a7b99c361faf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horizontal-adhesive-bandage'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('horizontal', 'adhesive', 'bandage')

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

        path('strip',(8,10),[('L',(18,10)),('L',(32,10)),('L',(40,10)),('A',(44,14),4),('L',(44,34)),('A',(40,38),4),('L',(32,38)),('L',(18,38)),('L',(8,38)),('A',(4,34),4),('L',(4,14)),('A',(8,10),4)],True)
        for x in (18,32):
            n='pad-'+str(x);bez(n,(x,10),((x-4,20),(x-4,28),(x,38)));join(n,'strip')
