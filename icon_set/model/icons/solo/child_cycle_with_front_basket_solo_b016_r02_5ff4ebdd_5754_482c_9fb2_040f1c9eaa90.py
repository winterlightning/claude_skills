"""Child cycle with a backrest, seat, basket and two equal wheels; open frame and rounded basket restore the toy silhouette.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction references: Lucide bike circular wheels and round joins.
Omissions: Wheel spokes and small handlebar omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='5ff4ebdd-5754-482c-9fb2-040f1c9eaa90'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/tricycle_5ff4ebdd-5754-482c-9fb2-040f1c9eaa90.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'child-cycle-with-front-basket-solo-b016-r02'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('tricycle',)
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
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        for n,x in [('rear',13),('front',35)]: circle(n,x,35,7)
        path('frame',(13,28),[('L',(13,20)),('L',(24,20)),('B',(35,16),(30,20),(33,18)),('L',(35,28))])
        path('seat',(13,20),[('L',(10,10)),('A',(18,10),4,4,True),('L',(20,14))])
        path('basket',(35,16),[('L',(31,6)),('L',(42,6)),('L',(42,12)),('A',(38,16),4,4,True),('L',(35,16))],True)
        for n in ('rear','front','seat','basket'): join(n,'frame')
