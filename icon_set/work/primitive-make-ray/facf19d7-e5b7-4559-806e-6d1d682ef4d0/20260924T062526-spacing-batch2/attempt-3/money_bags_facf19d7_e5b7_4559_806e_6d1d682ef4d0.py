"""money bags.
Plan: Front money bag and partially hidden rear bag with shared occlusion-boundary attachment nodes. Open rear crown and broad front crown remove small crown holes. Dollar reduced to main S curve, minor terminal ticks omitted. No useful exact Lucide match.
Keyshape SQUARE: visible bounds (4, 4, 44, 44); centerlines inset 2 from these bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='facf19d7-e5b7-4559-806e-6d1d682ef4d0'
SOURCE_PATH='pictographic-primitives/_uncategorized_27/money bags_facf19d7-e5b7-4559-806e-6d1d682ef4d0.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='money-bags'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('money', 'bags')
    def build(self):
        self.add_polyline('front-crown',(20,6),(38,6),(34,18),(24,18),closed=True)
        self.path('front-body',(24,18),[('L',(20,24)),('A',(14,30),6,6,False),('L',(14,36)),('A',(20,42),6,6,False),('L',(32,42)),('A',(42,32),10,10,False)])
        self.add_bezier('shoulder',(42,32),((42,24),(42,18),(34,18)))
        self.relate('connect','front-body','shoulder');self.relate('connect','front-crown','shoulder')
        self.relate('connect','front-crown','front-body')
        self.add_polyline('back-crown',(6,16),(10,24),(20,24));self.relate('connect','back-crown','front-body')
        self.path('back-body',(10,24),[('A',(6,28),4,4,False),('L',(6,32)),('A',(10,36),4,4,False),('L',(14,36))])
        self.relate('connect','back-body','back-crown');self.relate('connect','back-body','front-body')
        self.add_bezier('dollar',(32,27),((26,25),(26,30),(30,30)),((34,30),(34,34),(28,33)))

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
