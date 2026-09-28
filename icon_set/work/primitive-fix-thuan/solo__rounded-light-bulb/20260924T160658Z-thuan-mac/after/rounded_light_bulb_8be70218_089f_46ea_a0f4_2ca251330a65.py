'Symmetric light bulb; broad glass dome flows smoothly into a narrow neck and rounded base. Bounds (8,4)-(40,44).\nConstruction: Lucide lightbulb: circular dome and smooth narrowing shoulder.\nOmissions: Filament absent in source.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8be70218-089f-46ea-a0f4-2ca251330a65'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rounded-light-bulb/20260924T160658Z-thuan-mac/reference/lightbulb_8be70218-089f-46ea-a0f4-2ca251330a65.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-light-bulb'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('rounded', 'light', 'bulb')

    def build(self):

        def path(n,p,steps,closed=False):
            members=[]
            for i,s in enumerate(steps):
                k,q,*a=s; m=f'{n}-{i}'
                if k=='L': self.add_line(m,p,q)
                elif k=='A': self.add_arc(m,p,q,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif k=='C': self.add_bezier(m,p,(a[0],a[1],q))
                members.append(m);p=q
            self.add_contour(n,*members,closed=closed)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,rad):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        path('bulb',(8,20),[('A',(24,4),16,16,True),('A',(40,20),16,16,True),('C',(32,34),(40,27),(32,28)),('L',(32,40)),('A',(28,44),4,4,True),('L',(20,44)),('A',(16,40),4,4,True),('L',(16,34)),('C',(8,20),(16,28),(8,27))],True)
        line('base-seam',(16,34),(32,34));join('base-seam','bulb')
