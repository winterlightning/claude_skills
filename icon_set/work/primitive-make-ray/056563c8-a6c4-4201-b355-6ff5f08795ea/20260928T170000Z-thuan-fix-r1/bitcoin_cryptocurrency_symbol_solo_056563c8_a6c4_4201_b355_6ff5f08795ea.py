"""A Bitcoin sign within a circular coin border.
Review before drawing: The current sign has almost no projecting currency bars and reads as a plain B, unlike the original Bitcoin mark.
Reviewer feedback: Manual fix request (no more specific instruction).
Plan: CIRCLE radius 22 ink about (24,24). Keep the circular border and enlarge both top and bottom currency extensions while balancing the two bowls.
Construction reference: Lucide bitcoin original and atoms: a common stem, paired bowls, and explicit currency extensions; the source supplies the upright orientation.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '056563c8-a6c4-4201-b355-6ff5f08795ea'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bitcoin-cryptocurrency-symbol-solo/20260928T164600Z-thuan-mac/reference/circle bitcoin_056563c8-a6c4-4201-b355-6ff5f08795ea.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bitcoin-cryptocurrency-symbol-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('bitcoin', 'cryptocurrency', 'symbol', 'solo')

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
        circle('coin',24,24,20)

                # Currency owner: two matching B bowls, shared spine and paired projecting currency bars.
                x,t,b=19,15,31
                poly('spine',(x,11),(x,t),(x,23),(x,b),(x,35))
                path('bowls',(16,t),[('L',(x,t)),('L',(25,t)),('A',(25,23),6,4,True),('L',(x,23))])
                path('lower',(25,23),[('A',(25,b),6,4,True),('L',(x,b)),('L',(16,b))])
                join('spine','bowls');join('spine','lower');join('bowls','lower')
                for y,z in [(11,t),(b,35)]:
                    line(f'pin-{y}',(25,y),(25,z));join(f'pin-{y}','bowls' if y==11 else 'lower')
