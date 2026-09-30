'Lengthened the forehead curve and rounded the chin and nape, preserving the integrated frame and ear.\nOriginal/current comparison: The rejected face has a cramped forehead and angular chin/nape; the original has smooth anatomical curves within an integrated scan boundary.\nPlan: SQUARE, bounds (4, 4, 44, 44); shared circles, mirrored pairs and explicit joined nodes.\nReference: Shared human_ref/user.svg for anatomical vocabulary; original governs continuous profile and integrated boundary. No detached head/body pair.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b97885e6-dbf9-5160-931c-e559629ea220'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__human-head-side-profile-scan-batch-001-r3/20260929T110700Z-thuan-mac/reference/deepfake side_b97885e6-dbf9-5160-931c-e559629ea220.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'human-head-side-profile-scan-batch-001-r3'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('human', 'head', 'side', 'profile', 'scan', 'batch', '001', 'r3')

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

        path('profile',(24,15),[('A',(17,22),7,7,False),('L',(17,24)),('L',(14,28)),('L',(18,29)),('L',(18,31)),('C',(24,34),(18,33),(20,34)),('L',(24,42)),('L',(10,42)),('A',(6,38),4),('L',(6,10)),('A',(10,6),4),('L',(22,6)),('A',(42,26),20),('C',(38,42),(42,34),(34,34))])
        arc('ear',(30,21),(30,27),3)
