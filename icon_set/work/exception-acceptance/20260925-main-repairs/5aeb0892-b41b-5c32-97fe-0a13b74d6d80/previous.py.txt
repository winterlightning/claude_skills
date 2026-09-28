'Document with text content.\nPlan: VRECT_L preserves portrait paper. Enlarged fold with tangent corner and two text rules at pitch8.\nReference: file-text; Folded outline, smooth page corners and repeated text rules.\nChanges: No parts omitted; fold enlarged to avoid the pinched pocket.'
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
        self.add_line('top',(12,4),(24,4))
        self.add_line('fold-diagonal',(24,4),(40,19))
        self.add_line('right',(40,19),(40,40))
        self.add_arc('bottom-right',(40,40),(36,44),radius_x=4)
        self.add_line('bottom',(36,44),(12,44))
        self.add_arc('bottom-left',(12,44),(8,40),radius_x=4)
        self.add_line('left',(8,40),(8,8))
        self.add_arc('top-left',(8,8),(12,4),radius_x=4)
        self.add_contour('page','top','fold-diagonal','right','bottom-right','bottom','bottom-left','left','top-left',closed=True)
        self.add_line('fold-vertical',(24,4),(24,15))
        self.add_arc('fold-corner',(24,15),(28,19),radius_x=4,sweep=False)
        self.add_line('fold-bottom',(28,19),(40,19))
        self.add_contour('fold','fold-vertical','fold-corner','fold-bottom')
        self.relate('connect','page','fold')
        for i,y in enumerate([27,35]):self.add_line(f'text-{i}',(17,y),(31,y))

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

PARENT_MODULE = 'icon_set/model/icons/solo/common_file_text_5aeb0892_b41b_5c32_97fe_0a13b74d6d80.py'
