'Restored a wide central bust with a closed base and two partial outer shoulder silhouettes, preserving three distinct heads.\nOriginal/current comparison: The rejected group uses three equal narrow arches, losing the broad central foreground torso and partly hidden side figures.\nPlan: HRECT_L, bounds (2, 6, 46, 42); shared circles, mirrored pairs and explicit joined nodes.\nReference: human_ref/user.svg and Lucide users original/atomic-debug: broad central shoulder contour and partial occluded side busts; each circular jaw has 4 centerline/zero ink shoulder contact.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ee7da2e5-378e-466a-b367-d573122d74d0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-people-with-central-foreground-figure/20260929T104354Z-thuan-mac/reference/crew_ee7da2e5-378e-466a-b367-d573122d74d0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-people-with-central-foreground-figure'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('three', 'people', 'with', 'central', 'foreground', 'figure')
    human_construction = 'bust'

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def poly(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def con(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            con(n,n+'a',n+'b',closed=True)
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

        cx,cy,r=24,13,5
        circle('head-center',cx,cy,r)
        top=cy+r+4; w=10
        path('body-center',(cx-w,40),[('L',(cx-w,top+w)),('A',(cx,top),w),('A',(cx+w,top+w),w),('L',(cx+w,40)),('L',(cx-w,40))],True)
        join('head-center','body-center')
        for side,x,sign in [('left',7,-1),('right',41,1)]:
            circle('head-'+side,x,15,3)
            top=15+7
            start=(x+sign,36);outer=x+sign*3
            path('body-'+side,start,[('L',(outer,36)),('L',(outer,top+3)),('A',(x,top),3,3,sign<0)])
            join('head-'+side,'body-'+side')
