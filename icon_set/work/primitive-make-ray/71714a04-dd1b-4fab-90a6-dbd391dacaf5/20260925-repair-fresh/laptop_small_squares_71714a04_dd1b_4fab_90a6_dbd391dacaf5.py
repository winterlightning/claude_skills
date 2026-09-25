"""Fresh repair. Parent preserved in previous.py.txt. Supplied reference re-inspected.
See findings.md for current omissions and review; inherited comments describe the parent design.
"""
"""laptop small squares, complete SOLO48 composition.
Symbol plan is recorded in build(). Visible keyshape extremes: (2, 6, 46, 42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '71714a04-dd1b-4fab-90a6-dbd391dacaf5'
SOURCE_PATH = 'pictographic-primitives/other/laptop small squares_71714a04-dd1b-4fab-90a6-dbd391dacaf5.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'laptop-small-squares'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('laptop small squares',)

    def rounded(self,n,x,y,w,h,r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if i%2:self.add_arc(n+str(i),a,b,radius_x=r)
            else:self.add_line(n+str(i),a,b)
        self.add_contour(n,*(n+str(i) for i in range(8)),closed=True)

    def laptop(self):
        # Screen and base own shared hinge endpoints; repeated corner radius 4.
        self.add_line('screen-left',(10,34),(10,10))
        self.add_arc('screen-tl',(10,10),(14,6),radius_x=4)
        self.add_line('screen-top',(14,6),(34,6))
        self.add_arc('screen-tr',(34,6),(38,10),radius_x=4)
        self.add_line('screen-right',(38,10),(38,34))
        self.add_line('hinge',(38,34),(10,34))
        self.add_contour('screen','screen-left','screen-tl','screen-top','screen-tr','screen-right','hinge',closed=True)
        self.add_polyline('base',(10,34),(6,42),(42,42),(38,34))
        self.relate('connect','screen','base')

    def build(self):
        # Two equal left-aligned square tiles within the full laptop composition.
        self.laptop()
        tile=8
        for i,y in enumerate((14,26)):
            self.add_polyline('tile-'+str(i),(18,y),(18+tile,y),(18+tile,y+tile),(18,y+tile),closed=True)
