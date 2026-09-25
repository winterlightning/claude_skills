"""Rebalanced tall bowed sail and leaning mast above an upturned board; separated two equal wave lobes. Omitted sail stripes for clearance.
Construction: Lucide sailboat: clear sail/mast/board hierarchy. Source keeps leaning mast, bowed sail and raised board nose; omit sail stripes, use two equal wave lobes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6e5eb979-36c1-4127-b9b4-93312561e604'
SOURCE_PATH = 'pictographic-primitives/recreation/nautic sports sailing_6e5eb979-36c1-4127-b9b4-93312561e604.svg'
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
    icon_id = 'sailboard-on-waves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    categories = ("primitives", "recreation")
    aliases = ()
    keywords = ('nautic', 'sports', 'sailing')
    def build(self):
        s = self
        path(s,'sail',(18,4),('A',(8,24),30,30,False),('L',(26,24)),('L',(18,4)),closed=True)
        s.add_line('mast',(26,24),(30,33));s.relate('connect','mast','sail')
        s.add_polyline('board',(8,33),(30,33),(40,30));s.relate('connect','mast','board')
        path(s,'wave',(8,42),('A',(24,42),8,2,False),('A',(40,42),8,2,False))
