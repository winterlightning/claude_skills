"""The rejected bob-haired woman had a helmet outline and generic open shoulders. Restore flared bob ends and a broader closed blouse below a circular jaw.
Symbol plan: human_ref/user.svg circular jaw and shoulders; original flared bob and closed blouse. Jaw26 and shoulder30 make zero visible gap.
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

        path('hair',(8,28),[('L',(10,18)),('A',(38,18),14,14,True),('L',(40,28))])
        self.add_arc('jaw',(16,18),(32,18),radius_x=8,sweep=False)
        path('fringe',(16,18),[('C',(27,11),(21,18),(25,14)),('C',(32,18),(28,15),(30,17))]);join('fringe','jaw')
        line('temple-left',(10,18),(16,18));line('temple-right',(32,18),(38,18))
        for n in ('temple-left','temple-right'):
         join(n,'hair');join(n,'jaw');join(n,'fringe')
        path('body',(8,44),[('L',(8,40)),('A',(20,30),12,10,True),('L',(28,30)),('A',(40,40),12,10,True),('L',(40,44)),('L',(8,44))],True);join('jaw','body')
