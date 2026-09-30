"""Rejected Pikachu had plain antenna-like ears. Restore long pointed outlined ears and wide cheeks with centered paired eyes. Omit tiny mouth, cheek patches and ear-tip divisions for spacing.
Symbol plan: No useful exact Lucide match; original reference and geometric curves.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0c3a61ea-506a-536d-bd3c-5956c221a50a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pikachu-head/20260929T112503Z-thuan-mac/reference/pokemon pikachu electric mice_0c3a61ea-506a-536d-bd3c-5956c221a50a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'pikachu-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('pikachu', 'head')

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

        path('outline',(12,24),[('L',(6,6)),('C',(19,20),(13,9),(16,15)),('A',(29,20),13,13,True),('C',(42,6),(32,15),(35,9)),('L',(36,24)),('A',(38,32),13,13,True),('C',(24,42),(38,39),(31,42)),('C',(10,32),(17,42),(10,39)),('A',(12,24),13,13,True)],True)
        self.add_dot('eye-l',(19,30));self.add_dot('eye-r',(29,30))
