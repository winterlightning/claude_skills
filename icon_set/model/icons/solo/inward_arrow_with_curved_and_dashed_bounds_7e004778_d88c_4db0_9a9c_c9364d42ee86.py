"""Down-left arrow inside a smooth quarter-circle with detached top dash and outer corner dash. Arrow arms share one tip.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction references: No useful local Lucide match; original reference informs construction.
Omissions: Long dashed boundary reduced to a top dash and an L-shaped corner dash.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7e004778-d88c-4db0-9a9c-c9364d42ee86'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/transform inside_7e004778-d88c-4db0-9a9c-c9364d42ee86.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'inward-arrow-with-curved-and-dashed-bounds'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('transform', 'inside')
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

        path('boundary',(6,6),[('A',(42,42),36,36,True)])
        line('dash-top',(32,6),(34,6));line('corner-dash',(42,6),(42,12))
        line('shaft',(25,23),(11,37));poly('head',(11,25),(11,37),(23,37));join('shaft','head')
