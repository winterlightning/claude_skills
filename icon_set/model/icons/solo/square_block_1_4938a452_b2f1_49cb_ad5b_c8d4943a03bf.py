"""A square selection boundary with four corner handles.
Plan: Four identical rounded square handles derive from two repeated axis positions; connectors meet side midpoints.
Construction: square-dashed: discrete perimeter construction; handle geometry uses rounded-square construction
Envelope: visible (4,4)-(44,44); centerlines (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4938a452-b2f1-49cb-ad5b-c8d4943a03bf'
SOURCE_PATH = 'icon_set/work/todo-references/square block 1_4938a452-b2f1-49cb-ad5b-c8d4943a03bf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-block-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('square', 'block', '1')

    def build(self):
        for row,y in enumerate((6,34)):
            for col,x in enumerate((6,34)):self.box(f'handle-{row}-{col}',x,y,x+8,y+8,2)
        self.add_line('top',(14,10),(34,10))
        self.add_line('bottom',(14,38),(34,38))
        self.add_line('left',(10,14),(10,34))
        self.add_line('right',(38,14),(38,34))
        for edge,connections in {
         'top':[('handle-0-0',(2,3)),('handle-0-1',(8,9))],
         'bottom':[('handle-1-0',(2,3)),('handle-1-1',(8,9))],
         'left':[('handle-0-0',(5,6)),('handle-1-0',(0,11))],
         'right':[('handle-0-1',(5,6)),('handle-1-1',(0,11))]}.items():
            for handle,parts in connections:
                for part in parts:self.relate('connect',edge,f'{handle}-{part}')

    def box(self,name,l=6,t=6,r=42,b=42,rad=4):
        mx,my=(l+r)//2,(t+b)//2
        pts=[(mx,t),(r-rad,t),(r,t+rad),(r,my),(r,b-rad),(r-rad,b),(mx,b),(l+rad,b),(l,b-rad),(l,my),(l,t+rad),(l+rad,t)]
        for i in range(12):
            a,z=pts[i],pts[(i+1)%12]
            if i in (1,4,7,10):self.add_arc(f'{name}-{i}',a,z,radius_x=rad)
            else:self.add_line(f'{name}-{i}',a,z)
        self.add_contour(name,*(f'{name}-{i}' for i in range(12)),closed=True)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def arrow(self,name,start,tip,a,b):
        self.add_line(name+'-shaft',start,tip)
        self.add_polyline(name+'-head',a,tip,b)
        for i in (1,2):self.relate('connect',name+'-shaft',f'{name}-head-{i}')
