"""Beach Sun Lounger.

Plan: Reclining sun lounger with angled backrest, long seat and two feet.
Construction reference: Lucide bed: coherent furniture frame with structural legs; preserve side-view recline.
Keyshape HRECT_L: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f2d03866-b843-450c-8bdf-ed2cf61bd371'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_10/chaise_f2d03866-b843-450c-8bdf-ed2cf61bd371.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'reclining-sun-lounger'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/misc'
    aliases = ()
    keywords = ('beach', 'sun', 'lounger')

    def build(self):
        self.path('seat',[(4,8),(16,30),(44,30)])
        self.add_line('front-leg',(38,30),(44,40))
        self.add_line('back-leg',(18,30),(12,40))
        for leg in ['front-leg','back-leg']:self.relate('connect','seat',leg)

    def circle(self, name, x, y, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r, radius_y=ry)
        self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def path(self, name, points, closed=False):
        self.add_polyline(name, *points, closed=closed)

    def arc(self, name, a, b, r, ry=None, sweep=True):
        self.add_arc(name, a, b, radius_x=r, radius_y=r if ry is None else ry, sweep=sweep)

    def rect(self, name, x, y, w, h, r=4):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f'{name}-{i}'; ids.append(part)
            if i%2: self.arc(part,a,b,r)
            elif a != b: self.add_line(part,a,b)
            else: ids.pop()
        self.add_contour(name,*ids,closed=True)
