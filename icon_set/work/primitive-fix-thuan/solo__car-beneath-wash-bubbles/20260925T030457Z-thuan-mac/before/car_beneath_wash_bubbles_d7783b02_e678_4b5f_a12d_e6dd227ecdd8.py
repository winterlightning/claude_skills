"""Automatic Car Wash Service.

Plan: Front car with paired tires and three wash bubbles; reduce seven bubbles to three.
Construction reference: Lucide car-front: rounded body, trapezoidal windshield and paired wheels.
Keyshape SQUARE: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7783b02-e678-4b5f-a12d-e6dd227ecdd8'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_09/car repair wash 2_d7783b02-e678-4b5f-a12d-e6dd227ecdd8.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'car-beneath-wash-bubbles'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/misc'
    aliases = ()
    keywords = ('automatic', 'car', 'wash', 'service')

    def build(self):

        for i,x in enumerate((10,24,38)): self.circle(f'bubble-{i}',x,9,3)
        self.path('windshield',[(8,30),(14,22),(34,22),(40,30)])
        self.rect('body',6,30,36,8,2)
        self.relate('connect','windshield','body')
        for i,x in enumerate((12,36)):
            self.add_line(f'tire-{i}',(x,38),(x,42)); self.relate('connect','body',f'tire-{i}')

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
