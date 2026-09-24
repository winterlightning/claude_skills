"""emoji gift lover hug 1.
Plan: Face hugging ribboned gift; mirrored eye arcs, open face contour, squared gift. Lucide gift shared ribbon nodes; human references inform facial vocabulary. Recompose gift upright for space.
Keyshape SQUARE: visible bounds (4, 4, 44, 44); centerlines inset 2 from these bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4de1746e-1e17-4608-9148-82107fed5099'
SOURCE_PATH='pictographic-primitives/_uncategorized_16/emoji gift lover hug 1_4de1746e-1e17-4608-9148-82107fed5099.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='emoji-gift-lover-hug-1'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('emoji', 'gift', 'lover', 'hug', '1')
    def build(self):
        self.path('face',(6,24),[('A',(24,6),18,18,True),('A',(42,24),18,18,True),('A',(30,36),12,12,True)])
        self.add_polyline('gift',(6,28),(18,28),(30,28),(30,42),(18,42),(6,42),closed=True)
        self.add_line('ribbon',(18,28),(18,42));self.relate('connect','gift','ribbon')
        self.add_arc('arm',(30,36),(22,36),radius_x=4,sweep=True);self.relate('connect','arm','face');self.relate('connect','arm','gift')
        for i,x in enumerate((18,30)):self.add_arc(f'eye-{i}',(x-2,18),(x+2,18),radius_x=3,sweep=True)
        self.add_arc('smile',(21,23),(27,23),radius_x=4,sweep=False)

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
