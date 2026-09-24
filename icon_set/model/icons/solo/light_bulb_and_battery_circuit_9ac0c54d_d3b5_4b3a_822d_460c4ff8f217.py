"""Bulb and battery with a bent connecting wire at right; pear bulb uses one smooth circular cap and tangent shoulders.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction references: Lucide lightbulb: circular cap and smooth shoulder transitions.
Omissions: Filament and battery polarity omitted because their openings would be too small.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ac0c54d-d3b5-4b3a-822d-460c4ff8f217'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_33/science electricity_9ac0c54d-d3b5-4b3a-822d-460c4ff8f217.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'light-bulb-and-battery-circuit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ()
    keywords = ('science', 'electricity')
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

        path('bulb',(12,26),[('B',(6,16),(12,21),(6,23)),('A',(26,16),10,10,True),('B',(20,26),(26,23),(20,21)),('L',(12,26))],True)
        poly('battery',(6,34),(27,34),(27,42),(6,42),closed=True)
        path('wire',(36,16),[('A',(42,22),6,6,True),('L',(42,36)),('A',(36,42),6,6,True)])
