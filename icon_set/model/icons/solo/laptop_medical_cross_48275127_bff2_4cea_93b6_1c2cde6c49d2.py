"""laptop medical cross, complete SOLO48 composition.
Symbol plan is recorded in build(). Visible keyshape extremes: (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '48275127-bff2-4cea-93b6-1c2cde6c49d2'
SOURCE_PATH = 'icon_set/work/todo-references/laptop medical cross_48275127-bff2-4cea-93b6-1c2cde6c49d2.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'laptop-medical-cross'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("combination", "other", "primitives-generate")
    aliases = ()
    keywords = ('laptop medical cross',)

    def rounded(self,n,x,y,w,h,r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if i%2:self.add_arc(n+str(i),a,b,radius_x=r)
            else:self.add_line(n+str(i),a,b)
        self.add_contour(n,*(n+str(i) for i in range(8)),closed=True)

    def laptop(self):
        # Screen and base own shared hinge endpoints; repeated corner radius 4.
        self.add_line('screen-left',(8,32),(8,12))
        self.add_arc('screen-tl',(8,12),(12,8),radius_x=4)
        self.add_line('screen-top',(12,8),(36,8))
        self.add_arc('screen-tr',(36,8),(40,12),radius_x=4)
        self.add_line('screen-right',(40,12),(40,32))
        self.add_line('hinge',(40,32),(8,32))
        self.add_contour('screen','screen-left','screen-tl','screen-top','screen-tr','screen-right','hinge',closed=True)
        self.add_polyline('base',(8,32),(4,40),(44,40),(40,32))
        self.relate('connect','screen','base')

    def build(self):
        # Complete laptop enclosure and a centered medical plus.
        self.laptop()
        self.add_line('cross-h',(20,20),(28,20))
        self.add_line('cross-v',(24,17),(24,23))
        self.relate('connect','cross-h','cross-v')
