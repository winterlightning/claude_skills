"""Treble clef with tall narrow upper loop, straight descending stem and a broad circular central spiral; curve crossings represent one written musical glyph.
Keyshape VRECT_L: exact SOLO48 contract envelope.
Construction references: No useful local Lucide match; original reference informs construction.
Omissions: No staff lines; complete glyph loops retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0bb5de88-a86b-409b-a1eb-82ac6ee78932'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/clef_0bb5de88-a86b-409b-a1eb-82ac6ee78932.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'looped-treble-clef-0bb5de88'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('clef',)
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

        # The vertical stem, upper loop and central spiral use shared crossing nodes.
        path('stem',(24,4),[('L',(24,38)),('A',(18,44),6,6,True),('L',(12,44))])
        path('sweep',(24,4),[('A',(32,12),8,8,True),('B',(8,30),(32,20),(8,21)),('A',(40,30),16,6,False),('B',(28,20),(40,24),(34,20)),('B',(16,28),(20,20),(16,24))])
        join('stem','sweep')
