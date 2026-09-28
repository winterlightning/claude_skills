"""pregnancy-condom: Smooth condom outline; earlier revisions preserved."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f75fbe0c-9baa-5e37-ad68-e15a64925d22'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pregnancy-condom/20260927T170540Z-thuan-mac-1/reference/pregnancy condom_f75fbe0c-9baa-5e37-ad68-e15a64925d22.svg'
AUTHOR = "gpt-6"

class PregnancyCondom(Solo48):
    icon_id = 'pregnancy-condom'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'pregnancy-condom')

    def build(self):
        # Plan: Preserve the diagonal sleeve and rolled rim; use a smooth reservoir shoulder instead of tiny overlapping cap segments.
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
        path('body',(8,31),[('L',(27,12)),('C',(35,8),(31,8),(33,8)),('C',(40,6),(37,8),(38,6)),('C',(42,10),(42,6),(42,8)),('C',(36,21),(42,14),(39,18)),('L',(17,40))])
        path('rim',(6,29),[('L',(8,31)),('L',(17,40)),('L',(19,42))]);join('rim','body')
