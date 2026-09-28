"""bag-44d13a4d: Wide barrel handbag; earlier revisions preserved."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '44d13a4d-0f14-45d6-b151-8ea1e0eb4903'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bag-44d13a4d/20260926T085631Z-thuan-mac/reference/bag_44d13a4d-0f14-45d6-b151-8ea1e0eb4903.svg'
AUTHOR = 'claude-opus-5-5'

class Bag44d13a4d(Solo48):
    icon_id = 'bag-44d13a4d'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ('solo-ai-refine', 'solo-ai-first50', 'bag-44d13a4d')

    def build(self):
        # Plan: a handbag: rounded-rectangle body with a semicircular arch handle.
        # Reference: Lucide handbag: original and atomic-debug geometry.

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
        # Review: curved handle + rounded-rectangle bag. SQUARE (6,6)-(42,42):
        # body is an r4 rounded rectangle (6,18)-(42,42); the handle is a
        # semicircular r10 arch about (24,16) on legs that land on the body's
        # top edge at x=14/34 (split points shared with the body outline).
        path('handle',(14,18),[('L',(14,16)),('A',(34,16),10,10,True),('L',(34,18))])
        path('body',(10,18),[('L',(14,18)),('L',(34,18)),('L',(38,18)),('A',(42,22),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,22)),('A',(10,18),4,4,True)],True)
        join('body','handle')
