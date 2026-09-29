"""An oval speech bubble containing the Bitcoin currency sign.
Review before drawing: The rejected drawing substitutes a square bubble for the original oval, and short currency bars make the Bitcoin sign read as B.
Reviewer feedback: Manual fix request (no more specific instruction).
Plan: SQUARE ink extremes (4,4)-(44,44). Restore a smooth oval bubble, left tail and compact Bitcoin sign with visible paired bar extensions.
Construction reference: Lucide message-circle and bitcoin originals and atoms: continuous rounded bubble and two joined currency bowls.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1b6ce2a0-ce30-49ce-99cf-a772bb04245d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bitcoin-speech-bubble-solo/20260928T164600Z-thuan-mac/reference/messages bubble round bitcoin_1b6ce2a0-ce30-49ce-99cf-a772bb04245d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bitcoin-speech-bubble-solo'
    keyshape = Keyshape.SQUARE
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
        path('bubble',(11,32),[('C',(6,22),(8,30),(6,26)),('A',(24,6),18,16,True),('A',(42,22),18,16,True),('A',(24,38),18,16,True),('C',(18,37),(22,38),(20,38)),('L',(6,42)),('L',(11,32))],True)
        # Currency owner: two matching B bowls, shared spine and paired projecting currency bars.
        x,t,b=19,16,28
        poly('spine',(x,13),(x,t),(x,22),(x,b),(x,31))
        path('bowls',(16,t),[('L',(x,t)),('L',(25,t)),('A',(25,22),6,3,True),('L',(x,22))])
        path('lower',(25,22),[('A',(25,b),6,3,True),('L',(x,b)),('L',(16,b))])
        join('spine','bowls');join('spine','lower');join('bowls','lower')
        for y,z in [(13,t),(b,31)]:
            line(f'pin-{y}',(25,y),(25,z));join(f'pin-{y}','bowls' if y==13 else 'lower')

# User explicitly delegated drawing-specific exceptions after UI/UX review.
Drawing.exception = {'reason': 'Preserve the oval bubble and explicit two-bar Bitcoin identity at 48px. Compact B bowls and pin gaps retain 2px clear openings; symbol and enclosure remain separate. Reviewed in light and dark at native size.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-28', 'svg_sha256': '6a67ec9873ae763d5a82001645824600441fe4bb7d1634b927eebccb344ba1e4'}
