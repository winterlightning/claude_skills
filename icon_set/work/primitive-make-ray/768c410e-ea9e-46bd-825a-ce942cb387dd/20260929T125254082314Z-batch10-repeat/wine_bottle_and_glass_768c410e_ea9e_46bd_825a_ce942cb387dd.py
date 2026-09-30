"""The rejected bottle was square at the base and the glass was tiny and rectangular. Restore a wider stemmed bowl beside a rounded wine bottle.
Symbol plan: Lucide wine circular bowl and stem; source bottle-and-glass arrangement.
Keyshape HRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '768c410e-ea9e-46bd-825a-ce942cb387dd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wine-bottle-and-glass/20260929T124732Z-thuan-mac/reference/winery_768c410e-ea9e-46bd-825a-ce942cb387dd.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'wine-bottle-and-glass'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('wine', 'bottle', 'and', 'glass')

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

        path('bottle',(8,8),[('L',(16,8)),('L',(16,20)),('C',(20,27),(16,24),(20,23)),('L',(20,36)),('A',(16,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,27)),('C',(8,20),(4,23),(8,24)),('L',(8,8))],True)
        path('bowl',(28,20),[('L',(44,20)),('L',(44,24)),('A',(36,32),8,8,True),('A',(28,24),8,8,True),('L',(28,20))],True)
        line('stem',(36,32),(36,40));join('stem','bowl')
        poly('base',(30,40),(36,40),(42,40));join('base','stem')
