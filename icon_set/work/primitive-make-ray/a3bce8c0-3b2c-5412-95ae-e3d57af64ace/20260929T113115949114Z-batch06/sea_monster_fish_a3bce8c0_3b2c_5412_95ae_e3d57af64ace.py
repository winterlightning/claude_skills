"""Rejected sea monster was an angular star-like shape with a cramped jaw. Restore a curved open mouth, round head, dorsal fin and sweeping hooked tail.
Symbol plan: Original reference curvature and open jaw; no useful exact Lucide match.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a3bce8c0-3b2c-5412-95ae-e3d57af64ace'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sea-monster-fish/20260929T112503Z-thuan-mac/reference/fantasy leviathan fish_a3bce8c0-3b2c-5412-95ae-e3d57af64ace.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'sea-monster-fish'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sea', 'monster', 'fish')

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

        path('fish',(6,8),[('C',(28,10),(14,4),(22,6)),('L',(38,6)),('L',(35,18)),('C',(32,27),(32,21),(31,24)),('C',(42,30),(34,32),(39,34)),('L',(42,36)),('A',(36,42),6,6,True),('C',(23,32),(30,42),(26,36)),('L',(14,42)),('L',(17,30)),('C',(6,24),(10,30),(6,27)),('A',(6,8),10,10,False)],True)
        self.add_dot('eye',(22,17))
