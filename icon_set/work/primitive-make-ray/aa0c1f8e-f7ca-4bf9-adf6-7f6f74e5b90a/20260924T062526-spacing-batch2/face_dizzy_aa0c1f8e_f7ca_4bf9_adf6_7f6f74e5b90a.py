"""face dizzy.
Plan: Circular face with two mirrored, visibly wound spiral eyes. Preserve defining windings in selected blocked candidate after five repair rounds; eye/head and internal curl spacing remain unresolved. Human references inspected; no useful Lucide exact match.
Keyshape CIRCLE: visible bounds (2, 2, 46, 46); centerlines inset 2 from these bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='aa0c1f8e-f7ca-4bf9-adf6-7f6f74e5b90a'
SOURCE_PATH='pictographic-primitives/_uncategorized_17/face dizzy_aa0c1f8e-f7ca-4bf9-adf6-7f6f74e5b90a.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='face-dizzy'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('face', 'dizzy')
    def build(self):
        self.circle('head',24,24,20)
        for j,x in enumerate((16,32)):
            side=1 if j==0 else -1
            p=lambda dx,y:(x+side*dx,y)
            self.add_bezier(f'spiral-{j}',p(-6,20),(p(-6,12),p(6,12),p(6,20)),(p(6,26),p(-3,26),p(-3,20)),(p(-3,16),p(2,16),p(2,20)))
        self.circle('mouth',24,34,3)

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
