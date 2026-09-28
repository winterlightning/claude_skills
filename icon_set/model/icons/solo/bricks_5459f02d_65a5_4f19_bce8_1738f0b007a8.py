"""bricks: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5459f02d-65a5-4f19-bce8-1738f0b007a8'
SOURCE_PATH = 'pictographic-primitives/symbol/bricks_5459f02d-65a5-4f19-bce8-1738f0b007a8.svg'
AUTHOR = 'gpt-6'

class Bricks(Solo48):
    icon_id = 'bricks'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('bricks', 'symbol', 'solo-ai-next50')

    def build(self):
        # Plan: A brick wall has two broad courses and staggered vertical joints. Exact shared endpoints and one course-height parameter keep mortar gaps consistent.
        # Reference: Lucide brick-wall original and atomic-debug construction.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L":
                    self.add_line(ident, here, end)
                elif kind == "A":
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == "C":
                    c1, c2 = args
                    self.add_bezier(ident, here, (c1, c2, end))
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [("A",(cx+r,cy),r,r,True), ("A",(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name, (x0+r,y0), [
                ("L",(x1-r,y0)), ("A",(x1,y0+r),r,r,True),
                ("L",(x1,y1-r)), ("A",(x1-r,y1),r,r,True),
                ("L",(x0+r,y1)), ("A",(x0,y1-r),r,r,True),
                ("L",(x0,y0+r)), ("A",(x0+r,y0),r,r,True)], True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate("connect",a,b)
        poly('wall',(4,8),(18,8),(44,8),(44,24),(44,40),(30,40),(4,40),(4,24),closed=True)
        poly('course',(4,24),(18,24),(30,24),(44,24));line('top-joint',(18,8),(18,24));line('bottom-joint',(30,24),(30,40))
        for n in ('course','top-joint','bottom-joint'):join(n,'wall')
        join('top-joint','course');join('bottom-joint','course')
