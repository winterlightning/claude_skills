"""web form progress.
Plan: Two repeated circular nodes and central cancellation X on horizontal connector. Radial envelope radius20 preserves reference thin row; no useful Lucide exact match. No omissions.
Keyshape CIRCLE: visible bounds (2, 2, 46, 46); centerlines inset 2 from these bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='93ee9247-04b8-4aa1-b24d-f007fa02d450'
SOURCE_PATH='pictographic-primitives/interface-essential/web form progress_93ee9247-04b8-4aa1-b24d-f007fa02d450.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='web-form-progress'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('web', 'form', 'progress')
    def build(self):
        self.circle('left-node',10,24,6)
        self.circle('right-node',38,24,6)
        self.add_polyline('connector',(16,24),(24,24),(32,24))
        self.add_polyline('cross-a',(20,20),(24,24),(28,28))
        self.add_polyline('cross-b',(20,28),(24,24),(28,20))
        self.relate('connect','left-node','connector')
        self.relate('connect','right-node','connector')
        self.relate('connect','connector','cross-a','cross-b')

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
