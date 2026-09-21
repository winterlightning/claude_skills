"""Baking Flour Sifter.

Plan: Semicircular flour sifter and handle, with a centered row of falling grains.
Construction reference: Lucide soup: semicircular bowl attached to a horizontal rim; repeated grains share spacing.
Keyshape HRECT_L: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd268d76a-a04f-4964-9dfa-50ef4b8866a4'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_09/cake sifter_d268d76a-a04f-4964-9dfa-50ef4b8866a4.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'flour-sifter-with-falling-grains'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/misc'
    aliases = ()
    keywords = ('baking', 'flour', 'sifter')

    def build(self):

        self.add_line('rim',(4,8),(32,8))
        self.arc('sieve',(32,8),(4,8),14,16)
        self.add_contour('bowl','rim','sieve',closed=True)
        self.add_line('handle',(32,8),(44,8));self.relate('connect','bowl','handle')
        for i,x in enumerate((8,20,32)): self.add_line(f'grain-{i}',(x,34),(x,40))

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
