"""face spiral eyes.
Plan: Neutral hypnotized face with two spiral eyes, shortened one-turn curls and straight mouth. No useful local Lucide match. Repeated eye definition preserves paired shape.
Keyshape CIRCLE: visible bounds (2, 2, 46, 46); centerlines inset 2 from these bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cf969d29-b35a-425d-bec1-f3067a6600b5'
SOURCE_PATH='pictographic-primitives/_uncategorized_18/face spiral eyes_cf969d29-b35a-425d-bec1-f3067a6600b5.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='face-spiral-eyes'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('face', 'spiral', 'eyes')
    def build(self):
        self.circle('head',24,24,20)
        for i,x in enumerate((16,32)):
            self.path(f'spiral-{i}',(x-6,21),[('A',(x+6,21),6,6,True),('A',(x+2,21),2,2,True)])
        self.add_line('mouth',(20,34),(28,34))

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
