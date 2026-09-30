"""The rejected bob-haired portrait used a helmet-like arc and generic shoulders. Restore turned-out bob ends and a closed rounded blouse under the circular jaw.
Symbol plan: human_ref/user.svg circular jaw and shoulders; original turned-out bob and closed blouse. Jaw28, shoulders32 give touching ink.
Keyshape VRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4faebe8e-834d-47f1-a65f-eefb2985e002'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-with-bobbed-hair/20260929T124732Z-thuan-mac/reference/lady_4faebe8e-834d-47f1-a65f-eefb2985e002.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'woman-with-bobbed-hair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('woman', 'with', 'bobbed', 'hair')
    human_construction = "bust"
    def build(self):

        def path(n,start,steps,closed=False):
            point=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L': self.add_line(m,point,end)
                elif kind=='A': self.add_arc(m,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,point,(args[0],args[1],end))
                point=end; members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        path('hair',(10,30),[('L',(8,28)),('L',(8,20)),('A',(40,20),16,16,True),('L',(40,28)),('L',(38,30))])
        self.add_arc('jaw',(16,20),(32,20),radius_x=8,sweep=False)
        path('fringe',(16,20),[('C',(27,12),(21,20),(25,15)),('C',(32,20),(28,16),(30,19))]);join('fringe','jaw')
        line('temple-left',(8,20),(16,20));line('temple-right',(32,20),(40,20))
        for n in ('temple-left','temple-right'):
         join(n,'hair');join(n,'jaw');join(n,'fringe')
        path('body',(8,44),[('L',(8,40)),('A',(24,32),16,8,True),('A',(40,40),16,8,True),('L',(40,44)),('L',(8,44))],True);join('body','jaw')
