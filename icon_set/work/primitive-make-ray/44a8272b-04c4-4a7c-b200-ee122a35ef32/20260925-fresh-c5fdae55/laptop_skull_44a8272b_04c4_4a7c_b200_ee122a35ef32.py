"""laptop skull, complete SOLO48 composition.
Symbol plan is recorded in build(). Visible keyshape extremes: (2, 6, 46, 42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '44a8272b-04c4-4a7c-b200-ee122a35ef32'
SOURCE_PATH = 'pictographic-primitives/other/laptop skull_44a8272b-04c4-4a7c-b200-ee122a35ef32.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'laptop-skull'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('laptop skull',)

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
        # Taller laptop screen opens the skull's surrounding negative space.
        self.add_polyline('screen',(6,34),(6,6),(42,6),(42,34),(6,34),closed=True)
        self.add_polyline('base',(6,34),(6,42),(42,42),(42,34));self.relate('connect','screen','base')
        self.add_arc('cranium',(16,24),(32,24),radius_x=8)
        self.add_line('jaw-left',(16,24),(16,29));self.add_line('jaw-right',(32,24),(32,29))
        self.relate('connect','cranium','jaw-left');self.relate('connect','cranium','jaw-right')
        for x in (20,28):self.add_dot('eye-'+str(x),(x,23))

