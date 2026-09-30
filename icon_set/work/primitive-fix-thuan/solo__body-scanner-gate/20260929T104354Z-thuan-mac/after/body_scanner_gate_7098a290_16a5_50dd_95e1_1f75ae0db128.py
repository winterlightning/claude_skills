'Enlarged the circular head, set its exact detached gap and spaced the person evenly between paired posts.\nOriginal/current comparison: The rejected scanner figure has a tiny head and rigid shoulders; the original has a clear central person between scanning posts.\nPlan: HRECT_L, bounds (2, 6, 46, 42); shared circles, mirrored pairs and explicit joined nodes.\nReference: human_ref/full_body_ref.png: circular head, simple limbs; 26-(14+4)=8 centerline gap.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7098a290-16a5-50dd-95e1-1f75ae0db128'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__body-scanner-gate/20260929T104354Z-thuan-mac/reference/body scanner_7098a290-16a5-50dd-95e1-1f75ae0db128.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'body-scanner-gate'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('body', 'scanner', 'gate')

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

        for side,x,sign in [('left',4,1),('right',44,-1)]:
            poly('post-'+side,(x,8),(x,24),(x,40),(x+4*sign,40))
            line('sensor-'+side,(x,24),(x+2*sign,24));join('post-'+side,'sensor-'+side)
        circle('head',24,14,4)
        line('torso',(24,26),(24,33))
        poly('arms',(16,33),(16,26),(24,26),(32,26),(32,33));join('torso','arms')
        poly('legs',(18,40),(24,33),(30,40));join('legs','torso')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
