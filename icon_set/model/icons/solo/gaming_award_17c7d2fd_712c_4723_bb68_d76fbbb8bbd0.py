"""gaming award.
Plan: Mirrored smooth laurel branches with open foliage strokes and crossing base. Lucide sprout informs curved plant stems and leaf attachments. Reduce three leaves per branch to two and omit closed inner leaf outlines for clear negative space.
Keyshape SQUARE: visible bounds (4, 4, 44, 44); centerlines inset 2 from these bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='17c7d2fd-712c-4723-bb68-d76fbbb8bbd0'
SOURCE_PATH='pictographic-primitives/video-games/batch-04/gaming award_17c7d2fd-712c-4723-bb68-d76fbbb8bbd0.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='gaming-award'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases=()
    keywords=('gaming', 'award')
    def build(self):
        for side in (-1,1):
            p=lambda x,y:(24+side*(x-24),y)
            n='left' if side==1 else 'right'
            self.add_line(n+'-top',p(12,6),p(12,18))
            self.add_bezier(n+'-curve',p(12,18),(p(12,22),p(13,25),p(16,28)),(p(18,32),p(22,35),p(24,36)))
            self.add_line(n+'-tail',p(24,36),p(34,42))
            self.add_contour(n+'-stem',n+'-top',n+'-curve',n+'-tail')
            self.add_arc(n+'-leaf-0',p(6,10),p(12,18),radius_x=10,sweep=side<0)
            self.add_arc(n+'-leaf-1',p(6,24),p(16,28),radius_x=12,sweep=side<0)
            for j in (0,1):self.relate('connect',n+'-stem',f'{n}-leaf-{j}')
        self.relate('connect','left-stem','right-stem')

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
