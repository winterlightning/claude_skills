"""Bread slice with spreading knife resting diagonally across it; right bread edge meets the crossing handle at an actual occlusion.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction references: No useful local Lucide match; original reference informs construction.
Omissions: Small butter dab omitted; broad blade and bread silhouette retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f9a5cfd4-e289-4257-90a9-77f15fa702fa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/bread slice spread_f9a5cfd4-e289-4257-90a9-77f15fa702fa.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'knife-buttering-bread'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bread', 'slice', 'spread')
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

        path('bread',(8,25),[('B',(6,18),(6,24),(6,22)),('A',(18,6),12,12,True),('L',(30,6)),('A',(42,18),12,12,True),('B',(36,25),(42,22),(40,25)),('L',(36,35))])
        poly('bread-base',(36,35),(36,42),(6,42),(8,25));join('bread','bread-base')
        path('blade',(22,15),[('B',(16,18),(18,12),(16,14)),('B',(30,28),(16,27),(24,31)),('L',(22,15))],True)
        poly('handle',(30,28),(36,35),(42,42));join('blade','handle');join('bread','handle');join('bread-base','handle')
