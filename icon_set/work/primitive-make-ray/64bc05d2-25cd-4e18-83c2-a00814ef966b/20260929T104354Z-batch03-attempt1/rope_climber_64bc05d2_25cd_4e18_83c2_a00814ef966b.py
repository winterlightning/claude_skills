'Straightened the climbing rope, aligned the head and torso and rebuilt the raised grip and bent climbing legs.\nOriginal/current comparison: The rejected head is misaligned with the torso and the rope loops into the waist like a bowl.\nPlan: VRECT_L, bounds (6, 2, 42, 46); shared circles, mirrored pairs and explicit joined nodes.\nReference: human_ref/full_body_ref.png: head center on upper torso tangent; 24-(10+6)=8 centerline gap; intentionally asymmetric action.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '64bc05d2-25cd-4e18-83c2-a00814ef966b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rope-climber/20260929T104354Z-thuan-mac/reference/climbing_64bc05d2-25cd-4e18-83c2-a00814ef966b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rope-climber'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('rope', 'climber')

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

        circle('head',24,10,6)
        bez('torso',(24,24),((24,27),(22,30),(20,32)))
        poly('left-arm',(24,24),(12,24),(8,16));join('left-arm','torso')
        poly('right-arm',(24,24),(32,24),(40,16));join('right-arm','torso');join('right-arm','left-arm')
        poly('rope',(40,4),(40,16),(40,44));join('rope','right-arm')
        line('left-leg',(20,32),(8,44));join('left-leg','torso')
        poly('right-leg',(20,32),(32,36),(32,44));join('right-leg','torso');join('right-leg','left-leg')
        self.mark_human_figure('climber',head='head',torso='torso',torso_junction='start')
