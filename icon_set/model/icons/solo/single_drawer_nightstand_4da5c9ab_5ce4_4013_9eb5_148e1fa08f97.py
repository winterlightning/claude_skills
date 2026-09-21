"""Bedside Nightstand with Drawer.

Plan: Nightstand with one knob, upper drawer and plain lower compartment; shared cabinet width.
Construction reference: No useful exact Lucide match; geometric arc construction.
Keyshape SQUARE: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4da5c9ab-5ce4-4013-9eb5-148e1fa08f97'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/nightstand_4da5c9ab-5ce4-4013-9eb5-148e1fa08f97.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'single-drawer-nightstand'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/misc'
    aliases = ()
    keywords = ('bedside', 'nightstand', 'with', 'drawer')

    def build(self):

        self.rect('cabinet',6,6,36,28,4)
        self.add_line('divider',(6,24),(42,24));self.relate('connect','cabinet','divider')
        self.add_dot('knob',(24,15))
        for i,x in enumerate((12,36)):
            self.add_line(f'leg-{i}',(x,34),(x,42));self.relate('connect','cabinet',f'leg-{i}')

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
