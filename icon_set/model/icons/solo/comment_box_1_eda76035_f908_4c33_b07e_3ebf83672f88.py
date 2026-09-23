"""An empty rounded comment box with a lower-left speech tail.
Plan: No omissions; deliberate lower-left tail asymmetry preserved.
Lucide construction references: message-square.
Keyshape SQUARE: (4,4)-(44,44) ink.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = 'eda76035-f908-4c33-b07e-3ebf83672f88'
SOURCE_PATH = 'icon_set/work/todo-references/comment box 1_eda76035-f908-4c33-b07e-3ebf83672f88.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'comment-box-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('comment', 'box', '1')

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
        # A single rounded speech panel with a lower-left triangular tail.
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right',(42,10),(42,30))
        self.add_arc('br',(42,30),(38,34),radius_x=4)
        tail=[(38,34),(24,34),(14,42),(14,34),(10,34)]
        for i,(a,b) in enumerate(zip(tail,tail[1:])):self.add_line(f'tail-{i}',a,b)
        self.add_arc('bl',(10,34),(6,30),radius_x=4)
        self.add_line('left',(6,30),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('bubble','top','tr','right','br','tail-0','tail-1','tail-2','tail-3','bl','left','tl',closed=True)

