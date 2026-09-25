"""Burrow mound with shoulder bumps, ground baseline and centered arched entrance; mirror around x24.
Keyshape HRECT_M: exact SOLO48 contract envelope.
Construction references: No useful local Lucide match; original reference informs construction.
Omissions: None; restored the shoulder bumps and ground.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '86626526-ee56-4d45-ae9a-13aba59d21df'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/warren_86626526-ee56-4d45-ae9a-13aba59d21df.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'burrow-entrance-batch-078'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('warren',)
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

        path('mound',(4,38),[('B',(10,30),(4,34),(6,31)),('L',(10,24)),('A',(38,24),14,14,True),('L',(38,30)),('B',(44,38),(42,31),(44,34)),('L',(32,38)),('L',(16,38)),('L',(4,38))],True)
        path('tunnel',(16,38),[('L',(16,33)),('A',(32,33),8,8,True),('L',(32,38))])
        join('mound','tunnel')
