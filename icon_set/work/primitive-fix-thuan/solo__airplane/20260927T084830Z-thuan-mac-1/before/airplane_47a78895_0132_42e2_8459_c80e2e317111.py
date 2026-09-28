"""airplane: Swept wings · diagonal; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '47a78895-0132-42e2-8459-c80e2e317111'
SOURCE_PATH = 'pictographic-primitives/other/airplane_47a78895-0132-42e2-8459-c80e2e317111.svg'
AUTHOR = 'gpt-6'

class Airplane(Solo48):
    icon_id = 'airplane'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('solo-ai-refine', 'solo-ai-first50', 'airplane')

    def build(self):
        # Plan: One complete airplane outline mirrors across x+y=48. Both swept wings and both tailplanes are present, with a tangent circular nose. Square bounds keep a generous diagonal wingspan.
        # Reference: Lucide plane: original and atomic-debug geometry.

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
        # Half of the plane defines every paired wing and tail coordinate.
        half=[(24,16),(8,12),(6,16),(18,24),(12,30),(6,28),(6,36),(12,36)]
        reflect=lambda p:(48-p[1],48-p[0])
        commands=[('C',half[0],(32,6),(30,10))]
        commands += [('L',p) for p in half[1:]]
        commands += [('L',reflect(p)) for p in reversed(half[:-1])]
        commands += [('C',(42,12),(38,18),(42,16)),('A',(36,6),6,6,False)]
        path('airframe',(36,6),commands,True)
