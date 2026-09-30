'Smoothed both shoulders and the broad curved hem while preserving the hood and circular lower face.\nOriginal/current comparison: The rejected poncho has a rigid diamond hem and angular shoulders compared with the flowing garment in the original.\nPlan: SQUARE, bounds (4, 4, 44, 44); shared circles, mirrored pairs and explicit joined nodes.\nReference: human_ref/user.svg circular face vocabulary; original broad hooded garment supplies silhouette and natural curved hem.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b55bffa3-4279-4235-9ba3-a7ca76021d61'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__figure-broad-rain-poncho/20260929T110700Z-thuan-mac/reference/poncho_b55bffa3-4279-4235-9ba3-a7ca76021d61.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'figure-broad-rain-poncho'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('figure', 'broad', 'rain', 'poncho')

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

        bez('hood',(16,20),((16,12),(18,6),(24,6)),((30,6),(32,12),(32,20)))
        bez('poncho',(16,20),((12,21),(9,28),(6,34)),((12,38),(19,42),(24,42)),((29,42),(36,38),(42,34)),((39,28),(36,21),(32,20)))
        arc('face',(16,20),(32,20),8,s=False)
        join('hood','poncho');join('hood','face');join('poncho','face')
