'Recomposed on a square envelope with a longer thumb, rounded knuckles, a clear cuff and one readable finger crease.\nOriginal/current comparison: The rejected horizontal hand is squat; the original has a longer downward thumb and a clear cuff.\nPlan: SQUARE, bounds (4, 4, 44, 44); shared circles, mirrored pairs and explicit joined nodes.\nReference: Lucide thumbs-down original and atomic-debug: coherent thumb/palm outline and separate cuff join; supplied source orientation retained.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ccfc5e52-667a-4591-9a3a-ef60a2289489'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__thumbs-down-hand/20260929T104354Z-thuan-mac/reference/thumbs down_ccfc5e52-667a-4591-9a3a-ef60a2289489.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'thumbs-down-hand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('thumbs', 'down', 'hand')

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

        path('hand',(16,24),[('L',(22,30)),('L',(24,42)),('L',(28,42)),('A',(32,38),4,4,False),('L',(30,26)),('L',(36,26)),('A',(42,20),6,6,False),('L',(42,16)),('L',(42,12)),('A',(36,6),6,6,False),('L',(16,6))])
        path('cuff',(16,6),[('L',(8,6)),('A',(6,8),2,2,False),('L',(6,22)),('A',(8,24),2,2,False),('L',(16,24)),('L',(16,6))],True);join('hand','cuff')
        line('finger',(34,16),(42,16));join('finger','hand')
