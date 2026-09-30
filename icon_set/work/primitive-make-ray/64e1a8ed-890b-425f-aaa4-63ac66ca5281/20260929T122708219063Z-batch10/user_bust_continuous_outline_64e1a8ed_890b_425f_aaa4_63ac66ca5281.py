"""The rejected bust had a narrow vertical neck and steep shoulders. Restore a round head, a short gently curved neck and broad sloping shoulders in one continuous silhouette.
Symbol plan: human_ref/user.svg for broad shoulders; original continuous-neck silhouette retained.
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

        path('bust',(6,42),[('C',(18,30),(10,40),(18,37)),('C',(15,23),(18,27),(17,25)),('A',(12,16),10,10,True),('A',(36,16),12,10,True),('A',(33,23),10,10,True),('C',(30,30),(31,25),(30,27)),('C',(42,42),(30,37),(38,40))])
