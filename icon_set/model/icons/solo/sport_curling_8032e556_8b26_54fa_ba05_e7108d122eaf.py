"""sport curling.
Plan: Curling stone upper left, diagonal broom down to lower left, circular marker lower right. No useful Lucide match. Rounded stone and broom with integer cardinal arcs; omit stone seam to open interior.
Keyshape SQUARE: visible bounds (4, 4, 44, 44); centerlines inset 2 from these bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='8032e556-8b26-54fa-ba05-e7108d122eaf'
SOURCE_PATH='pictographic-primitives/sports/sport curling_8032e556-8b26-54fa-ba05-e7108d122eaf.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='sport-curling'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "sports"
    aliases=()
    keywords=('sport', 'curling')
    def build(self):
        self.path('stone',(10,18),[('L',(14,18)),('L',(20,18)),('A',(24,22),4,4,True),('A',(20,26),4,4,True),('L',(10,26)),('A',(6,22),4,4,True),('A',(10,18),4,4,True)],True)
        self.add_polyline('handle',(14,18),(14,10),(22,10));self.relate('connect','handle','stone')
        self.path('broom-head',(28,34),[('L',(28,38)),('A',(24,42),4,4,True),('L',(18,42)),('A',(14,38),4,4,True),('A',(18,34),4,4,True),('L',(28,34))],True)
        self.add_line('shaft',(42,6),(28,34));self.relate('connect','shaft','broom-head')
        self.circle('marker',39,39,3)

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,ops,closed=False):
        at=start; members=[]
        for i,op in enumerate(ops):
            eid=f'{n}-{i}';kind,end,*args=op
            if end==at:continue
            if kind=='L':self.add_line(eid,at,end)
            elif kind=='A':self.add_arc(eid,at,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            at=end;members.append(eid)
        self.add_contour(n,*members,closed=closed)
