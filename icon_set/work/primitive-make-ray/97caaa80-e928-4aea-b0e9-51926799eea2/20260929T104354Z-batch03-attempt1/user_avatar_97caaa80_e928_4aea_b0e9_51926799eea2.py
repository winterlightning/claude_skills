'Restored the closed torso and slightly enlarged the circular head, with smooth symmetric shoulders and exact bust contact.\nOriginal/current comparison: The rejected generic open-bottom shoulders omit the closed shirt body of the supplied father portrait.\nPlan: VRECT_L, bounds (6, 2, 42, 46); shared circles, mirrored pairs and explicit joined nodes.\nReference: human_ref/user.svg: circular head and broad smooth shoulders; original father portrait supplies closed lower torso. 26-(13+9)=4 centerline/zero ink gap.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '97caaa80-e928-4aea-b0e9-51926799eea2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__user-avatar/20260929T104354Z-thuan-mac/reference/father_97caaa80-e928-4aea-b0e9-51926799eea2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'user-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('user', 'avatar')
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

        circle('head',24,13,9)
        path('body',(8,44),[('L',(8,38)),('A',(20,26),12),('L',(28,26)),('A',(40,38),12),('L',(40,44)),('L',(8,44))],True)
        join('head','body')
