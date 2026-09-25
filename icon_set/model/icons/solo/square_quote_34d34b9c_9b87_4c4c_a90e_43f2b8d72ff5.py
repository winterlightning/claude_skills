"""Two closing quotation marks inside a square.
Repair plan: Equal circular bowls with exactly 4-unit centerline diameter and open descending tails.
Omissions: Inner return edge of each comma tail.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '34d34b9c-9b87-4c4c-a90e-43f2b8d72ff5'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_35/square quote_34d34b9c-9b87-4c4c-a90e-43f2b8d72ff5.svg'
AUTHOR = 'gpt-6'
# Plan: Rounded square containing two matching closing quotation marks.
# References: quote: repeated rounded upper bowls and descending hooked tails.
# Reduction: No parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'square-quote'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('square', 'quote')

    def build(self):
        self.box("frame",6,6,42,42,4)
        # Shared circular bowls and open tails avoid narrow comma interiors.
        for n,x in [('left',17),('right',31)]:
            self.circle(n,x,19,2)
            self.add_bezier(n+'-tail',(x+2,19),((x+2,25),(x+1,29),(x-2,31)))
            self.relate('connect',n,n+'-tail')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,l,t,r,b,q=4):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)
