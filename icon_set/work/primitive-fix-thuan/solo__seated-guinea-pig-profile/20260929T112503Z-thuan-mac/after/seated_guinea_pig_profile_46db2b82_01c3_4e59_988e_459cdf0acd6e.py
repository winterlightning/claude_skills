"""Rejected guinea pig looked like a short-legged dog with a square haunch. Restore a full rounded seated rump, tiny round ear and short front foot. Omit small mouth and inner haunch line for spacing.
Symbol plan: No useful exact Lucide match; original reference and geometric curves.
Keyshape HRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '46db2b82-01c3-4e59-988e-459cdf0acd6e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-guinea-pig-profile/20260929T112503Z-thuan-mac/reference/guinea pig_46db2b82-01c3-4e59-988e-459cdf0acd6e.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'seated-guinea-pig-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('seated', 'guinea', 'pig', 'profile')

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

        path('body',(18,40),[('A',(4,26),14,14,True),('A',(18,12),14,14,True),('L',(28,12)),('A',(34,12),3,4,True),('C',(44,24),(40,12),(44,18)),('C',(36,31),(44,28),(40,30)),('L',(39,36)),('A',(36,40),3,4,True),('L',(18,40))],True)
        self.add_dot('eye',(34,23))
