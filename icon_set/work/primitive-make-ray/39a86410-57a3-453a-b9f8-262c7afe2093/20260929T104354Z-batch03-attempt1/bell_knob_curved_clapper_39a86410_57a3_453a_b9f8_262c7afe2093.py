'Lengthened the bell sides and used tangent flares, keeping the top knob and curved clapper.\nOriginal/current comparison: The rejected bell dome is squat with very short sides compared with the upright original.\nPlan: VRECT_L, bounds (6, 2, 42, 46); shared circles, mirrored pairs and explicit joined nodes.\nReference: Lucide bell original and atomic-debug: dome, continuous side flares and detached curved clapper.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '39a86410-57a3-453a-b9f8-262c7afe2093'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bell-knob-curved-clapper/20260929T104354Z-thuan-mac/reference/ring_39a86410-57a3-453a-b9f8-262c7afe2093.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bell-knob-curved-clapper'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('bell', 'knob', 'curved', 'clapper')

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

        self.add_dot('knob',(24,4))
        path('bell',(12,20),[('A',(36,20),12,8,True),('L',(36,26)),('C',(40,34),(36,30),(38,32)),('L',(8,34)),('C',(12,26),(10,32),(12,30)),('L',(12,20))],True)
        arc('clapper',(20,42),(28,42),4,2,False)
