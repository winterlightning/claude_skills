"""Video game bowl city.
Symbol plan: Wide round necked vessel contains a two-step open skyline. Shared mirrored bowl controls reach6,6..42,42. City step pitch8; no skyline baseline.
Omissions: Floating ball, city baseline and third stair removed so the defining bowl and stepped skyline retain clearance.
Construction references: No useful Lucide exact game logo; geometric reconstruction from supplied silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='c4822a44-f834-4646-8377-fe8ba010de72'
SOURCE_PATH='pictographic-primitives/_uncategorized_39/video game bowl city_c4822a44-f834-4646-8377-fe8ba010de72.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='video-game-bowl-city'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('video', 'game', 'bowl', 'city')

    def path(self,n,start,ops,closed=False):
        at=start; members=[]
        for i,op in enumerate(ops):
            kind,end,*args=op
            if at==end: continue
            m=f'{n}-{i}'
            if kind=='L': self.add_line(m,at,end)
            elif kind=='A': self.add_arc(m,at,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            else: self.add_bezier(m,at,(args[0],args[1],end))
            members.append(m);at=end
        if closed and at!=start:
            self.add_line(n+'-close',at,start);members.append(n+'-close')
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def rect(self,n,l,t,r,b,k=4,top=(),right=(),bottom=(),left=()):
        ops=[('L',(x,t)) for x in sorted(top) if l+k<x<r-k]
        ops += [('L',(r-k,t)),('A',(r,t+k),k,k,True)]
        ops += [('L',(r,y)) for y in sorted(right) if t+k<y<b-k]
        ops += [('L',(r,b-k)),('A',(r-k,b),k,k,True)]
        ops += [('L',(x,b)) for x in sorted(bottom,reverse=True) if l+k<x<r-k]
        ops += [('L',(l+k,b)),('A',(l,b-k),k,k,True)]
        ops += [('L',(l,y)) for y in sorted(left,reverse=True) if t+k<y<b-k]
        ops += [('L',(l,t+k)),('A',(l+k,t),k,k,True)]
        self.path(n,(l+k,t),ops,True)

    def build(self):
        self.path('bowl',(18,10),[('C',(6,28),(10,12),(6,21)),('C',(24,42),(6,36),(14,42)),('C',(42,28),(34,42),(42,36)),('C',(30,10),(42,21),(38,12))])
        self.add_polyline('neck',(18,10),(18,6),(30,6),(30,10));self.relate('connect','bowl','neck')
        self.add_polyline('city',(16,31),(16,30),(24,30),(24,22),(32,22),(32,31))
