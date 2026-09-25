"""A desktop computer monitor with a bottom bezel and tapered stand.
Plan: No omissions; mirrored pedestal and rounded display retained.
Lucide construction references: monitor.
Keyshape SQUARE: (4,4)-(44,44) ink.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = 'a857f0fd-7c79-4e85-aa88-a49b91dc1b32'
SOURCE_PATH = 'icon_set/work/todo-references/computer_a857f0fd-7c79-4e85-aa88-a49b91dc1b32.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'computer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('computer',)

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
        # Large rounded display with an 8-unit bottom bezel and tapered pedestal.
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right-1',(42,10),(42,26))
        self.add_line('right-2',(42,26),(42,30))
        self.add_arc('br',(42,30),(38,34),radius_x=4)
        bottom=[(38,34),(29,34),(19,34),(10,34)]
        for i,(a,b) in enumerate(zip(bottom,bottom[1:])):self.add_line(f'bottom-{i}',a,b)
        self.add_arc('bl',(10,34),(6,30),radius_x=4)
        self.add_line('left-1',(6,30),(6,26))
        self.add_line('left-2',(6,26),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('display','top','tr','right-1','right-2','br','bottom-0','bottom-1','bottom-2','bl','left-1','left-2','tl',closed=True)
        self.add_line('bezel',(6,26),(42,26))
        self.relate('connect','display','bezel')
        for name,x1,x2 in [('left',19,17),('right',29,31)]:
            self.add_line('pedestal-'+name,(x1,34),(x2,42))
            self.relate('connect','display','pedestal-'+name)
        self.add_polyline('foot',(14,42),(17,42),(31,42),(34,42))
        self.relate('connect','foot','pedestal-left')
        self.relate('connect','foot','pedestal-right')

