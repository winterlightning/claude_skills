"""bag-44d13a4d: Wide barrel handbag; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '44d13a4d-0f14-45d6-b151-8ea1e0eb4903'
SOURCE_PATH = 'pictographic-primitives/shopping/bag_44d13a4d-0f14-45d6-b151-8ea1e0eb4903.svg'
AUTHOR = 'gpt-6'

class Bag44d13a4d(Solo48):
    icon_id = 'bag-44d13a4d'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ('solo-ai-refine', 'solo-ai-first50', 'bag-44d13a4d')

    def build(self):
        # Plan: A low wide handbag has a tall squared arch handle and a rounded barrel-shaped body. HRECT bounds distinguish its horizontal proportions.
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
        path('handle',(16,20),[('L',(16,12)),('A',(20,8),4,4,True),('L',(28,8)),('A',(32,12),4,4,True),('L',(32,20))])
        path('body',(10,20),[('L',(16,20)),('L',(32,20)),('L',(38,20)),('C',(44,30),(42,20),(44,25)),('C',(34,40),(44,37),(40,40)),('L',(14,40)),('C',(4,30),(8,40),(4,37)),('C',(10,20),(4,25),(6,20))],True)
        join('body','handle')
