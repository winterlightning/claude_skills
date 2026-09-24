"""Bugle with an open flared bell, mouthpiece and complete oval tube loop. Horizontal tube runs and flare start with matching tangents.
Keyshape HRECT_L: exact SOLO48 contract envelope.
Construction references: No useful local Lucide match; original reference informs construction.
Omissions: Double tube walls reduced to a single stroke, complete loop restored.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1c3b1dee-2c1a-4e89-91de-95172d2201db'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/brass_1c3b1dee-2c1a-4e89-91de-95172d2201db.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'looped-brass-bugle'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('brass',)
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

        path('bell',(4,16),[('L',(25,16)),('B',(44,8),(34,16),(39,13)),('L',(44,32)),('B',(28,24),(38,27),(34,24))])
        path('tube',(20,24),[('L',(28,24)),('A',(28,40),8,8,True),('L',(20,40)),('A',(20,24),8,8,True)],True)
        join('tube','bell')
