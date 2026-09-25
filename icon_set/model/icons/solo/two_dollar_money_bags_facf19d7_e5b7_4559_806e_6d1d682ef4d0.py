"""money bags.
Plan: Two money bags, open front neck and lower crown leave room for recognizable dollar with terminal stems. Rear crown simplified to open fold. Preserve genuine shared rear/front junctions. No useful Lucide exact match.
Keyshape SQUARE: visible bounds (4, 4, 44, 44); centerlines inset 2 from these bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='facf19d7-e5b7-4559-806e-6d1d682ef4d0'
SOURCE_PATH='pictographic-primitives/_uncategorized_27/money bags_facf19d7-e5b7-4559-806e-6d1d682ef4d0.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='two-dollar-money-bags'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('money', 'bags')
    def build(self):
        self.add_polyline('crown',(24,14),(20,6),(38,6),(36,14))
        self.path('front-left',(24,14),[('A',(14,24),10,10,False),('L',(14,36)),('A',(20,42),6,6,False),('L',(32,42)),('A',(42,32),10,10,False)])
        self.add_bezier('front-right',(42,32),((42,22),(42,20),(36,14)))
        self.relate('connect','crown','front-left');self.relate('connect','crown','front-right');self.relate('connect','front-left','front-right')
        self.add_polyline('back-crown',(6,16),(10,24),(14,24));self.relate('connect','back-crown','front-left')
        self.path('back-body',(10,24),[('A',(6,28),4,4,False),('L',(6,32)),('A',(10,36),4,4,False),('L',(14,36))])
        self.relate('connect','back-body','back-crown');self.relate('connect','back-body','front-left')
        self.add_line('dollar-top',(30,20),(30,22))
        self.add_bezier('dollar-s',(30,22),((20,22),(22,28),(28,28)),((34,28),(34,33),(26,33)))
        self.add_contour('dollar','dollar-top','dollar-s')

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
