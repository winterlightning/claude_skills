"""The rejected continuous bust had a narrow straight neck and steep shoulders. Restore a circular head, smooth neck transitions and wide sloping shoulders in a single silhouette.
Symbol plan: human_ref/user.svg circular head and broad smooth shoulders; source continuous neck retained. Head arcs share center24,19 and radius13.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '64e1a8ed-890b-425f-aaa4-63ac66ca5281'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__user-bust-continuous-outline/20260929T122443Z-thuan-mac/reference/person_64e1a8ed-890b-425f-aaa4-63ac66ca5281.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'user-bust-continuous-outline'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('user', 'bust', 'continuous', 'outline')

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

        path('bust',(6,42),[('C',(18,32),(14,38),(18,38)),('C',(12,24),(18,29),(14,28)),('A',(11,19),13,13,True),('A',(37,19),13,13,True),('A',(36,24),13,13,True),('C',(30,32),(34,28),(30,29)),('C',(42,42),(30,38),(34,38))])
