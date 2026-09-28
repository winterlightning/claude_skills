"""Lucide paintbrush: distinct ferrule, rounded handle cap and curved tuft. Shared diagonal band edges preserve width; curved cap replaces chamfered polygon.
Fresh bad-stroke revision; fixed SOLO48 stroke4, integer grid. Keyshape SQUARE."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0ceae122-4d52-44c0-84da-c9168dce14c9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rounded-artist-paintbrush-batch-019-04/20260924T092330Z-thuan-mac/reference/brush_0ceae122-4d52-44c0-84da-c9168dce14c9.svg'
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
    icon_id = 'rounded-artist-paintbrush-batch-019-04'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('brush',)
    def build(self):
        s = self
        path(s,'handle',(24,16),('L',(34,6)),('A',(42,14),8,8,True),('L',(32,24)))
        s.add_polyline('ferrule',(24,16),(32,24),(26,30),(18,22),closed=True)
        path(s,'bristles',(18,22),('A',(6,34),12,12,False),('L',(6,42)),('L',(14,42)),('A',(26,30),12,12,False))
        s.relate('connect','handle','ferrule');s.relate('connect','ferrule','bristles')
