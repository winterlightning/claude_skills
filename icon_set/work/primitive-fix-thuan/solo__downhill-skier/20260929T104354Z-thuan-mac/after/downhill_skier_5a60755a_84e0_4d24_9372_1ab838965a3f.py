'Aligned the head above the upper torso, rebuilt a crouch and added the forward pole over a smooth ski.\nOriginal/current comparison: The rejected head floats beside the body and the rear arm bends unnaturally; the source shows a crouching rider with a pole.\nPlan: VRECT_L, bounds (6, 2, 42, 46); shared circles, mirrored pairs and explicit joined nodes.\nReference: human_ref/full_body_ref.png: circular head aligned with vertical upper-torso tangent; 22-(9+5)=8 centerline gap.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5a60755a-84e0-4d24-9372-1ab838965a3f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__downhill-skier/20260929T104354Z-thuan-mac/reference/snowboard_5a60755a-84e0-4d24-9372-1ab838965a3f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'downhill-skier'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('downhill', 'skier')

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

        circle('head',26,9,5)
        bez('torso',(26,22),((26,26),(23,28),(20,30)))
        poly('leg',(20,30),(28,34),(20,44));join('leg','torso')
        poly('arm',(26,22),(32,28),(40,24));join('arm','torso')
        poly('pole',(40,22),(40,24),(40,36));join('pole','arm')
        path('ski',(8,40),[('C',(20,44),(12,42),(16,44)),('L',(36,44)),('A',(40,40),4,4,False)])
        join('ski','leg')
        self.mark_human_figure('rider',head='head',torso='torso',torso_junction='start')
