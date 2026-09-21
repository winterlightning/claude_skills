"""Baby in Rocking Cradle.

Plan: Cradle with baby head above a broad front panel and rocking base; omit post decoration.
Construction reference: human_ref/user.svg: round baby head; cradle is a physical supporting object.
Keyshape SQUARE: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aaf97260-0761-4f35-b2ef-c885751d9b03'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_13/cradle_aaf97260-0761-4f35-b2ef-c885751d9b03.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'baby-seated-in-rocking-cradle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/misc'
    aliases = ()
    keywords = ('baby', 'in', 'rocking', 'cradle')

    def build(self):
        self.circle('head',24,10,4)
        self.rect('cradle',8,22,32,8,3)
        self.arc('rocker',(6,38),(42,38),18,4,sweep=False)
        self.add_line('support',(24,30),(24,42))
        self.relate('connect','cradle','support');self.relate('connect','rocker','support')

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
