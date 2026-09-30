'Thickened the central tube and used consistently rounded mirrored end caps with axial leads.\nOriginal/current comparison: The rejected fuse looks like a dumbbell, with a very thin central tube and square small-radius end caps.\nPlan: HRECT_M, bounds (2, 8, 46, 40); shared circles, mirrored pairs and explicit joined nodes.\nReference: Lucide plug original and atomic-debug: rounded housings and leads attached at explicit wall nodes.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '19059222-8a90-50b8-a216-cc1d758bf898'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horizontal-axial-fuse-with-rounded-end-caps/20260929T110700Z-thuan-mac/reference/electronics fuse_19059222-8a90-50b8-a216-cc1d758bf898.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horizontal-axial-fuse-with-rounded-end-caps'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('horizontal', 'axial', 'fuse', 'with', 'rounded', 'end', 'caps')

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

        for name,cx in [('left',14),('right',34)]:
            path(name,(cx,10),[('A',(cx+4,14),4),('L',(cx+4,16)),('L',(cx+4,24)),('L',(cx+4,32)),('L',(cx+4,34)),('A',(cx,38),4),('A',(cx-4,34),4),('L',(cx-4,32)),('L',(cx-4,24)),('L',(cx-4,16)),('L',(cx-4,14)),('A',(cx,10),4)],True)
        for y in (16,32):
            n='tube-'+str(y);line(n,(18,y),(30,y));join(n,'left');join(n,'right')
        line('lead-left',(4,24),(10,24));join('lead-left','left')
        line('lead-right',(38,24),(44,24));join('lead-right','right')
