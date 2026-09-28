'Three round berries in a triangular cluster with a curved stem and pointed leaf. Equal circular upper berries. Bounds (8,4)-(40,44).\nConstruction: Lucide grape: shared berry radii and coherent clustered fruit.\nOmissions: None'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c09c4db6-f5a3-4264-8d21-6ab3263d70b9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/berry_c09c4db6-f5a3-4264-8d21-6ab3263d70b9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-round-berries-on-a-leafy-stem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('three', 'round', 'berries', 'on', 'a', 'leafy', 'stem')

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
        circle('left',16,28,8);circle('right',32,28,8);join('left','right')
        path('bottom',(16,36),[('A',(32,36),8,8,False)]);join('bottom','left');join('bottom','right')
        path('stem',(24,28),[('L',(24,12)),('C',(14,4),(24,8),(18,4))]);join('stem','left');join('stem','right')
        path('leaf',(24,12),[('C',(40,4),(26,4),(34,4)),('C',(24,12),(40,12),(30,16))],True);join('leaf','stem')
