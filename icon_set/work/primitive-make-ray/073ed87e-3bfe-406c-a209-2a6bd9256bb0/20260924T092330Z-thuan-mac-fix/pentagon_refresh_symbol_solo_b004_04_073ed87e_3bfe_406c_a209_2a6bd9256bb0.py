"""Lucide refresh-cw: arrow follows the terminal edge. One open pentagonal perimeter with a short, coherent arrowhead; deliberate upper-right opening.
Fresh bad-stroke revision; fixed SOLO48 stroke4, integer grid. Keyshape SQUARE."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '073ed87e-3bfe-406c-a209-2a6bd9256bb0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pentagon-refresh-symbol-solo-b004-04/20260924T092330Z-thuan-mac/reference/pentagon arrow_073ed87e-3bfe-406c-a209-2a6bd9256bb0.svg'
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
    icon_id = 'pentagon-refresh-symbol-solo-b004-04'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('pentagon', 'arrow')
    def build(self):
        s = self
        s.add_polyline('pentagon',(42,22),(36,42),(12,42),(6,20),(24,6),(34,14))
        s.add_polyline('arrowhead',(32,6),(34,14),(26,16));s.relate('connect','pentagon','arrowhead')
