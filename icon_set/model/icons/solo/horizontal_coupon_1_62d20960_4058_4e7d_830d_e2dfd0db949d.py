"""horizontal coupon 1, re-authored as one complete SOLO48 composition.
Symbol plan is recorded in build(); paired shapes share dimensions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '62d20960-4058-4e7d-830d-e2dfd0db949d'
SOURCE_PATH = 'icon_set/work/todo-references/horizontal coupon 1_62d20960-4058-4e7d-830d-e2dfd0db949d.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'horizontal-coupon-1'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    categories = ("container",)
    aliases = ()
    keywords = ('horizontal coupon 1',)

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)

    def rounded(self,n,x,y,w,h,r):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i in range(8):
            a,b=points[i],points[(i+1)%8]
            if i%2:self.add_arc(n+str(i),a,b,radius_x=r)
            else:self.add_line(n+str(i),a,b)
        self.add_contour(n,*(n+str(i) for i in range(8)),closed=True)

    def heart(self):
        # Paired nine-unit lobes and mirrored lower shoulders.
        self.add_arc('left-lobe',(24,15),(6,15),radius_x=9,sweep=False)
        self.add_arc('left-shoulder',(6,15),(10,25),radius_x=14,sweep=False)
        self.add_line('point-1',(10,25),(24,42))
        self.add_line('point-2',(24,42),(38,25))
        self.add_arc('right-shoulder',(38,25),(42,15),radius_x=14,sweep=False)
        self.add_arc('right-lobe',(42,15),(24,15),radius_x=9,sweep=False)
        self.add_contour('heart','left-lobe','left-shoulder','point-1','point-2','right-shoulder','right-lobe',closed=True)

    def build(self):
        # Outward side lobes, not inward ticket notches; paired elliptical ends.
        self.add_line('top-1',(10, 14),(10, 10))
        self.add_line('top-2',(10, 10),(38, 10))
        self.add_line('top-3',(38, 10),(38, 14))
        self.add_arc('right-lobe',(38,14),(38,34),radius_x=6,radius_y=10)
        self.add_line('bottom-1',(38, 34),(38, 38))
        self.add_line('bottom-2',(38, 38),(10, 38))
        self.add_line('bottom-3',(10, 38),(10, 34))
        self.add_arc('left-lobe',(10,34),(10,14),radius_x=6,radius_y=10)
        self.add_contour('coupon','top-1','top-2','top-3','right-lobe','bottom-1','bottom-2','bottom-3','left-lobe',closed=True)

# Declared visible keyshape extremes: (2, 8, 46, 40).
