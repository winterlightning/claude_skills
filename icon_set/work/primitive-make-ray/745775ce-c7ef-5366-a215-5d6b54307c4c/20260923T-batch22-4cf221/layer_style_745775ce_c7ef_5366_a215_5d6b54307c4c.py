"""layer style, complete SOLO48 composition.
Symbol plan is recorded in build(). Visible keyshape extremes: (4, 4, 44, 44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '745775ce-c7ef-5366-a215-5d6b54307c4c'
SOURCE_PATH = 'icon_set/work/todo-references/layer style_745775ce-c7ef-5366-a215-5d6b54307c4c.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'layer-style'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('layer style',)

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
        # A slanted lower-case f with curved terminals and a separate x.
        self.add_arc('f-foot',(6,42),(14,34),radius_x=8,sweep=False)
        self.add_line('f-stem',(14,34),(20,18))
        self.add_line('f-neck',(20,18),(20,14))
        self.add_arc('f-hook',(20,14),(28,6),radius_x=8)
        self.add_line('f-terminal',(28,6),(30,6))
        self.add_contour('f','f-foot','f-stem','f-neck','f-hook','f-terminal')
        self.add_polyline('f-bar',(12,18),(20,18),(22,18))
        self.relate('connect','f','f-bar')
        self.add_line('x-down',(30,22),(42,38))
        self.add_line('x-up',(30,38),(42,22))
        self.relate('connect','x-down','x-up')
