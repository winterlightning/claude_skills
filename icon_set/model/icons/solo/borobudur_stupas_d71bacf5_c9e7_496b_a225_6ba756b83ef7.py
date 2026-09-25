from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd71bacf5-c9e7-496b-a225-6ba756b83ef7'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/chandi borobudur_d71bacf5-c9e7-496b-a225-6ba756b83ef7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'borobudur-stupas'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    categories = ('landmarks', 'primitives')
    aliases = ()
    keywords = ('chandi borobudur',)
    # Plan: A central spired stupa and two smaller domes rise from a shared stepped temple base.
    # Construction references: Original Borobudur reference: dominant central stupa and smaller flanking stupas.
    # Omissions: Small side spires omitted because they crowd the platform walls.
    def build(self):
        # Stepped temple platform supports three bell-shaped stupas, central tower taller.
        self.path('temple',(6,42),[(6,36),((10,32),4,4,True),((14,36),4,4,True),(14,28),(18,28),(18,24),((24,18),6,6,True),((30,24),6,6,True),(30,28),(34,28),(34,36),((38,32),4,4,True),((42,36),4,4,True),(42,42),(6,42)],True)
        self.add_line('spire',(24,6),(24,18));self.relate('connect','spire','temple')

    def path(self, name, start, steps, closed=False):
        current = start
        ids = []
        for index, step in enumerate(steps):
            ident = f"{name}-{index}"
            if len(step) == 2:
                self.add_line(ident, current, step)
                current = step
            else:
                end, rx, ry, sweep = step
                self.add_arc(ident, current, end, radius_x=rx, radius_y=ry, sweep=sweep)
                current = end
            ids.append(ident)
        self.add_contour(name, *ids, closed=closed)

    def circle(self, name, cx, cy, r):
        self.path(name, (cx-r,cy), [((cx+r,cy),r,r,True),((cx-r,cy),r,r,True)], True)

    def box(self, name, x, y, w, h, r=3):
        self.path(name,(x+r,y),[(x+w-r,y),((x+w,y+r),r,r,True),(x+w,y+h-r),
            ((x+w-r,y+h),r,r,True),(x+r,y+h),((x,y+h-r),r,r,True),(x,y+r),((x+r,y),r,r,True)],True)
