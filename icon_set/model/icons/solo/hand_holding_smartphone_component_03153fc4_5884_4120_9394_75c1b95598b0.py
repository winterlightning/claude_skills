"""Hand grips smartphone with inward squeeze arrows, retained from complete reference. Lucide smartphone owns matching corner radii, Lucide hand informs palm curve. Individual curled fingers reduced to one grip line.
Keyshape HRECT_L; clean centerlines revision. Shared symbol parameters own paired geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '03153fc4-5884-4120-9394-75c1b95598b0'
SOURCE_PATH = 'pictographic-primitives/phones/squeeze sides 1_03153fc4-5884-4120-9394-75c1b95598b0.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='hand-holding-smartphone-component'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/phones"
    aliases=()
    keywords=('hand', 'holding', 'smartphone', 'component')
    def build(self):

        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,k=2):
            path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        line=self.add_line
        poly=self.add_polyline
        def join(a,b): self.relate('connect',a,b)

        box('phone',14,8,34,30,3)
        path('palm',(18,40),[('L',(34,40)),('A',(44,30),10,10,False),('L',(44,28)),('C',(34,24),(44,24),(38,24))]);join('palm','phone')
        line('grip',(14,22),(22,22));join('phone','grip')
        for j,s in enumerate((-1,1)):
            def p(x,y):return (24+s*x,y)
            poly(f'arrow-{j}',p(20,16),p(10,16))
            poly(f'chevron-{j}',p(14,12),p(10,16),p(14,20))
            join(f'arrow-{j}',f'chevron-{j}');join(f'arrow-{j}','phone');join(f'chevron-{j}','phone')
