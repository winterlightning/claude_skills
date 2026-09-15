"""A narrow-necked flask with a rounded lower body contains a curved plant stem rising through its mouth. One broad pointed leaf leans upper-right, and a horizontal liquid line crosses the flask's shoulder.

VRECT_XL visible bounds (6,2)-(42,46); open flask neck widened around a seedling. Liquid line omitted; leaf retained. Lucide flask-conical informed vessel construction. Plant leans right intentionally.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '043bbb0a-ec23-47f4-bd3b-7394bf708232'
SOURCE_PATH = 'pictographic-primitives/science/gmo_043bbb0a-ec23-47f4-bd3b-7394bf708232.svg'
AUTHOR = 'gpt-6'

class SeedlingInLaboratoryFlask(Solo48):
    icon_id = 'seedling-in-laboratory-flask'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('seedling', 'flask', 'plant', 'biotechnology', 'laboratory', 'gmo')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.segments('neck-left',(14,23),(14,28),(8,36))
        self.add_arc('bowl-left',(8,36),(16,44),radius_x=8,sweep=False)
        self.add_line('bottom',(16,44),(32,44))
        self.add_arc('bowl-right',(32,44),(40,36),radius_x=8,sweep=False)
        self.segments('neck-right',(40,36),(34,28),(34,23))
        self.add_contour('flask','neck-left-1','neck-left-2','bowl-left','bottom','bowl-right','neck-right-1','neck-right-2')
        self.add_line('rim-left',(10,23),(14,23));self.add_line('rim-right',(34,23),(38,23))
        self.relate('connect','rim-left','flask');self.relate('connect','rim-right','flask')
        self.add_line('stem',(24,33),(24,16))
        self.add_arc('leaf-top',(24,16),(40,4),radius_x=16,radius_y=12)
        self.add_arc('leaf-bottom',(40,4),(24,16),radius_x=16,radius_y=12)
        self.add_contour('leaf','leaf-top','leaf-bottom',closed=True)
        self.relate('connect','stem','leaf')
