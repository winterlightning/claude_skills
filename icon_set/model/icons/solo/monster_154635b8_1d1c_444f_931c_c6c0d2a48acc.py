"""monster.
Plan: Angry horned monster with raised arms and two legs. Horns merged into outer silhouette to avoid undersized horn holes; matched brows convey anger. Omit minor mouth and hand curls to maintain facial and arm clearance. No useful Lucide exact match; mirrored construction.
Keyshape SQUARE: visible bounds (4, 4, 44, 44); centerlines inset 2 from these bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='154635b8-1d1c-444f-931c-c6c0d2a48acc'
SOURCE_PATH='pictographic-primitives/_uncategorized_27/monster_154635b8-1d1c-444f-931c-c6c0d2a48acc.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='monster'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('monster',)
    def build(self):
        self.add_polyline('body',(10,14),(6,6),(18,14),(30,14),(42,6),(38,14),(38,26),(38,42),(28,42),(28,34),(20,34),(20,42),(10,42),(10,26),closed=True)
        for n,side in [('left',-1),('right',1)]:
            p=lambda dx,y:(24+side*dx,y)
            self.add_line(n+'-arm',p(14,26),p(18,22));self.relate('connect','body',n+'-arm')
            self.add_line(n+'-brow',p(6,22),p(4,24))

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
