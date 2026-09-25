"""A broad shallow bowl beneath three separated, open cabbage curls; circular curls replace collapsed cubic loops.
Keyshape HRECT_L: exact SOLO48 contract envelope.
Construction references: Lucide soup: broad bowl and separate curved food strokes.
Omissions: Many tiny strips reduced to three open curls.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9d6010e3-0f0e-4eff-be58-e66150706645'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/coleslaw_9d6010e3-0f0e-4eff-be58-e66150706645.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'bowl-of-curled-coleslaw'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('coleslaw',)
    def build(self):

        def path(n, start, steps, closed=False):
            ids=[]; p=start
            for i,step in enumerate(steps):
                k=f'{n}-{i}';kind=step[0];q=step[1]
                if kind=='L': self.add_line(k,p,q)
                elif kind=='A': self.add_arc(k,p,q,radius_x=step[2],radius_y=step[3],sweep=step[4])
                elif kind=='B': self.add_bezier(k,p,(step[2],step[3],q))
                ids.append(k);p=q
            self.add_contour(n,*ids,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('bowl',(4,26),[('L',(44,26)),('A',(30,40),14,14,True),('L',(18,40)),('A',(4,26),14,14,True)],True)
        path('curl-left',(8,17),[('A',(16,17),4,4,True)])
        path('curl-center',(23,8),[('A',(31,8),4,4,False)])
        path('curl-right',(39,17),[('A',(43,13),4,4,False)])
