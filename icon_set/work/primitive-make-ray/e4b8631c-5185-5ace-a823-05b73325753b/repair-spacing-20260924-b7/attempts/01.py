"""pen tools: fresh spacing repair.
Plan: Paired control handles over a symmetric closed nib with central slit. No useful Lucide inspected for this composition.
Keyshape SQUARE: extrema derived from the profile's standard envelope.
Omissions: Large guide arc, tiny nib hole and separate base band omitted for clearance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e4b8631c-5185-5ace-a823-05b73325753b'
SOURCE_PATH='pictographic-primitives/design/pen tools_e4b8631c-5185-5ace-a823-05b73325753b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='pen-tools'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('pen', 'tools')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,segments,closed=False):
        at=start; members=[]
        for i,s in enumerate(segments):
            eid=f'{n}-{i}'; kind,end,*args=s
            if end==at: continue
            if kind=='L': self.add_line(eid,at,end)
            else: self.add_arc(eid,at,end,radius_x=args[0],sweep=args[1] if len(args)>1 else True)
            at=end; members.append(eid)
        self.add_contour(n,*members,closed=closed)
    def cross(self,n,x,y,r):
        for i,(dx,dy) in enumerate([(-r,0),(r,0),(0,-r),(0,r)]):
            self.add_line(f'{n}-{i}',(x,y),(x+dx,y+dy))
        for i in range(4):
            for j in range(i): self.relate('connect',f'{n}-{i}',f'{n}-{j}')

    def build(self):
        self.circle('left-node',8,10,2);self.circle('right-node',40,10,2)
        self.add_polyline('control-square',(20,6),(28,6),(28,10),(28,14),(20,14),(20,10),closed=True)
        self.add_line('left-control',(10,10),(20,10))
        self.add_line('right-control',(28,10),(38,10))
        for side in ('left','right'):
            self.relate('connect',side+'-control',side+'-node');self.relate('connect',side+'-control','control-square')
        self.add_polyline('nib',(24,24),(12,36),(16,42),(32,42),(36,36),closed=True)
        self.add_line('slit',(24,24),(24,32));self.relate('connect','nib','slit')
