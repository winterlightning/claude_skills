"""gaming award.
Plan: Mirrored open laurel branches with three leaf strokes each and crossing base. Lucide sprout: coherent branch attachments. Simplify filled-out leaf outlines to open foliage strokes to preserve six-leaf count without undersized holes.
Keyshape SQUARE: visible bounds (4, 4, 44, 44); centerlines inset 2 from these bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='17c7d2fd-712c-4723-bb68-d76fbbb8bbd0'
SOURCE_PATH='pictographic-primitives/video-games/batch-04/gaming award_17c7d2fd-712c-4723-bb68-d76fbbb8bbd0.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='gaming-award'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('gaming', 'award')
    def build(self):
        # Shared mirrored branch nodes and three open leaf strokes per side.
        for side in (-1,1):
            p=lambda x,y:(24+side*(x-24),y)
            n='left' if side==1 else 'right'
            self.add_polyline(n+'-stem',p(12,6),p(12,18),p(16,28),p(24,36),p(34,42))
            for i,(a,b) in enumerate([((6,10),(12,18)),((6,24),(16,28)),((8,36),(24,36))]):
                self.add_line(f'{n}-leaf-{i}',p(*a),p(*b));self.relate('connect',n+'-stem',f'{n}-leaf-{i}')
        self.relate('connect','left-stem','right-stem')
        self.relate('connect','left-leaf-2','right-stem')
        self.relate('connect','right-leaf-2','left-stem')
        self.relate('connect','left-leaf-2','right-leaf-2')

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
