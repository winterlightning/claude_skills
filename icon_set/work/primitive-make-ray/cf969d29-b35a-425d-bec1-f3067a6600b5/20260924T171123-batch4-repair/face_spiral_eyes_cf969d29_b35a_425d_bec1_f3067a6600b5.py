"""Hypnotized face with spiral eyes.
Plan: CIRCLE preserves the round face. Spiral turns and inter-eye spacing remain inadequate; not visually approved.
Reduction: Spiral turn count reduced; straight mouth retained.
Construction references: Original reference supplies opposing windings; human facial vocabulary, no useful exact Lucide match used.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cf969d29-b35a-425d-bec1-f3067a6600b5'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_18/face spiral eyes_cf969d29-b35a-425d-bec1-f3067a6600b5.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id='face-spiral-eyes'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('face', 'spiral', 'eyes')
    def build(self):
        # Shared mirrored coil definition: opening, spacing and winding remain explicit.
        self.circle('head',24,24,20)
        for j,x in enumerate((16,32)):
            side=1 if j==0 else -1
            q=lambda dx,y:(x+side*dx,y)
            self.add_bezier(f'spiral-{j}',q(-7,20),(q(-7,9),q(7,9),q(7,20)),(q(7,30),q(-3,30),q(-3,20)),(q(-3,16),q(2,16),q(2,20)))
        self.add_line('mouth',(21,34),(27,34))
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