'Enlarged the rounded nose and recomposed the swept wings and tail around the diagonal fuselage.\nOriginal/current comparison: The rejected jet has a boxy tail and an abrupt small nose compared with the rounded, swept silhouette in the source.\nPlan: SQUARE, bounds (4, 4, 44, 44); shared circles, mirrored pairs and explicit joined nodes.\nReference: Lucide plane original and atomic-debug: coherent diagonal fuselage with integrated swept wings and tail; supplied passenger-jet orientation retained.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '440ed8d8-ba1d-485b-bd8d-a6ae4bdc2513'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__jumbo-jet/20260929T110700Z-thuan-mac/reference/jumbo jet_440ed8d8-ba1d-485b-bd8d-a6ae4bdc2513.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'jumbo-jet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('jumbo', 'jet')

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

        path('plane',(34,6),[('A',(42,14),8),('L',(32,24)),('L',(38,40)),('L',(30,42)),('L',(24,32)),('L',(16,40)),('L',(8,42)),('L',(6,34)),('L',(16,24)),('L',(6,16)),('L',(8,8)),('L',(24,16)),('L',(34,6))],True)
