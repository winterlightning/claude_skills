'Rebalanced the head and broad shoulder, enlarged the bent forearm and used explicit bust construction at the chin.\nOriginal/current comparison: The rejected arm reads as a thin loop and the shoulder/head junction triggers internal-spacing review.\nPlan: VRECT_L, bounds (6, 2, 42, 46); shared circles, mirrored pairs and explicit joined nodes.\nReference: human_ref/user.svg: broad shoulder and circular face; 26-(13+9)=4 centerline/zero ink contact; asymmetric hand-at-chin pose.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1b67153c-7c88-4721-a1a4-34d2dfd71022'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__thinking-person-with-hand-at-chin/20260929T104354Z-thuan-mac/reference/doubter_1b67153c-7c88-4721-a1a4-34d2dfd71022.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'thinking-person-with-hand-at-chin'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('thinking', 'person', 'with', 'hand', 'at', 'chin')
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

        circle('head',23,13,9)
        path('body',(8,44),[('L',(8,41)),('A',(23,26),15)])
        bez('raised-arm',(23,26),((24,33),(27,41),(30,44)),((38,44),(40,41),(40,36)),((40,31),(38,27),(34,26)))
        join('head','body');join('head','raised-arm');join('body','raised-arm')
