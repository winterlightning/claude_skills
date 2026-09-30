"""Rejected Buddha looked like a bell on a cushion with a center divider. Restore a rounded robed torso, diagonal robe edge and broader crossed-leg base. Halo rays omitted to preserve figure proportions.
Symbol plan: human_ref/user.svg and original seated Buddha; head bottom16, shoulders24 gives exact4 ink gap.
Keyshape VRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9c4fcc62-4575-453e-9566-a7f24bb9a3bd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-buddha-statue/20260929T112503Z-thuan-mac/reference/landmark buddha statue_9c4fcc62-4575-453e-9566-a7f24bb9a3bd.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'seated-buddha-statue'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('seated', 'buddha', 'statue')

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

        circle('head',24,10,6)
        path('robe',(12,34),[('L',(12,30)),('A',(18,24),6,6,True),('L',(30,24)),('A',(36,30),6,6,True),('L',(36,34))])
        path('legs',(12,34),[('A',(8,38),4,4,False),('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(40,38)),('A',(36,34),4,4,False),('L',(12,34))],True)
        join('robe','legs')
        path('fold',(30,24),[('A',(12,34),24,24,True)]);join('fold','robe');join('fold','legs')
