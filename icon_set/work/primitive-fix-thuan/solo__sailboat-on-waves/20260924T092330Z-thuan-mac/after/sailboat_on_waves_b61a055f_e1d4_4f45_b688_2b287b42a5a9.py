"""Restored leaning curved sail, coherent open hull and two equal wave lobes; omitted the duplicate deck edge for clearance.
Construction: Lucide sailboat: separate sail and open hull; source sail leans left. Replace vertical quarter-circle sail and vague water line with leaning curved sail and two equal wave lobes; omit deck duplicate.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b61a055f-e1d4-4f45-b688-2b287b42a5a9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sailboat-on-waves/20260924T092330Z-thuan-mac/reference/boat_b61a055f-e1d4-4f45-b688-2b287b42a5a9.svg'
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
    icon_id = 'sailboat-on-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('boat',)
    def build(self):
        s = self
        path(s,'sail',(16,6),('L',(22,22)),('L',(36,20)),('A',(16,6),20,14,False),closed=True)
        s.add_polyline('hull',(6,28),(12,31),(36,31),(42,28))
        path(s,'wave',(6,40),('A',(24,40),9,2,False),('A',(42,40),9,2,False))
