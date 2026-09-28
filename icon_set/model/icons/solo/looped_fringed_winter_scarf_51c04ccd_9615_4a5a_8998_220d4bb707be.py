"""Winter scarf with a soft neck loop and two subtly flared hanging tails; loop and tail junctions are exact and tails remain separate.
Keyshape VRECT_L: exact SOLO48 contract envelope.
Construction references: No useful local Lucide match; original reference informs construction.
Omissions: Fine fringe strands omitted; flared cloth ends retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '51c04ccd-9615-4a5a-8998-220d4bb707be'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/stole_51c04ccd-9615-4a5a-8998-220d4bb707be.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'looped-fringed-winter-scarf'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('stole',)
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

        path('loop',(18,4),[('L',(30,4)),('A',(40,14),10,10,True),('A',(30,24),10,10,True),('L',(18,24)),('A',(8,14),10,10,True),('A',(18,4),10,10,True)],True)
        path('left-tail',(18,24),[('L',(14,44)),('L',(8,42)),('L',(8,14))]);join('left-tail','loop')
        path('right-tail',(30,24),[('L',(30,40)),('L',(40,44)),('L',(40,14))]);join('right-tail','loop')
