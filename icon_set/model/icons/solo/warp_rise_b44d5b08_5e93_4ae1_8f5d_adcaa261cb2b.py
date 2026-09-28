"""warp-rise: Even rising wave bands; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b44d5b08-5e93-4ae1-8f5d-adcaa261cb2b'
SOURCE_PATH = 'pictographic-primitives/design/warp rise_b44d5b08-5e93-4ae1-8f5d-adcaa261cb2b.svg'
AUTHOR = 'gpt-6'

class WarpRise(Solo48):
    icon_id = 'warp-rise'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'warp-rise')

    def build(self):
        # Plan: Preserve the rising three-line ribbon; repeat the same curve with equal offsets for consistent spacing.
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
        path('ribbon',(6,18),[('C',(42,6),(21,18),(27,6)),('L',(42,18)),('L',(42,30)),('C',(6,42),(27,30),(21,42)),('L',(6,30)),('L',(6,18))],True)
        path('middle',(6,30),[('C',(42,18),(21,30),(27,18))]);join('middle','ribbon')
