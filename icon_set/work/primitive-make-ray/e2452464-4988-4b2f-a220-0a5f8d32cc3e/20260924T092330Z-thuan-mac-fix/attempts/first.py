"""Lucide paintbrush informs bristle/handle hierarchy; source pointed tuft retained. Smooth bristle quarters and rounded cap replace the angular rejected outline. No useful exact pointed-brush Lucide match.
Fresh bad-stroke revision; fixed SOLO48 stroke4, integer grid. Keyshape SQUARE."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e2452464-4988-4b2f-a220-0a5f8d32cc3e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pointed-paintbrush/20260924T092330Z-thuan-mac/reference/brush_e2452464-4988-4b2f-a220-0a5f8d32cc3e.svg'
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
    icon_id = 'pointed-paintbrush'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('brush',)
    def build(self):
        s = self
        path(s,'handle',(18,22),('L',(34,6)),('A',(42,14),8,8,True),('L',(26,30)))
        path(s,'bristles',(18,22),('A',(8,32),10,10,False),('L',(6,42)),('L',(16,42)),('A',(26,32),10,10,False),('L',(26,30)),('L',(18,22)),closed=True)
        s.relate('connect','handle','bristles')
