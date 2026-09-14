"""ball-with-lines: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '02c70f52-9dee-4f13-8c03-a5f8a38f8a84'
SOURCE_PATH = 'icons-json/symbol/ball with lines_02c70f52-9dee-4f13-8c03-a5f8a38f8a84.json'
AUTHOR = 'gpt-6'

class BallWithLinesVariant2(Solo48):
    icon_id = 'ball-with-lines-v2'
    variant_of = 'ball-with-lines'
    variant_label = 'AI stroke review · first 50'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ball', 'with', 'lines', 'symbol', 'solo-ai-first50')

    def build(self):
        # Plan: A circular football owns a central pentagonal panel and five radial seams. Paired lower seams mirror about x=24.
        # Reference: No useful exact Lucide match; geometric construction from the supplied subject.

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
        path('outline',(24,4), [('A',(44,24),20,20,True),('A',(36,40),20,20,True),('A',(12,40),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True)],True)
        poly('panel',(24,15),(34,23),(30,33),(18,33),(14,23),closed=True)
        for j,(a,b) in enumerate((((24,4),(24,15)),((44,24),(34,23)),((36,40),(30,33)),((12,40),(18,33)),((4,24),(14,23)))):
         line(f'seam-{j}',a,b);join(f'seam-{j}','outline');join(f'seam-{j}','panel')

