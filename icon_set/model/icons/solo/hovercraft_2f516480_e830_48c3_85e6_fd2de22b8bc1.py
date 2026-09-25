"""Hovercraft with a rounded air cushion, slanted cabin and curved aft fan guard. Roof transition tangent matches slanted windshield.
Keyshape HRECT_M: exact SOLO48 contract envelope.
Construction references: No useful local Lucide match; original reference informs construction.
Omissions: No window glazing or extra skirt seam.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2f516480-e830-48c3-85e6-fd2de22b8bc1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/hovercraft_2f516480-e830-48c3-85e6-fd2de22b8bc1.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'hovercraft'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hovercraft',)
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

        path('hull',(4,28),[('L',(9,28)),('L',(28,28)),('L',(36,28)),('L',(44,28)),('A',(34,38),10,10,True),('L',(14,38)),('A',(4,28),10,10,True)],True)
        path('cabin',(9,28),[('L',(13,16)),('B',(20,10),(15,10),(16,10)),('L',(24,10)),('A',(28,14),4,4,True),('L',(28,28))])
        path('fan',(36,28),[('L',(36,22)),('A',(44,14),8,8,True),('L',(44,28))])
        join('hull','cabin');join('hull','fan')
