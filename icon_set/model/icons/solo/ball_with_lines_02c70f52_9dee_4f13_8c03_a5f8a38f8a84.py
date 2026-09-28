"""ball-with-lines: Mirrored football panels; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '02c70f52-9dee-4f13-8c03-a5f8a38f8a84'
SOURCE_PATH = 'pictographic-primitives/symbol/ball with lines_02c70f52-9dee-4f13-8c03-a5f8a38f8a84.svg'
AUTHOR = 'gpt-6'

class BallWithLines(Solo48):
    icon_id = 'ball-with-lines'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('solo-ai-refine', 'solo-ai-first50', 'ball-with-lines')

    def build(self):
        # Plan: A true circular ball owns a six-sided central panel and six radial seams. The geometry is derived from shared axes so both horizontal and vertical reflections match exactly; no unequal lower panels.
        # Reference: Original football; exact mirrored panel construction.

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
        axis=24
        ring=[(24,4),(40,12),(44,24),(40,36),(24,44),(8,36),(4,24),(8,12)]
        path('outline',ring[0],[('A',p,20,20,True) for p in ring[1:]+ring[:1]],True)
        # One upper-right panel quadrant owns all paired vertices.
        panel=[(axis,12),(34,18),(34,30),(axis,36),(14,30),(14,18)]
        poly('panel',*panel,closed=True)
        ends=[(24,4),(40,12),(40,36),(24,44),(8,36),(8,12)]
        for j,(a,b) in enumerate(zip(panel,ends)):
         line(f'seam-{j}',a,b);join(f'seam-{j}','panel');join(f'seam-{j}','outline')
