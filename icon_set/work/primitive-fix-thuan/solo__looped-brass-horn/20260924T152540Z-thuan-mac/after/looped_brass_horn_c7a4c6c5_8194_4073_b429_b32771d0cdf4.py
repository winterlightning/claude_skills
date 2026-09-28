"""Flugelhorn with left mouthpiece, rounded flare and a closed broad tubing loop. The bell opens at right and tube loop joins lower flare.
Keyshape HRECT_L: exact SOLO48 contract envelope.
Construction references: No useful local Lucide match; original reference informs construction.
Omissions: Doubled tube walls reduced to one coherent stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c7a4c6c5-8194-4073-b429-b32771d0cdf4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__looped-brass-horn/20260924T152540Z-thuan-mac/reference/flugelhorn_c7a4c6c5-8194-4073-b429-b32771d0cdf4.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'looped-brass-horn'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference'
    aliases = ()
    keywords = ('flugelhorn',)
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

        path('bell',(4,16),[('L',(22,16)),('B',(44,8),(34,16),(40,13)),('L',(44,36)),('B',(27,24),(40,28),(35,24))])
        path('tube',(20,24),[('L',(27,24)),('A',(27,40),8,8,True),('L',(20,40)),('A',(20,24),8,8,True)],True)
        join('tube','bell')
