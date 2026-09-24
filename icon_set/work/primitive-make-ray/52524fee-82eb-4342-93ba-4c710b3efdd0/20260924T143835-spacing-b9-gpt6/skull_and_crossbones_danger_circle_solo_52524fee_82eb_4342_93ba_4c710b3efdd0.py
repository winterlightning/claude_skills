"""circle skull xmark: fresh spacing repair.
Plan: Skull and diagonal crossbones remain recognizable within the ring. Bone runs meet real skull and ring nodes.
Keyshape CIRCLE: CIRCLE preserves the enclosing warning badge.
Omissions: Eyes merged into cheek sockets; center tooth omitted; bone ends joined to border.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='52524fee-82eb-4342-93ba-4c710b3efdd0'
SOURCE_PATH='pictographic-primitives/other/circle skull xmark_52524fee-82eb-4342-93ba-4c710b3efdd0.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='skull-and-crossbones-danger-circle-solo'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('circle', 'skull', 'xmark')

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
        # Outer circle is split at four exact 12-16-20 attachment nodes.
        pts=[(12,8),(36,8),(36,40),(12,40)]
        for i in range(4):self.add_arc(f'ring-{i}',pts[i],pts[(i+1)%4],radius_x=20)
        self.add_contour('ring',*(f'ring-{i}' for i in range(4)),closed=True)
        self.add_bezier('dome',(16,16),((20,12),(28,12),(32,16)))
        self.add_bezier('right-temple',(32,16),((34,18),(34,21),(34,24)))
        self.add_polyline('right-cheek',(34,24),(30,30),(30,32))
        self.add_polyline('left-cheek',(18,32),(18,30),(14,24))
        self.add_bezier('left-temple',(14,24),((14,21),(14,18),(16,16)))
        # Keep continuous runs without nesting polyline contours.
        self.relate('connect','dome','right-temple');self.relate('connect','dome','left-temple')
        self.relate('connect','right-temple','right-cheek');self.relate('connect','left-temple','left-cheek')
        for s in (-1,1):
            side='left' if s<0 else 'right'
            self.add_line(side+'-eye',(24+s*10,24),(24+s*4,24))
            self.relate('connect',side+'-eye',side+'-temple');self.relate('connect',side+'-eye',side+'-cheek')
            self.add_line(side+'-bone-top',(24+s*12,8),(24+s*8,16))
            self.relate('connect',side+'-bone-top','ring');self.relate('connect',side+'-bone-top','dome');self.relate('connect',side+'-bone-top',side+'-temple')
            self.add_line(side+'-bone-bottom',(24+s*6,30),(24+s*12,40))
            self.relate('connect',side+'-bone-bottom',side+'-cheek');self.relate('connect',side+'-bone-bottom','ring')
