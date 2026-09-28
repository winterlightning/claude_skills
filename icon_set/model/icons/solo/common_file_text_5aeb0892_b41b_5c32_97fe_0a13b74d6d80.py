"""A text document has a folded upper-right corner and two text lines.
Symbol plan: Portrait page with equal radius-4 corners, diagonal fold and two repeated text rules at pitch 9.
Keyshape visible bounds: (6, 2, 42, 46).
Construction references: Lucide file-text: coherent folded page and text bars; supplied reference: two long text lines and smooth folded corner..
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5aeb0892-b41b-5c32-97fe-0a13b74d6d80'
SOURCE_PATH = 'pictographic-primitives/files/common file text_5aeb0892-b41b-5c32-97fe-0a13b74d6d80.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'common-file-text'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('common', 'file', 'text')
    def build(self):
        self.add_line('top',(12,4),(28,4))
        self.add_line('fold-diagonal',(28,4),(40,16))
        self.add_line('right',(40,16),(40,40))
        self.add_arc('bottom-right',(40,40),(36,44),radius_x=4)
        self.add_line('bottom',(36,44),(12,44))
        self.add_arc('bottom-left',(12,44),(8,40),radius_x=4)
        self.add_line('left',(8,40),(8,8))
        self.add_arc('top-left',(8,8),(12,4),radius_x=4)
        self.add_contour('page','top','fold-diagonal','right','bottom-right','bottom','bottom-left','left','top-left',closed=True)
        self.add_line('fold-vertical',(28,4),(28,12))
        self.add_arc('fold-corner',(28,12),(32,16),radius_x=4,sweep=False)
        self.add_line('fold-bottom',(32,16),(40,16))
        self.add_contour('fold','fold-vertical','fold-corner','fold-bottom')
        self.relate('connect','page','fold')
        for i,y in enumerate([25,34]):self.add_line(f'text-{i}',(17,y),(31,y))

    def circle(self, name, cx, cy, r):
        self.add_arc(name+"-top", (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+"-bottom", (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+"-top", name+"-bottom", closed=True)

    def box(self, name, left, top, right, bottom, r=3):
        points = [(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                  (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f"{name}-{i}"
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
            members.append(part)
        self.add_contour(name,*members,closed=True)
