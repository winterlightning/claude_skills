"""Beer Pint Drinking Glass.

Plan: Tall pint glass with a broad rim band and tapered body; straight symmetric taper.
Construction reference: Lucide glass-water: symmetric tapered vessel and broad internal horizontal band.
Keyshape VRECT_M: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'abfeb248-6514-4811-885e-542a4db3e966'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_31/pint_abfeb248-6514-4811-885e-542a4db3e966.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'tall-pint-glass-rim-band'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('beer', 'pint', 'drinking', 'glass')

    def build(self):

        self.path('glass',[(10,4),(38,4),(38,12),(32,44),(16,44),(10,12)],True)
        self.add_line('rim',(10,12),(38,12));self.relate('connect','glass','rim')

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
