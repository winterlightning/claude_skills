"""No useful exact local Lucide safety-pin match. Retain diagonal wire, circular coil and hooked clasp; replace sharp interior hook with circular return. Attempt preserves the two required openings.
Fresh bad-stroke revision; fixed SOLO48 stroke4, integer grid. Keyshape SQUARE."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e8f5f092-e7e9-4e0f-ad55-5ae52fcdd2e9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__safety-pin/20260924T092330Z-thuan-mac/reference/safety pin_e8f5f092-e7e9-4e0f-ad55-5ae52fcdd2e9.svg'
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
    icon_id = 'safety-pin'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('safety', 'pin')
    def build(self):
        s = self
        path(s,'outline',(6,30),('L',(30,6)),('A',(42,18),12,12,True),('L',(18,42)),('A',(6,30),12,12,True),closed=True)
        s.add_arc('coil',(6,30),(18,42),radius_x=12);s.relate('connect','coil','outline')
        path(s,'clasp-hook',(30,6),('L',(30,12)),('A',(36,18),6,6,False),('L',(36,24)));s.relate('connect','clasp-hook','outline')
