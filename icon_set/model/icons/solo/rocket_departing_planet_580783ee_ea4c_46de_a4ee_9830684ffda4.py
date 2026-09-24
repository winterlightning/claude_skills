"""Restored a curved pointed rocket body with swept fins, a larger circular planet and a clean departure trail. Omitted the tiny separate exhaust mark; preserved upward-right direction.
Construction: Lucide rocket: pointed body with swept fins. Circular planet and diagonal departure trail remain; tiny separate exhaust omitted. Asymmetry is directional.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '580783ee-ea4c-46de-a4ee-9830684ffda4'
SOURCE_PATH = 'pictographic-primitives/science/rocket earth_580783ee-ea4c-46de-a4ee-9830684ffda4.svg'
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
    icon_id = 'rocket-departing-planet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('rocket', 'earth')
    def build(self):
        s = self
        path(s,'planet',(14,17),('A',(6,29),13,13,False),('A',(14,41),13,13,False),('A',(19,42),13,13,False),('A',(31,34),13,13,False))
        path(s,'rocket',(24,16),('L',(28,16)),('A',(42,6),14,10,True),('A',(34,22),8,16,True),('L',(34,26)),('L',(24,16)),closed=True)
        path(s,'trail',(6,42),('A',(14,41),8,1,False),('L',(23,28)));s.relate('connect','planet','trail')
