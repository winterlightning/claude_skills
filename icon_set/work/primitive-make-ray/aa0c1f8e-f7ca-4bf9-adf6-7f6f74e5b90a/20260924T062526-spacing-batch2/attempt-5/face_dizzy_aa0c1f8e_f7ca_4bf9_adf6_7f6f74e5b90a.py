"""face dizzy.
Plan: Dizzy face with mirrored spiral eyes and worried open mouth. No useful local Lucide spiral-face match. Preserve visible eye windings; human reference facial vocabulary.
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
        for i,x in enumerate((16,32)):
            self.path(f'spiral-{i}',(x-6,21),[('A',(x+6,21),6,6,True),('A',(x+2,21),2,2,True)])
        self.add_arc('mouth',(21,34),(27,34),radius_x=4,sweep=True)

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
