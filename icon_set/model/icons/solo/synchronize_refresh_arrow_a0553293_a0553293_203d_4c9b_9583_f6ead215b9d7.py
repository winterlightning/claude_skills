"""synchronize-refresh-arrow-a0553293: Smooth refresh curve; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a0553293-203d-4c9b-9583-f6ead215b9d7'
SOURCE_PATH = 'icons-json/interface-essential/synchronize refresh arrow_a0553293-203d-4c9b-9583-f6ead215b9d7.json'
AUTHOR = 'gpt-6'

class SynchronizeRefreshArrowA0553293(Solo48):
    icon_id = 'synchronize-refresh-arrow-a0553293'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('solo-ai-full-set', 'synchronize-refresh-arrow-a0553293')

    def build(self):
        # Plan: Preserve rotation direction and open-ring length; use matching quarter ellipses and a shared arrow point.
        # Reference: Original subject; preserve the distinctive silhouette and proportions.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L" and tuple(end) == tuple(here):
                    continue
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
        def pt(x,y):return (48-x,y) if True else (x,y)
        commands=[('A',pt(26,8),18,16,False),('A',pt(44,24),18,16,False),('A',pt(26,40),18,16,False)]
        if False:commands.append(('C',pt(10,32),pt(19,40),pt(14,37)))
        path('curve',pt(8,24),commands)
        path('head',pt(4,19),[('L',pt(8,24)),('L',pt(13,19))]);join('head','curve')
