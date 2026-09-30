"""Envelopes: rejected back envelope lacks its flap and front corners are square. Restore two flap cues and rounded sheet corners. Round the front corners and restore a rear flap descending behind the foreground envelope.
Symbol plan: Lucide mail original and atomic geometry: rounded envelope corners with diagonal flap folds; overlapping pair per source.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3b4efb64-ab06-49d1-9d84-ece28a78b1ca'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-mail-envelopes-batch-007-13/20260929T115456Z-thuan-mac/reference/envelope back front_3b4efb64-ab06-49d1-9d84-ece28a78b1ca.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'two-mail-envelopes-batch-007-13'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('two', 'mail', 'envelopes', 'batch', '007', '13')

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

        path('rear',(6,30),[('L',(6,9)),('A',(9,6),3,3,True),('L',(29,6)),('A',(32,9),3,3,True),('L',(32,18))])
        poly('rear-flap',(6,10),(17,19),(23,14));join('rear','rear-flap')
        box('front',16,18,42,42,3);join('front','rear')
        poly('flap',(17,19),(29,30),(41,19));join('flap','front');join('rear-flap','front')
