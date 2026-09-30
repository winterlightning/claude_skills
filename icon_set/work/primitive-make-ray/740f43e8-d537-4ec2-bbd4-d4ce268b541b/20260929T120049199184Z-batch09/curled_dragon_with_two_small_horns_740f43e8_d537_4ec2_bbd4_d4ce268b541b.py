"""Horned dragon: rejected head is a long rectangle and the body an open squiggle. Restore a rounded snout and coherent S-curve through the curled body. Round the snout and carry a smooth S-curve from the jaw through the curled tail.
Symbol plan: Original horned dragon: rounded horizontal snout, two horns and flowing S body; no useful direct Lucide match.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '740f43e8-d537-4ec2-bbd4-d4ce268b541b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__curled-dragon-with-two-small-horns/20260929T115456Z-thuan-mac/reference/dragon_740f43e8-d537-4ec2-bbd4-d4ce268b541b.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'curled-dragon-with-two-small-horns'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('curled', 'dragon', 'with', 'two', 'small', 'horns')

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

        path('dragon',(18,12),[('C',(29,14),(23,10),(27,12)),('L',(38,14)),('A',(38,22),4,4,True),('L',(27,22)),('C',(26,28),(20,22),(20,25)),('C',(36,35),(31,30),(36,32)),('C',(24,42),(36,41),(30,42)),('L',(16,42)),('A',(6,32),10,10,True),('C',(8,23),(6,29),(10,26)),('C',(14,29),(13,23),(15,26)),('C',(14,34),(14,31),(11,32)),('L',(23,34)),('C',(20,25),(29,34),(20,29)),('C',(18,12),(12,19),(13,14))],True)
        line('horn-left',(18,12),(13,6));line('horn-right',(25,12),(25,6));join('horn-left','dragon');join('horn-right','dragon')
