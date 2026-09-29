"""A rounded square speech bubble containing Bitcoin.
Review before drawing: The current tail continues directly from the left wall instead of the inset source tail, and the currency bars disappear into B.
Reviewer feedback: Manual fix request (no more specific instruction).
Plan: SQUARE ink extremes (4,4)-(44,44). Rounded box with inset lower-left tail and a clear Bitcoin sign with both projecting bars.
Construction reference: Lucide message-square and bitcoin originals and atoms: rounded enclosure with one tail and joined currency bowls.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '692b5811-84ae-4db0-8d66-219feaafec3e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bitcoin-message-speech-bubble-solo/20260928T164600Z-thuan-mac/reference/messages bubble square bitcoin_692b5811-84ae-4db0-8d66-219feaafec3e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bitcoin-message-speech-bubble-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('bitcoin', 'message', 'speech', 'bubble', 'solo')

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
        path('bubble',(12,6),[('L',(36,6)),('A',(42,12),6,6,True),('L',(42,30)),('A',(36,36),6,6,True),('L',(23,36)),('L',(12,42)),('L',(12,36)),('A',(6,30),6,6,True),('L',(6,12)),('A',(12,6),6,6,True)],True)

        # Currency owner: two matching B bowls, shared spine and paired projecting currency bars.
        x,t,b=19,15,31
        poly('spine',(x,11),(x,t),(x,23),(x,b),(x,35))
        path('bowls',(16,t),[('L',(x,t)),('L',(25,t)),('A',(25,23),6,4,True),('L',(x,23))])
        path('lower',(25,23),[('A',(25,b),6,4,True),('L',(x,b)),('L',(16,b))])
        join('spine','bowls');join('spine','lower');join('bowls','lower')
        for y,z in [(11,t),(b,35)]:
            line(f'pin-{y}',(25,y),(25,z));join(f'pin-{y}','bowls' if y==11 else 'lower')
