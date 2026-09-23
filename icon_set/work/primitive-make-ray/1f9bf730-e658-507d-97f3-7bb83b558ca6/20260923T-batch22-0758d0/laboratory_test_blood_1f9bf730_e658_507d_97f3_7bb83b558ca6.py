"""laboratory test blood, complete SOLO48 composition.
Symbol plan is recorded in build(). Visible keyshape extremes: (4, 4, 44, 44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1f9bf730-e658-507d-97f3-7bb83b558ca6'
SOURCE_PATH = 'icon_set/work/todo-references/laboratory test blood_1f9bf730-e658-507d-97f3-7bb83b558ca6.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'laboratory-test-blood'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('laboratory test blood',)

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
        # Tube at left and a separate teardrop at right; two clear semantic parts.
        self.add_polyline('tube-top',(6,20),(6,6),(18,6),(18,20))
        self.add_line('liquid',(6,20),(18,20))
        self.relate('connect','tube-top','liquid')
        self.add_line('tube-right',(18,20),(18,36))
        self.add_arc('tube-bottom',(18,36),(6,36),radius_x=6)
        self.add_line('tube-left',(6,36),(6,20))
        self.add_contour('tube-lower','tube-right','tube-bottom','tube-left')
        self.relate('connect','tube-top','tube-lower')
        self.relate('connect','liquid','tube-lower')
        self.add_line('drop-left',(36,8),(30,20))
        self.add_arc('drop-bottom',(30,20),(42,20),radius_x=6,radius_y=8,sweep=False)
        self.add_line('drop-right',(42,20),(36,8))
        self.add_contour('drop','drop-left','drop-bottom','drop-right',closed=True)
