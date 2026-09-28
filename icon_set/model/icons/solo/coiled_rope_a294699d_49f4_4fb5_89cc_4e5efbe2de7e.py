"""coiled-rope: Two diagonal rope loops with one broad waist binding. Second loop is the half-turn of the first, using shared radii. Extra tight wraps omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a294699d-49f4-4fb5-89cc-4e5efbe2de7e'
SOURCE_PATH = 'pictographic-primitives/outdoors/outdoors rope 1_a294699d-49f4-4fb5-89cc-4e5efbe2de7e.svg'
AUTHOR = 'gpt-6'


class CoiledRope(Solo48):
    icon_id = 'coiled-rope'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('rope', 'coil', 'climbing', 'camping', 'knot', 'cord', 'outdoors', 'outdoors-batch-02')

    def build(self):
        # Plan: Two diagonal rope loops with one broad waist binding. Second loop is the half-turn of the first, using shared radii. Extra tight wraps omitted.
        # Lucide lasso original and atomic-debug inspected for construction.
        # Human scenes use icon_set/references/human_ref/full_body_ref.png.
        # Centerline envelope: (6, 6, 42, 42).
        def path(name, start, commands, closed=False):
            members, here = [], start
            for i, (kind, end, *args) in enumerate(commands):
                part = f"{name}-{i}"
                if kind == 'L':
                    self.add_line(part, here, end)
                else:
                    rx, ry, sweep = args
                    self.add_arc(part, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                members.append(part)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [('A',(cx+r,cy),r,r,True),('A',(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line, poly = self.add_line, self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        poly('binding',(14,20),(20,14),(24,18),(30,24),(34,28),(28,34),(24,30),(18,24),closed=True)
        for i in range(2):
            def p(x,y): return (x,y) if i==0 else (48-x,48-y)
            path(f'loop-{i}',p(24,18),[('L',p(24,12)),('A',p(30,6),6,6,True),('L',p(36,6)),('A',p(42,12),6,6,True),('L',p(42,18)),('A',p(36,24),6,6,True),('L',p(30,24))])
            join(f'loop-{i}','binding')
