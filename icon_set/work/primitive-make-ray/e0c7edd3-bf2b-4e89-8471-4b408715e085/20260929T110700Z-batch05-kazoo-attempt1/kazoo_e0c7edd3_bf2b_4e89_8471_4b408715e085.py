'Restored the round membrane housing and inner opening, with tapered diagonal tube ends joined at exact nodes.\nOriginal/current comparison: The rejected kazoo omits the circular membrane opening and reads like a wrench or bent tube.\nPlan: SQUARE, bounds (4, 4, 44, 44); shared circles, mirrored pairs and explicit joined nodes.\nReference: No useful subject-specific Lucide match; supplied reference defines the subject.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e0c7edd3-bf2b-4e89-8471-4b408715e085'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__kazoo/20260929T110700Z-thuan-mac/reference/kazoo_e0c7edd3-bf2b-4e89-8471-4b408715e085.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'kazoo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('kazoo',)

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

        circle('membrane-housing',24,24,12)
        circle('opening',24,24,3)
        poly('mouthpiece',(12,24),(6,36),(12,42),(24,36));join('mouthpiece','membrane-housing')
        poly('bell',(24,12),(36,6),(42,12),(36,24));join('bell','membrane-housing')
