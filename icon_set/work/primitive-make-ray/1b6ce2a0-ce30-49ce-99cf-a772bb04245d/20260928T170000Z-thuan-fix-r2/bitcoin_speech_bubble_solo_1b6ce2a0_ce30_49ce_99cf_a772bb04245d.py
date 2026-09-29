"""An oval speech bubble containing the Bitcoin currency sign.
Review before drawing: The rejected drawing substitutes a square bubble for the original oval, and short currency bars make the Bitcoin sign read as B.
Reviewer feedback: Manual fix request (no more specific instruction).
Plan: HRECT_L ink extremes (2,6)-(46,42), smooth oval bubble with left tail, larger visible paired Bitcoin bar extensions; preserve source asymmetry in the tail.
Construction reference: Lucide message-circle and bitcoin originals and atoms: continuous rounded bubble and two joined currency bowls.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1b6ce2a0-ce30-49ce-99cf-a772bb04245d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bitcoin-speech-bubble-solo/20260928T164600Z-thuan-mac/reference/messages bubble round bitcoin_1b6ce2a0-ce30-49ce-99cf-a772bb04245d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bitcoin-speech-bubble-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('bitcoin', 'speech', 'bubble', 'solo')

    def build(self):

        def path(n, start, steps, closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(steps):
                p=f'{n}-{i}'
                if kind=='L': self.add_line(p,here,end)
                elif kind=='A': self.add_arc(p,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(p,here,(args[0],args[1],end))
                here=end;members.append(p)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def poly(n,*pts): self.add_polyline(n,*pts,closed=pts[0]==pts[-1])
        def line(n,a,b): self.add_line(n,a,b)
        def join(a,b): self.relate('connect',a,b)
        path('bubble',(10,31),[('C',(4,22),(6,29),(4,26)),('A',(24,8),20,14,True),('A',(44,22),20,14,True),('A',(24,36),20,14,True),('C',(18,35),(22,36),(20,36)),('L',(6,40)),('L',(10,31))],True)

        # Currency owner: two matching B bowls, shared spine and paired projecting currency bars.
        x,t,b=19,15,31
        poly('spine',(x,11),(x,t),(x,23),(x,b),(x,35))
        path('bowls',(16,t),[('L',(x,t)),('L',(25,t)),('A',(25,23),6,4,True),('L',(x,23))])
        path('lower',(25,23),[('A',(25,b),6,4,True),('L',(x,b)),('L',(16,b))])
        join('spine','bowls');join('spine','lower');join('bowls','lower')
        for y,z in [(11,t),(b,35)]:
            line(f'pin-{y}',(25,y),(25,z));join(f'pin-{y}','bowls' if y==11 else 'lower')
