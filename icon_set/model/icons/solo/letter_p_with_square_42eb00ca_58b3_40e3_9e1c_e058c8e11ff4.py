"""letter p with square, complete SOLO48 composition.
Symbol plan is recorded in build(). Visible keyshape extremes: (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '42eb00ca-58b3-40e3-9e1c-e058c8e11ff4'
SOURCE_PATH = 'icon_set/work/todo-references/letter p with square_42eb00ca-58b3-40e3-9e1c-e058c8e11ff4.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'letter-p-with-square'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('letter p with square',)

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
        # Hand-authored capital P within a square frame; curved bowl and shared stem.
        self.rounded('frame',6,6,36,36,4)
        self.add_line('p-top',(18,15),(26,15))
        self.add_arc('p-bowl',(26,15),(26,25),radius_x=5)
        self.add_line('p-middle',(26,25),(18,25))
        self.add_line('p-upper-stem',(18,25),(18,15))
        self.add_contour('p-loop','p-top','p-bowl','p-middle','p-upper-stem',closed=True)
        self.add_line('p-lower-stem',(18,25),(18,33))
        self.relate('connect','p-loop','p-lower-stem')
