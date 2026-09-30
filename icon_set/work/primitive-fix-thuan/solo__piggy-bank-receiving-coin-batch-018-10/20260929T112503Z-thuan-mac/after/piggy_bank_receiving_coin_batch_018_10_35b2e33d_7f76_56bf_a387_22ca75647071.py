"""Rejected piggy bank was a boxy animal without a rounded back. Restore a round belly, arched rump, ear and two short feet beneath the separate coin. Tail and coin denomination omitted for spacing.
Symbol plan: Lucide piggy-bank original and atomic geometry: rounded body, snout, ear and paired feet; left facing per original.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '35b2e33d-7f76-56bf-a387-22ca75647071'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__piggy-bank-receiving-coin-batch-018-10/20260929T112503Z-thuan-mac/reference/piggy_35b2e33d-7f76-56bf-a387-22ca75647071.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'piggy-bank-receiving-coin-batch-018-10'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('piggy', 'bank', 'receiving', 'coin', 'batch', '018', '10')

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

        circle('coin',29,11,5)
        path('pig',(6,27),[('L',(11,27)),('L',(13,19)),('L',(21,25)),('L',(30,25)),('A',(42,37),12,12,True),('L',(42,38)),('L',(37,42)),('L',(30,42)),('L',(30,38)),('L',(20,38)),('L',(20,42)),('L',(12,42)),('L',(12,35)),('L',(6,35)),('L',(6,27))],True)
