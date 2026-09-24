"""Two interlocking diagonal chain links. A half-turn repeats one smooth capsule-like open link; tangent corners and long diagonal runs retain the chain.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction references: Lucide link: two opposing open link contours with diagonal straights.
Omissions: None; deliberate diagonal orientation retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f183456b-fb13-4447-905a-cd134fb7972e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/link_f183456b-fb13-4447-905a-cd134fb7972e.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'interlocking-chain-links-f183456b'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('link',)
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

        for i in (0,1):
         p=lambda x,y:(x,y) if i==0 else (48-x,48-y)
         path(f'link-{i}',p(21,27),[('B',p(32,28),p(24,31),p(28,32)),('L',p(39,21)),('B',p(42,14),p(41,19),p(42,17)),('B',p(34,6),p(42,10),p(38,6)),('B',p(27,9),p(31,6),p(29,7))])
