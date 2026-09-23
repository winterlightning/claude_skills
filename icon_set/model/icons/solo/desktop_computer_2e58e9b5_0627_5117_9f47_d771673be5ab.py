"""A desktop display with a lower bezel and tapered stand. All paired corners share radius 3; shared axis x24. Centerline extremes (4,8)-(44,40).
Lucide monitor original and atomic-debug: four tangent quarter-circle corners, centered support, and horizontal foot. Source-specific bezel and stand preserved.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2e58e9b5-0627-5117-9f47-d771673be5ab'
SOURCE_PATH = 'icon_set/work/todo-references/desktop computer_2e58e9b5-0627-5117-9f47-d771673be5ab.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'desktop-computer'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/devices"
    aliases = ()
    keywords = ('desktop', 'computer')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def rounded(self, name, l, t, r, b, radius):
        q=radius
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
        for j in range(8):
            if j%2: self.add_arc(name+str(j),pts[j],pts[j+1],radius_x=q)
            else: self.add_line(name+str(j),pts[j],pts[j+1])
        self.add_contour(name, *(name+str(j) for j in range(8)), closed=True)

    def build(self):

        l,t,r,b,q=4,8,44,30,3
        self.add_line('top',(l+q,t),(r-q,t))
        self.add_arc('top-right',(r-q,t),(r,t+q),radius_x=q)

        self.add_line('right-upper',(r,t+q),(r,22))
        self.add_line('right-lower',(r,22),(r,b-q))

        self.add_arc('bottom-right',(r,b-q),(r-q,b),radius_x=q)
        self.add_line('bottom-1',(r-q,b),(28,b))
        self.add_line('bottom-2',(28,b),(24,b))
        self.add_line('bottom-3',(24,b),(20,b))
        self.add_line('bottom-4',(20,b),(l+q,b))
        self.add_arc('bottom-left',(l+q,b),(l,b-q),radius_x=q)

        self.add_line('left-lower',(l,b-q),(l,22))
        self.add_line('left-upper',(l,22),(l,t+q))
        self.add_arc('top-left',(l,t+q),(l+q,t),radius_x=q)
        self.add_contour('screen',*['top', 'top-right', 'right-upper', 'right-lower', 'bottom-right', 'bottom-1', 'bottom-2', 'bottom-3', 'bottom-4', 'bottom-left', 'left-lower', 'left-upper', 'top-left'],closed=True)
        self.add_line('bezel',(l,22),(r,22))
        self.relate('connect','screen','bezel')

        self.add_line('stand-left',(20,b),(18,40))
        self.add_line('stand-right',(28,b),(30,40))
        self.add_polyline('foot',(14,40),(18,40),(30,40),(34,40))
        for part in ('stand-left','stand-right'):
            self.relate('connect',part,'screen')
            self.relate('connect',part,'foot')
