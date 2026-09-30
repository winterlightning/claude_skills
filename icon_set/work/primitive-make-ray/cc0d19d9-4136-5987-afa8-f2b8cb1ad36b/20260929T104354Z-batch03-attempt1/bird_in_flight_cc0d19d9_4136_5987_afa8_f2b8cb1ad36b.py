'Restored both raised wings and a hooked forward profile, with broad coherent flight contours.\nOriginal/current comparison: The rejected drawing has one wing and a round songbird head; the original is a two-winged soaring bird.\nPlan: HRECT_L, bounds (2, 6, 46, 42); shared circles, mirrored pairs and explicit joined nodes.\nReference: Lucide bird original and atomic-debug: coherent breast contour and beak; supplied reference owns two-wing flight pose.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cc0d19d9-4136-5987-afa8-f2b8cb1ad36b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bird-in-flight/20260929T104354Z-thuan-mac/reference/wild bird hunt_cc0d19d9-4136-5987-afa8-f2b8cb1ad36b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bird-in-flight'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('bird', 'in', 'flight')

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

        path('bird',(4,8),[('C',(28,26),(20,9),(23,17)),('C',(44,8),(28,14),(35,10)),('L',(36,26)),('C',(44,34),(42,26),(44,28)),('C',(28,32),(39,31),(33,30)),('L',(30,40)),('C',(20,35),(24,40),(22,38)),('C',(4,40),(11,41),(7,42)),('L',(4,31)),('L',(13,32)),('L',(20,25)),('C',(4,8),(12,20),(7,16))],True)
