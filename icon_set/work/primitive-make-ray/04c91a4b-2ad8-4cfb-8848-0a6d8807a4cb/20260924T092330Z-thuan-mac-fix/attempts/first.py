"""Lucide refresh-cw: circular turns and corner arrowheads. Rotational pair uses radius20 and shared integer 3-4-5 radial points; preserve two opposing arrows.
Fresh bad-stroke revision; fixed SOLO48 stroke4, integer grid. Keyshape SQUARE."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '04c91a4b-2ad8-4cfb-8848-0a6d8807a4cb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__recycling/20260924T092330Z-thuan-mac/reference/recycling_04c91a4b-2ad8-4cfb-8848-0a6d8807a4cb.svg'
AUTHOR = "gpt-6"

def path(s,n,start,*steps,closed=False):
    ids=[]; here=start
    for i,c in enumerate(steps):
        k,end,*args=c; ident=f'{n}-{i}'
        if k=='L': s.add_line(ident,here,end)
        else: s.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
        ids.append(ident);here=end
    s.add_contour(n,*ids,closed=closed)

def circle(s,n,x,y,r):
    path(s,n,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

def box(s,n,l,t,r,b,k=3):
    path(s,n,(l+k,t),('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True),closed=True)

class Drawing(Solo48):
    icon_id = 'recycling'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('recycling',)
    def build(self):
        s = self
        path(s,'upper',(6,26),('A',(26,6),20,20,True),('A',(42,14),20,20,True))
        s.add_polyline('upper-head',(34,14),(42,14),(42,6));s.relate('connect','upper','upper-head')
        path(s,'lower',(42,22),('A',(22,42),20,20,True),('A',(6,34),20,20,True))
        s.add_polyline('lower-head',(14,34),(6,34),(6,42));s.relate('connect','lower','lower-head')
