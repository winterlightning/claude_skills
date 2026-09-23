"""The letters GDPR inside a rounded rectangular panel.
SOLO48 HRECT_M; geometry authored independently from the rendered reference.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '06655b8e-39ad-4051-aafc-316a27ffb14a'
SOURCE_PATH = 'icon_set/work/todo-references/gdpr text in rectangle_06655b8e-39ad-4051-aafc-316a27ffb14a.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'gdpr-text-in-rectangle'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/signs'
    aliases = ()
    keywords = ('gdpr', 'text', 'in', 'rectangle')

    def line(self, n, a, b):
        self.add_line(n,a,b)

    def arc(self,n,a,b,rx,ry=None,sweep=True):
        self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)

    def rect(self,n,x,y,w,h,r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if i%2:self.arc(f"{n}-{i}",a,b,r)
            else:self.line(f"{n}-{i}",a,b)
        self.add_contour(n,*(f"{n}-{i}" for i in range(8)),closed=True)

    def build(self):
        # Plan: rounded frame and four hand-built single-line glyphs in one row.
        self.rect('frame',4,10,40,28,3)
        self.add_polyline('g',(13,19),(10,18),(8,21),(8,27),(10,30),(13,29),(13,25),(11,25))
        self.line('d-stem',(18,18),(18,30))
        self.arc('d-bowl',(18,18),(18,30),5,6)
        self.relate('connect','d-stem','d-bowl')
        for n,x in [('p',27),('r',36)]:
            self.line(n+'-stem',(x,30),(x,18))
            self.arc(n+'-bowl',(x,18),(x,24),4,3)
            self.relate('connect',n+'-stem',n+'-bowl')
        self.line('r-leg',(36,24),(41,30));self.relate('connect','r-leg','r-stem');self.relate('connect','r-leg','r-bowl')
