"""Diagonal kitchen knife with a broad curved blade and smoothly rounded handle. Shared seam has no extra shoulder kink.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction references: Lucide utensils: coherent blade edge and handle.
Omissions: No handle rivets; diagonal orientation fits the full knife.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1dc2167f-9221-4801-9aa7-1f646f10bc31'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/knife edge_1dc2167f-9221-4801-9aa7-1f646f10bc31.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'kitchen-knife'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('knife', 'edge')
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

        path('outline',(6,6),[('L',(28,22)),('L',(40,34)),('B',(42,38),(42,36),(42,36)),('B',(38,42),(42,40),(40,42)),('B',(34,40),(36,42),(36,42)),('L',(22,28)),('B',(6,6),(10,28),(6,18))],True)
        line('seam',(28,22),(22,28));join('outline','seam')
