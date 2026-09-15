"""horn: Balanced horn outline; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '82d50937-0e36-4f84-b67b-aafe2b74a0ce'
SOURCE_PATH = 'icons-json/transportation/horn_82d50937-0e36-4f84-b67b-aafe2b74a0ce.json'
AUTHOR = 'gpt-6'

class Horn(Solo48):
    icon_id = 'horn'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('solo-ai-full-set', 'horn')

    def build(self):
        # Plan: Preserve both flared ends and the U-shaped lower loop; use shared horizontal neck dimensions.
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
        path('horn',(4,8),[('L',(14,18)),('L',(34,18)),('L',(44,8)),('L',(44,32)),('L',(34,26)),('L',(14,26)),('L',(4,32)),('L',(4,8))],True)
        path('loop',(14,26),[('L',(14,36)),('A',(18,40),4,4,False),('L',(30,40)),('A',(34,36),4,4,False),('L',(34,26))]);join('loop','horn')
