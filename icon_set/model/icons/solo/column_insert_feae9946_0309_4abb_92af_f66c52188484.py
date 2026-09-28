"""Two separate columns with a downward insertion chevron between them.
Plan: No defining parts omitted; columns share dimensions and rounding.
Lucide construction references: columns-2.
Keyshape SQUARE: (4,4)-(44,44) ink.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = 'feae9946-0309-4abb-92af-f66c52188484'
SOURCE_PATH = 'icon_set/work/todo-references/column insert_feae9946-0309-4abb-92af-f66c52188484.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'column-insert'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('column', 'insert')

    def circle(self, name, cx, cy, radius):
        self.add_arc(name+'-top',(cx-radius,cy),(cx+radius,cy),radius_x=radius)
        self.add_arc(name+'-bottom',(cx+radius,cy),(cx-radius,cy),radius_x=radius)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self, name, left, top, right, bottom, radius):
        # Shared corner radius and a bottom-centre attachment node.
        mid=(left+right)//2
        pts=[(left+radius,top),(right-radius,top),(right,top+radius),
             (right,bottom-radius),(right-radius,bottom),(mid,bottom),
             (left+radius,bottom),(left,bottom-radius),(left,top+radius),(left+radius,top)]
        members=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            key=f'{name}-{i}';members.append(key)
            if i in (1,3,6,8): self.add_arc(key,a,b,radius_x=radius)
            else: self.add_line(key,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
        # Two matching column definitions flank the central downward insertion chevron.
        for name,left in [('left-column',6),('right-column',30)]:
            self.box(name,left,20,left+12,42,3)
        self.add_polyline('insert',(18,6),(24,12),(30,6))

